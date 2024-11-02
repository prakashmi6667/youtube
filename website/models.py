from django.db import models
from django.utils.timezone import datetime
# Create your models here.
class Channel(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    logo = models.ImageField(upload_to="logo/")
    total_subscription = models.IntegerField(default=0)

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    # created_on = models.DateField(default=datetime.now, editable=False, null=True, blank=True)
   

    class Meta:
        verbose_name_plural = "Channel"
        verbose_name = "Channel"

    def __str__(self):
        return self.name
class Videos(models.Model):

    objects = models.Manager()
    
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE, limit_choices_to={"is_active":True})
    title = models.CharField(max_length=250)    
    thumbnail = models.ImageField(upload_to="videoThumbnail/")
    video = models.CharField(max_length=250, null=True, blank=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
   

    class Meta:
        verbose_name_plural = "video"
        verbose_name = "video"

    def __str__(self):
        return self.title


class Comments(models.Model):

    objects = models.Manager()
    
    video = models.ForeignKey(Videos, on_delete=models.CASCADE, limit_choices_to={"is_active":True})
    comments = models.TextField(null=True, blank=True)    
    

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
   
    
    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comments"

  