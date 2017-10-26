from django.db import models
#from django.conf.urls import reverse
#from dj7angoango.urls import reverse
# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	active = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)
	last_logged_in = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name + " : " +self.email

class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	author = models.ForeignKey(Author)
	def __str__(self):
		return self.name
	
		
class Tag(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	author = models.ForeignKey(Author)
	def __str__(self):
		return self.name
	
class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Author)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag)
	def __str__(self):
		return self.title

class Feedback(models.Model):
	name = models.CharField(max_length=200, help_text="Name of the sender")
	email = models.EmailField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Feedback"
		
	def __str__(self):
		return self.name+ "-" + self.email

class MyFeedback(models.Model):
	name = models.CharField(max_length=200, help_text="Name of the sender")
	email = models.EmailField(max_length=200)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Feedback"
	def __str__(self):
		return self.name + "--" + self.email