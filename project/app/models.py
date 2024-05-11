from django.db import models

# Create your models here.

class Student(models.Model):
    Firstname=models.CharField(max_length=250)
    Lastname=models.CharField(max_length=250)
    Email=models.EmailField()
    City=models.CharField(max_length=250)
    Contact=models.IntegerField()

    class Meta():
        db_table='Student'
        verbose_name_plural='Student'

    def __str__(self):
        return self.Email


