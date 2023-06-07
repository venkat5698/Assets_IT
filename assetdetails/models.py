# from django.db import models

# Create your models here.
from django.db import models

class AssetDetails(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    asset_id = models.CharField(max_length=100)
    system_type = models.CharField(max_length=10)
    designation = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    imei_number = models.CharField(max_length=20)
    dongle_number = models.CharField(max_length=20)
    date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    filename = models.FileField(upload_to='uploads/')