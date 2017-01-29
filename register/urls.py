from django.conf.urls import url, include
from django.contrib import admin
from .views import registerEntry, detailEntry, listEntry, overviewEntry, categoryView, dateView, addCategory, entry_pivot_chart_view

urlpatterns = [
    url(r'^$', registerEntry, name="register"),
    url(r'^(?P<pk>\d+)/detail/$',detailEntry, name="detail"),
    url(r'^all/$', listEntry, name='list'),
    url(r'^overview/$', overviewEntry, name='overview'),
    url(r'^overview/graph/$', entry_pivot_chart_view, name='graph'),
    url(r'^category/$', categoryView, name='cat_view'),
    url(r'^date/$', dateView, name='date_view'),
    url(r'^category/new/$', addCategory, name='add_cat'),



]
