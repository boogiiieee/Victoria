# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import simplejson as json
from django.core import exceptions
from django import forms

from annoying.fields import AutoOneToOneField, JSONField

from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^map2gis\.django_2gis_widget\.LocationField"])

DEFAULT_WIDTH = 500
DEFAULT_HEIGHT = 400
DEFAULT_LAT, DEFAULT_LNG = 56.463988, 84.962543
DEFAULT_ADDRESS = u''


class LocationWidget(forms.TextInput):
    def __init__(self, *args, **kw):
        self.map_width = kw.get("map_width", DEFAULT_WIDTH)
        self.map_height = kw.get("map_height", DEFAULT_HEIGHT)

        super(LocationWidget, self).__init__(*args, **kw)
        self.inner_widget = forms.widgets.HiddenInput()

    def render(self, name, value, *args, **kwargs):
        if value is None:
            lat, lon, address = DEFAULT_LAT, DEFAULT_LNG, DEFAULT_ADDRESS
            value = {'lat': lat, 'lon': lon, 'address': address}
        else:
            value = json.loads(value)
            lat, lon, address = float(value['lat']), float(value['lon']), value['address']
        curLocation = json.dumps(value, cls=DjangoJSONEncoder)

        js = '''
            <script type="text/javascript">
            //<![CDATA[
                var map_%(id)s;

                function save_position_%(id)s(point, address) {
                    var input = document.getElementById("id_%(name)s");
                    var location = {'lat':point.getLat().toFixed(12), 'lon':point.getLon().toFixed(12)};
                    location.address = '%(address)s';
                    if (address) {
                        location.address = address;
                    }
                    input.value = JSON.stringify(location);
                    document.getElementById('address_%(name)s').value = location.address;

                    var marker = new DG.Markers.Common({geoPoint:point});
                    map_%(id)s.markers.removeAll();
                    map_%(id)s.markers.add(marker);
                    map_%(id)s.setCenter(point, 16);

                    map_%(id)s.geocoder.get(point, {
                        types: ['district'],
                        success: function(geocoderObjects) {
                            var district = geocoderObjects[0].getShortName();
                            if ( district ) {
                                if ( $('#id_1-map2gis_district').length ) {
                                    $('#id_1-map2gis_district').val(district);
                                    console.log(district);
                                }
                            }
                        }
                    });
                }

                function load_%(id)s() {
                    map_%(id)s = new DG.Map("map_%(name)s");
                    map_%(id)s.controls.add(new DG.Controls.Zoom());
                    var point = new DG.GeoPoint(%(lon)f, %(lat)f);
                    map_%(id)s.setCenter(point, 16);

                    if ('%(address)s' && %(lon)f && %(lat)f) {
                        var marker = new DG.Markers.Common({geoPoint: point});
                        map_%(id)s.markers.add(marker);
                    }

                    map_%(id)s.addEventListener(map_%(id)s.getContainerId(), 'DgClick', function(evt){
                        map_%(id)s.geocoder.get(evt.getGeoPoint(), {
                            types: ['district', 'street', 'living_area', 'place', 'house'],
                            success: function(geocoderObjects) {
                                save_position_%(id)s(geocoderObjects[0].getCenterGeoPoint(), geocoderObjects[0].getName());
                            }
                        });
                    });

                    $('#address_%(name)s').autocomplete({
                        source: function(request, response) {
                            if (request.term.length > 2) {
                                map_%(id)s.geocoder.get(request.term, {
                                    types: ['district', 'street', 'living_area', 'place', 'house'],
                                    limit: 10,
                                    success: function(geocoderObjects) {
                                        response($.map(geocoderObjects, function(item) {
                                            return {
                                                value: item.getName(),
                                                location: item.getCenterGeoPoint()
                                            }
                                        }));
                                    }
                                });
                            }
                        },
                        select: function(event, ui) {
                            save_position_%(id)s(ui.item.location, ui.item.value);
                        }
                    });

                    $('#address_%(name)s').focusout(function(){
                        save_position_%(id)s(map_%(id)s.getCenter(), $('#address_%(name)s').val());
                    });
                }

                $(document).ready(function(){
                    load_%(id)s();
                });
            //]]>
            </script>
        ''' % dict(id=name.replace('-', '_'), name=name, lat=lat, lon=lon, address=address)

        html = self.inner_widget.render("%s" % name, "%s" % curLocation, dict(id='id_%s' % name))

        html += u'<div id="map_%s" style="width:%dpx; height:%dpx"></div>' % (
            name, self.map_width, self.map_height)
        html += u'<label>%s: </label><input id="address_%s" type="text" style="width:200px" />' \
                u'<br />' % (u'Поиск по адресу', name)
        html += u'<span class="def_address">Текущий адрес: %s</span>' % (
            address if address else u'(Не указан)',)

        return mark_safe(html + js)

    class Media:
        css = {'all': (
            'http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css',
        )}
        js = (
            'http://code.jquery.com/jquery-1.7.1.js',
            'http://code.jquery.com/ui/1.10.3/jquery-ui.js',
            'http://maps.api.2gis.ru/1.0',
        )


class LocationField(JSONField):
    def formfield(self, **kwargs):
        defaults = {'widget': LocationWidget}
        return super(LocationField, self).formfield(**defaults)