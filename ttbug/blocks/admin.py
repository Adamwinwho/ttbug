from django.contrib import admin
from .models import Blocks

# Register your models here.
class BlockAdmin(admin.ModelAdmin):
    list_display = ("name","owner","describe","create_time_stamp")

    
admin.site.register(Blocks,BlockAdmin)
