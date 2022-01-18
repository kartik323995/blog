from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class post(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add = True)   
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk}) 

class profile(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile')
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):    
        super().save()
        i = Image.open(self.image.path)
        if i.height > 300 or i.width > 300:
            i.thumbnail((300,300))
            i.save(self.image.path)
