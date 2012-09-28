from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'demox.views.home', name='home'),
    # url(r'^demox/', include('demox.foo.urls')),

    url(r'^customer/', include('customer.urls', namespace='customer',
        app_name='customer')),

    url(r'^api-auth/', include('djangorestframework.urls',
        namespace='djangorestframework')),

    url(r'^admin/', include(admin.site.urls)),
)
