from django.db import models

class Friend_users(models.Model):
    first_name=models.CharField('first Name',max_length=30)
    last_name=models.CharField('last Name',max_length=20)
    birthdate=models.DateTimeField('Brithday')
    gender=models.CharField('Gender',max_length=6,blank=True)
    emailid=models.EmailField('Email address',blank=True)
    phone=models.CharField('Phone Number',max_length=120)
    address=models.CharField('Address',max_length=120,blank=True)
    pincode=models.CharField('pincode',max_length=6,blank=True)

    def __str__(self):
        return self.first_name


