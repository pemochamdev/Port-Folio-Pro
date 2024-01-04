from django.db import models
import string
from random import choice
from io import BytesIO
from time import strftime
import sys

from PIL import Image
from django.urls import reverse_lazy 
from django.utils.text import slugify
from django.templatetags.static import static
from django.utils.timezone import  now
from django.db.models.signals import post_delete
from django.core.files.uploadedfile import InMemoryUploadedFile

from core.signals import file_cleanup


# Create your models here.
def generate_file_name(length=30):
    letters = string.ascii_letters + string.digits
    return ''.join(choice(letters) for _ in range(length))


def project_directory_path(instance, filename):
    return 'projects/{0}/{1}'.format(strftime('%Y/%m/%d'), generate_file_name() + '.' + filename.split('.')[-1])






# About Model
class About(models.Model):
    key = models.CharField(max_length=100, primary_key = True)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    

    class Meta:
      
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'
    
    def __str__(self):
        return self.key


# Service Model
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Service name')
    description = models.TextField()
    image = models.ImageField(upload_to="services", default='default.png')


    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name




class Experience(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="experiences", default='default.png')
    from_date = models.DateField()
    to_date = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.position, self.company)



class ProjectCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Project(models.Model):
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, null=True)
    image = models.ImageField(upload_to=project_directory_path, default="default.png")
    link = models.CharField(max_length=255, null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    current = models.BooleanField(default=False)
    # description = HTMLField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        

        # Opening the uploaded image
        im = Image.open(self.image)

        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((550, 370))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the image field value to be the newly modified image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Project, self).save()

post_delete.connect(file_cleanup, sender=Project)



class Skill(models.Model):
    title = models.CharField(max_length=50)
    rate = models.IntegerField()

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.school


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name


def blog_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(strftime('%Y/%m/%d'), generate_file_name(25) + '.' + filename.split('.')[-1])


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to=blog_directory_path, null=True, blank=True)
    created_at = models.DateField(default=now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Blog, self).save()

    @property
    def photo(self):
        if self.image:
            return self.image.url
        else:
            return static("images/blog_default.jpg")

    def get_absolute_url(self):
        return reverse_lazy('core:blog-details', self.slug)


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
    

    
