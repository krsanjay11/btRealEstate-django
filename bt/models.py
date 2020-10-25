from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=False)
    city = models.CharField(max_length=50)
    date = models.DateField()
    phone = models.CharField(max_length=15,blank=False)
    email = models.CharField(max_length=50,blank=False)
    time = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name


class Register(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20, default="")
    username = models.CharField(max_length=50)
    date = models.DateField()
    phone = models.CharField(max_length=15,blank=False)
    email = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fname

class inquiry(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    property = models.CharField(max_length=50, default="")
    date = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
