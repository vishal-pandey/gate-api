from django.db import models

# Create your models here.

class Visitor(models.Model):
	id = models.AutoField(primary_key=True)
	visit_date = models.DateField(auto_now_add=True)
	card_number = models.TextField()
	name = models.TextField()
	address = models.TextField()
	mobile = models.TextField()
	number_plate = models.TextField()
	destination = models.TextField()
	purpose = models.TextField()
	intime = models.DateTimeField(auto_now_add=False)
	outtime = models.DateTimeField(auto_now_add=False)





