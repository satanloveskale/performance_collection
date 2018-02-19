from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from .utils import unique_slug_generator
from django.core.urlresolvers import reverse

# Create your models here.
class Name(models.Model):
    author = models.CharField(max_length=60,null=True, blank=True)
    def __str__(self):
        return self.author

class Subject(models.Model):
    term = models.CharField(max_length=60,null=True, blank=True)
    def __str__(self):
        return self.term

class Score(models.Model):
    score_title = models.CharField(max_length=120,null=True, blank=True)
    call_number = models.CharField(max_length=20, blank=True)
    collection = models.CharField(max_length=60,null=True, blank=True)
    author = models.ForeignKey('Name', on_delete=models.CASCADE,)
    arranger = models.CharField(max_length=120,null=True, blank=True)
    editor = models.CharField(max_length=120,null=True, blank=True)
    uniform_title = models.CharField(max_length=120,null=True, blank=True)
    publisher = models.CharField(max_length=120,null=True, blank=True)
    place_of_publication =  models.CharField(max_length=120,null=True, blank=True)
    date_of_publication =  models.CharField(max_length=120,null=True, blank=True)
    copyright_date =  models.CharField(max_length=120,null=True, blank=True)
    plate_number = models.CharField(max_length=120,null=True, blank=True)
    publisher_number = models.CharField(max_length=120,null=True, blank=True)
    series = models.CharField(max_length=20,null=True, blank=True)
    subject = models.ManyToManyField(Subject)
    collation = models.CharField(max_length=120,null=True, blank=True)
    holdings = models.CharField(max_length=120, null=True,blank=True)
    medium = models.CharField(max_length=120,null=True, blank=True)
    key_signature= models.CharField(max_length=20,null=True, blank=True)
    condition= models.CharField(max_length=20,null=True, blank=True)
    missing = models.CharField(max_length=20,null=True, blank=True)
    level = models.CharField(max_length=20,null=True, blank=True)
    contents = models.CharField(max_length=20,null=True, blank=True)
    cost= models.CharField(max_length=20,null=True, blank=True)
    cat_date = models.CharField(max_length=20,null=True, blank=True)
    cat_by= models.CharField(max_length=20,null=True, blank=True)
    acquisition_date= models.CharField(max_length=20,null=True, blank=True)
    notes = models.TextField(max_length=1000,null=True, blank=True, help_text="Enter a brief note")
    duration = models.CharField(max_length=20,null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    #objects = CopyManager()
    def get_absolute_url(self):
        return "/performance_collection/%s/" % self.slug


    def __str__(self):
        return self.score_title

    @property
    def title(self):
        return self.score_title

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
     if not instance.slug:
       instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Score)



