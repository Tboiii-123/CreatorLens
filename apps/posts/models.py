from decouple import config
from django.db import models
from apps.account.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")

    title = models.CharField(max_length=255)
    content = models.TextField()

    views = models.PositiveBigIntegerField(default=0)  # optional fallback
    
    image = CloudinaryField('image', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




      

