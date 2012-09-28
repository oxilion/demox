from django.conf.urls import patterns, include, url

from . import views

customers = patterns('',
    url(r'^$', views.CustomerList.as_view(), name='list'),
    url(r'^(?P<pk>[^/]+)/$', views.CustomerInstance.as_view(), name='detail'),
    url(r'^(?P<customer>[^/]+)/phone_numbers/$',
        views.PhoneNumberList.as_view(), name='phone_numbers'),
    url(r'^(?P<customer>[^/]+)/phone_numbers/(?P<number>[^/]+)/$',
        views.PhoneNumberInstance.as_view(), name='phone_number'),
)

api = patterns('',
        url(r'^$', views.Root.as_view()),
        url(r'^customers/', include(customers, namespace='customers')),
)

urlpatterns = patterns('',
        url(r'^api/', include(api, namespace='api')),
)
