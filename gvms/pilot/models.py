from django.db import models
import hashlib

class Profile(models.Model):
	@classmethod
	def mkpasswd(self, password, salt):
		m = hashlib.md5()
		m.update(password + salt)
		return str(m.hexdigest())

	userid     = models.IntegerField()
	first_name = models.CharField(max_length=30)
	last_name  = models.CharField(max_length=30)
	email      = models.EmailField(max_length=245)
	password   = models.CharField(max_length=32)
	hours      = models.FloatField()
	transfer_hours = models.FloatField()
	ip_address = models.CharField(max_length=100)
	salt       = models.CharField(max_length=30)