from django.db import models
from django.contrib.auth.models import User
from blocks.models import Blocks

# Create your models here.
class Articles(models.Model):
    owner = models.ForeignKey(User,verbose_name="作者")
    title = models.CharField("文章标题",max_length=100)
    author = models.CharField("文章作者",max_length=100)
    content = models.TextField("文章内容",max_length=10000)
    block = models.ForeignKey(Blocks,verbose_name="所属板块")

    create_time_stamp = models.DateTimeField("创建时间",auto_now_add=True)
    last_update_timestamp = models.DateTimeField("最后更新时间",auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
