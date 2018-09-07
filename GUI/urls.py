
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^add-node', views.add_node, name="add_node"),
	url(r'^add-comment/(?P<id>[0-9]+)$', views.add_comment, name='add_comment'),
	url(r'^download-comments', views.download_comments, name='download_comments'),
]