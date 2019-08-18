from django.db import models
from django.conf import settings
# Create your models here.



class News(models.Model):
    CHOICES =(("0","Poltics"),("1","Sports"),("2","Entertainment"),("3","International"))
    title= models.CharField(max_length=255)
    article = models.TextField()
    count = models.IntegerField(default=0)
    category =models.CharField(choices=CHOICES, max_length=2)
    cover_image= models.ImageField(upload_to='uploads',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,related_name='newses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ='News'


class Feedback(models.Model):
    commentator=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)       