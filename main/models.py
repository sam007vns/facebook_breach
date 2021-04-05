from django.db import models

class facebook_data(models.Model):
	mobile_no=models.CharField(max_length=12)
	registration=models.CharField(max_length=15)
	info=models.TextField()
	def __str__(self):
		return self.info
class user_matched(models.Model):
	mobile_no=models.CharField(max_length=12)
	registration=models.CharField(max_length=15)
	info=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.user.mobile_no)
class user_not_matched(models.Model):
	phone=models.CharField(max_length=12)
	date_added=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.mobile_no

# Create your models here.
