from django.conf.urls import patterns, include, url
from booksite.views import hello, current_datetime, hours_ahead,display_meta
from django.contrib import admin
from books import views as bviews
from contact import views as cviews
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^hello/$', hello),
	url(r'^time/$', current_datetime),
	url(r'^another-time-page/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^display-meta/',display_meta), 
	url(r'^search-form/$', bviews.search_form),
	url(r'^search/$', bviews.search),
	url(r'^contact-form/$', cviews.contact),
	
    # Examples:
    # url(r'^$', 'booksite.views.home', name='home'),
    # url(r'^booksite/', include('booksite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
