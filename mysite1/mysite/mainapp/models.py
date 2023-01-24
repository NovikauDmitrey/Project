from django.db import models


#Create your models here.
class Author(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)

class Contact(models.Model):

#    POST_TYPES = [('c', 'mar'), ('m', 'cc')]
    your_surname = models.CharField(max_length=100)
    your_name = models.CharField(max_length=100)
    your_secname = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    describe = models.CharField(max_length=1000)

def __str__(self):
    return self.email