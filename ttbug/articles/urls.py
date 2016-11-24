from django.conf.urls import url
from .views import articles_list, article_detail,article_create

urlpatterns = [
        url(r"^list/(?P<block_id>\d+)",articles_list),
        url(r"^detail/(?P<article_id>\d+)",article_detail),
        url(r"^create/(?P<block_id>\d+)",article_create),
        ]
