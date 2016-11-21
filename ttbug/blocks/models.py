from django.db import models

# Create your models here.

class Blocks(models.Model):
    name = models.CharField("板块名称",max_length=100)
    owner = models.CharField("板块管理员",max_length=100)
    describe = models.CharField("板块描述",max_length=300)

    create_time_stamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)
