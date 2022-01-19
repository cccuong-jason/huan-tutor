import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

	STATUS = (
		(0, "Draft"), 
		(1, "Publish")
	)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(max_length=255, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	is_deleted = models.BooleanField(default=False)
	content = models.TextField()
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):

		return self.title
