from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save





class UserProfile(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField(max_length=8, default="1999-10-01")
    picture = models.ImageField(upload_to='imgs', blank=True)


    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
