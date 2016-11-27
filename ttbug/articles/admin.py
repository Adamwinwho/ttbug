from django.contrib import admin
from .models import Articles
from pagedown.widgets import AdminPagedownWidget
from django import forms
# Register your models here.

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Articles
        fields = "__all__"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","last_update_timestamp")
    form = ArticleForm

admin.site.register(Articles,ArticleAdmin)

