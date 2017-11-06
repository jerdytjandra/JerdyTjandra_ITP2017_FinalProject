from django.db import models

class Pet(models.Model):
	pet_type = models.CharField(max_length=50)
	price = models.IntegerField()

	def __str__(self):
		return str(self.pet_type)

class Cart(models.Model):
	userid = models.ForeignKey('auth.User')
	productid = models.ForeignKey('Pet', null = True)

	def __str__(self):
		return str(self.userid) + ' ' + str(self.productid)