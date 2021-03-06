"""djsocketio_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import os
from djsocketio_example.settings import BASE_DIR
import sampleapp.views

urlpatterns = [
	url(r'^$', sampleapp.views.home, name='home'),
	# url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': BASE_DIR+'/static/'}),
	url(r'^admin/', include(admin.site.urls)),
	url("", include('django_socketio.urls')),
	url("^message/$", sampleapp.views.message, name="message"),
]
