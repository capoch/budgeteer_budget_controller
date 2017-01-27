from django.conf.urls import url, include
from django.contrib import admin
from .views import registerEntry, detailEntry, listEntry, overviewEntry

urlpatterns = [
    url(r'^$', registerEntry, name="register"),
    url(r'(?P<pk>\d+)/detail/$',detailEntry, name="detail"),
    url(r'all/$', listEntry, name='list'),
    url(r'overview/$', overviewEntry, name='overview'),

]
