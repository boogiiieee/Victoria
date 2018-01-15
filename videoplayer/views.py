# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404

#######################################################################################################################
#######################################################################################################################

def add_video_frame(request, lesson_id, url):
	subject_name = None
	if 'subject_name' in request.GET:
		subject_name = request.GET.get('subject_name')
	return render_to_response('frame.html', {'url':url, 'lesson_id':lesson_id, 'subject_name':subject_name}, RequestContext(request))
	
#######################################################################################################################
#######################################################################################################################
