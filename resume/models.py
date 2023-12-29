from django.db import models



class resume_Table(models.Model):
    name = models.CharField(max_length=100)
    dob= models.DateField()
    gender= models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='documents/',blank=True)
    my_file = models.FileField(upload_to='documents/',blank=True)
