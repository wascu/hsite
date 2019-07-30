from django.views.generic.base import RedirectView
from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    # path('favicon.ico',serve,{'path':'static/booktest/ico/favicon.ico'}),
    # url(r'^index',cache_page(60*15)(views.index),
    url(r'^',views.index),
    # url(r'^cache',views.cache1),
]