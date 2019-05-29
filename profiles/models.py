from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	profile_img=models.ImageField(null=True,blank=True,default="default.png")
	cover_img=models.ImageField(null=True,blank=True,)
	location=models.CharField(null=True,blank=True,max_length=100)
	education=models.CharField(null=True,blank=True,max_length=100)
	work_at=models.CharField(null=True,blank=True,max_length=100)
	bio=models.CharField(null=True,blank=True,max_length=50)
	following=models.ManyToManyField(User,blank=True,related_name='followed_by')


	def __str__(self):
		return self.user.username

	def get_following(self):
		users=self.following.all()
		return users.exclude(username=self.user.username)

	def get_absolute_url(self):
		return reverse('profilies:profile',args=[self.user.username])	

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)