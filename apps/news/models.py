from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.



class News(models.Model):
    CHOICES =(("0","Poltics"),("1","Sports"),("2","Entertainment"),("3","International"))
    title= models.CharField(max_length=255)
    article = models.TextField()
    count = models.IntegerField(default=0)
    category =models.CharField(choices=CHOICES, max_length=2)
    cover_image= models.ImageField(upload_to='uploads',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,related_name='newses')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("detail_news", kwargs={"pk": self.pk})

    def get_api_like_url(self):
        return reverse("like-api-toggle", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name_plural ='News'


class Feedback(models.Model):
    commentator=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,related_name='commented_by')
    news = models.ForeignKey(News, on_delete=models.CASCADE ,related_name='comments')
    comment =models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Favorite(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE ,related_name='favourite_news')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,related_name='added_by')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.news



       