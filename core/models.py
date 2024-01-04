from django.db import models

# Create your models here.


# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about')

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    

    class Meta:
      
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'
    
    def __str__(self):
        return "About Me"


# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Service name')
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="work")

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title


# Client Model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name = "Client Say")
    image = models.ImageField(upload_to="clients", default="default.png")

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name
    

    
