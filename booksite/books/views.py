from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from books.models import Book, Publisher, Author
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView,ListView
#from django.views.generic.list import ListView

def search_form(request):
    return render(request, 'search_form.html')
    
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len	(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books =  Book.objects.filter(title__icontains=q)
			return(render(request, 'search_results.html',
			{'books': books, 'query': q}))
	return(render(request, 'search_form.html', 
	{'errors': errors}))
		
def about_pages(request, page):
	try:
		return(render(request,"about/%s.html" %page))
	except TemplateDoesNotExist:
		raise(Http404())
		
class PublisherPageListView(ListView):
	def get_queryset(self):
		return(Publisher.objects.filter(name__icontains='').order_by('name')) 

class BookListView(ListView):
	model = Book
	
	def head(self, *args, **kwargs):
		last_book = self.get_queryset().latest(
		'publication_date')
		response =  HttpResponse('')
		response['Last-Modified']  = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
		return response

# Complex filtering with wrapper function
def books_by_publisher(request,name):
	#look up publisher (use 404 is not found)
	publisher = get_object_or_404(Publisher,name__iexact=name)
	
	#use object_list view 
	return(ListView.as_view(
		request, 
		queryset = Book.objects.filter(publisher=publisher),
		template_name = 'books/books_by_publisher.html',
		template_object_name = 'book',
		extra_context = {'publisher': publisher}
	))
	
class BookByPublisherListView(ListView):
	publisher = get_object_or_404(Publisher,name__iexact='name')
	template_name = 'books/books_by_publisher.html',
	context_object_name = 'book',
	#extra_context = {'publisher': publisher}
	
	def get_query_set(self):
		return(Book.objects.filter(publisher=publisher),
)

# Complex filtering with class
class BookByPublisherListView1(ListView):
	def books_by_publisher(request,name):
		#look up publisher (use 404 is not found)
		publisher = get_object_or_404(Publisher,name__iexact=name)
	
		#use object_list view 
		return(ListView(
			#request, 
			queryset = Book.objects.filter(publisher=publisher),
			template_name = 'books/books_by_publisher.html',
			context_object_name = 'book',
			extra_context = {'publisher': publisher}
	))
	

