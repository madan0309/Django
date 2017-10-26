from django.contrib import admin

# Register your models here.
from blog import models
from .models import Post, Author, Category, Tag, Feedback

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject', 'date',)
	search_fields = ('name', 'email',)
	date_hierarchy = 'date'

admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.Author)
admin.site.register(models.Tag)
admin.site.register(Feedback, FeedbackAdmin)
