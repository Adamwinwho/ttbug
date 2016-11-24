from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","last_update_timestamp")

admin.site.register(Articles,ArticleAdmin)
