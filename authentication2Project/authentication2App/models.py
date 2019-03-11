from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPosts(models.Model):
	# KEY: Should probably use CASCADE delete option so bloggers posts get deleted if blogger deleted
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    blog_title = models.CharField(max_length=100)
    blog_entry = models.CharField(max_length=500)

