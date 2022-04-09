from django.db import models
from django.shortcuts import reverse
class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published')
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES,max_length=1,default='p')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified =models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view',args=[self.id])
