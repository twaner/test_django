from django.db import models
from booksite.books.models import Publisher


class Contact_Information(Publisher):
	publisher = models.ForeignKey(Publisher)
	email = models.CharField(max_length=30)
	phone = models.CharField(max_length=10)
