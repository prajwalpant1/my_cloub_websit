from multiprocessing import managers
from site import venv
from django.db import models
class Venue(models.Model):
    name = models.CharField('Venue Name',max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    web=models.URLField(max_length=200)
    def __str__(self):
        return self.name
class MyclubUser(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name + ' ' + self.last_name
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    venv=models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    # venue = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField('Event Date')
    manager=models.CharField(max_length=60)
    attendies=models.ManyToManyField(MyclubUser,blank=True)


    def __str__(self):
        return self.name