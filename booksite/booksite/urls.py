from django.conf.urls import *
from django.contrib import admin
#from django.views.generic.list import ListView
from django.views.generic import ListView, DetailView, TemplateView
from books.views import PublisherPageListView, books_by_publisher, \
BookByPublisherListView, BookListView
admin.autodiscover()

#models
from books.models import Publisher

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('booksite.views',
	url(r'^hello/$', 'hello'),
	url(r'^time/$', 'current_datetime'),
	url(r'^another-time-page/$', 'current_datetime'),
	url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
	url(r'^hours/plus/(?P<offset>\d{1,2})/$', 'hours_ahead'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^display-meta/','display_meta'),
	url(r'^image/', 'my_image'),
)

urlpatterns += patterns('books.views', 
	url(r'^search-form/$', 'search_form'),
	url(r'^search/$', 'search'),
	url(r'^about/$', TemplateView.as_view(template_name='about.html')),
	url(r'^about/(\w+)/$', 'about_pages'),
)

urlpatterns += patterns('contact.views',
	url(r'^contact-form/$', 'contact'),
)

publisher_info= {
	'queryset': Publisher.objects.all(),
	'template_name': 'publisher_list.html',
	'template_object_name': 'publisher'
}

def get_books():
	return Book.objects.all()

publisher_info1= {
	'queryset': Publisher.objects.all(),
	'template_object_name': 'publisher',
	'extra_context': {'book_list': get_books}
}

urlpatterns += patterns('books.views', 
	url(r'^publishers1/$', ListView.as_view(),publisher_info),
	url(r'^publishers/$', ListView.as_view(model=Publisher,)),
	url(r'^publishers2/$', ListView.as_view(
		queryset = Publisher.objects.all(),
		template_name = 'publisher_list.html')),
	url(r'^publishers4/$',PublisherPageListView.as_view(
		template_name='publisher_list.html')),
	url(r'^books/(\w+)/$', books_by_publisher),
	url(r'^books1/(\w+)/$', BookByPublisherListView.as_view(), name='books_by_publisher.html'),
	url(r'^datebooks/$', BookListView.as_view()),
)

