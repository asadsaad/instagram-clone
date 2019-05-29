from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


# Create your models here.
class Post(models.Model):
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    creat_at=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name='likes',blank=True)
    view_count=models.IntegerField(default=0)
    img=models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post_app:details',args=[self.pk])

    def total_likes(self):
    	return self.like.count()

    def increase(self):
    	self.view_count+=1
    	self.save()

class Comments(models.Model):
	comment_content=models.TextField()
	c_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="c_ed")
	reply=models.ForeignKey("Comments",blank=True,null=True,related_name="replies",on_delete=models.CASCADE,)
	post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='blabla')
	created_on=models.DateTimeField(auto_now_add=True)
		
	def __str__(self):
		return self.post.content