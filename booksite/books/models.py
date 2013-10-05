from django.db import models
#from contact.models import Contact_Information

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
	#contact_information = models.ForeignKey(Contact_Information)
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		ordering = ['name']
	
class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField('e-mail', blank=True)
	## verbose_name='e-mail'
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class BookManager(models.Manager):
	def title_count(self, keyword):
		return(self.filter(title__icontains=keyword).count())
		
	def author_count(self, keyword):
		return(self.filter(authors__icontains=keyword).count())
		
class DahlBookManager(models.Manager):
	def get_query_set(self):
		return(super(DahlBookManager,self).get_query_set().filter \
		(authors='Roald Dahl'))
	
class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(blank=True, null=True)
	num_pages = models.IntegerField(blank=True, null=True)
	objects = BookManager()
	dahl_objects = DahlBookManager()
	
	def __unicode__(self):
		return self.title
		
class HorrorBook(Book):
	how_scary = models.CharField(max_length=20)
	
class TerrorBook(HorrorBook):
	test = models.CharField(max_length=10)
	
class Person(models.Model):
	name_f = models.CharField(max_length=20)
	name_l = models.CharField(max_length=20)
	sex = models.CharField(max_length=1)
	
	class Meta:
		abstract = True
		
class GhostWriter(Person):
	num_books = models.IntegerField(max_length=10)
	
