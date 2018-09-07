from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Attack_Node(models.Model):
	name = models.CharField(max_length=40, primary_key=True)
	desc = desc = models.CharField(max_length=500, default=True)

	def __str__(self):
		return self.name

class Defense_Node(models.Model):

	name = models.CharField(max_length=40)
	desc = models.CharField(max_length=500)
	date_added = models.DateTimeField(default=timezone.now, blank=True)
	parent = models.ForeignKey(Attack_Node, on_delete=models.CASCADE, default=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-date_added']

class Comment(models.Model):

	text = models.CharField(max_length=3000)
	pub_date = models.DateTimeField(default=datetime.now, blank=True)
	parent = models.ForeignKey(Defense_Node, on_delete=models.CASCADE, default=True)

	def __str__(self):
		return self.text

