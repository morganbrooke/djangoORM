from django.db import models
class Interest(models.Model):
	interest_name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = 'interests'
class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	occupation = models.CharField(max_length=50)
	interest = models.ForeignKey(Interest)
	class Meta:
		db_table = 'users'