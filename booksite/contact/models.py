from django.db import models
from books.models import Publisher


class Contact_Information(models.Model):
	contact = models.AutoField(primary_key=True)
	publisher = models.ForeignKey(Publisher, related_name='publisher_contact')
	email = models.CharField(max_length=30)
	phone = models.CharField(max_length=10)
