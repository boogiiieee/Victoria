# -*- coding: utf-8 -*-

import string
import random

from django import template
from django.template import Node
from django.template import TemplateSyntaxError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.conf import settings


register = template.Library()


def randdigits(n):
    a = string.digits
    return ''.join([random.choice(a) for i in range(n)])

####################################################################################################
#####################################################################################################

#Выводит медиа карты для карты
class MediaMap2GisNode(Node):
    def render(self, context):
        """
        в скриптах установлена прямая загрузка API карт (вместо {{STATIC_URL}} ) -
        не всегда работало корректно
        """
        return mark_safe('''
            <script type="text/javascript" src="http://maps.api.2gis.ru/1.0"></script>
            <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false">
            </script>
        ''' % {'static': settings.STATIC_URL})


def media_map2gis(parser, token):
    bits = token.split_contents()
    if len(bits) != 1: raise TemplateSyntaxError(_("Error token tag \"media_map2gis\""))
    return MediaMap2GisNode()


media_map2gis = register.tag(media_map2gis)

####################################################################################################
####################################################################################################


#Выводит карту
class GetMap2GisNode(Node):
    def __init__(self, location_field, map_width, map_height, zoom):
        """
        :param map_width: ширина div для карты
        :param map_height: высота div для карты
        :param zoom: zoom карты по умолчанию, больше - крупнее, 18 - max
        """
        self.location_field = template.Variable(location_field)
        self.map_width = map_width
        self.map_height = map_height
        self.zoom = zoom

    def render(self, context):
        name = randdigits(10)
        value = self.location_field.resolve(context)
        lat, lon, address = float(value['lat']), float(value['lon']), value['address']
        zoom = self.zoom

        js = '''
            <script type="text/javascript">
            //<![CDATA[
                var map_%(id)s;

                function load_%(id)s() {
                    map_%(id)s = new DG.Map("map_%(id)s");
                    map_%(id)s.controls.add(new DG.Controls.Zoom());
                    var point = new DG.GeoPoint(%(lon)f, %(lat)f);
                    map_%(id)s.setCenter(point, %(zoom)s);

                    if ('%(address)s') {
                        var marker = new DG.Markers.Common({geoPoint: point});
                        map_%(id)s.markers.add(marker);
                    }
                }

                $(function(){
                    load_%(id)s();
                });
            //]]>
            </script>
        ''' % dict(id=name, lat=lat, lon=lon, address=address, zoom=zoom)

        html = u'<div id="map_%s" style="width:%s; height:%s"></div>' % (
            name, self.map_width, self.map_height)
        return mark_safe(html + js)


def get_map2gis_zoom(parser, token):
    bits = token.split_contents()
    if len(bits) != 5:
        raise TemplateSyntaxError(_("Error token tag \"get_map2gis\""))
    return GetMap2GisNode(bits[1], bits[2][1:-1], bits[3][1:-1], bits[4])


get_map2gis_zoom = register.tag(get_map2gis_zoom)

#######################################################################################################################
#######################################################################################################################