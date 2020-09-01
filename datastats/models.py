import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Dataset(models.Model):
    file_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    load_date = models.DateTimeField('date loaded')
    
    def __str__(self):
        return self.file_name
        
    def was_uploaded_recently(self):
        return self.load_date >= timezone.now() - datetime.timedelta(days=1)
    
class Column(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=200, verbose_name="Column Name")
    column_type = models.CharField(max_length=200, verbose_name="Column Type")
    num_blank = models.IntegerField(verbose_name="Number Blank Values")
    num_unique = models.IntegerField(verbose_name="Number Unique Values")
    variability = models.FloatField(verbose_name="Variability Index")
    num_count = models.IntegerField(verbose_name="Number of Values (Numeric)", default=None, null=True)
    num_max = models.FloatField(verbose_name="Max Value", default=None, blank=True, null=True)
    num_min = models.FloatField(verbose_name="Min Value", default=None, blank=True, null=True)
    num_mean = models.FloatField(verbose_name="Avg Value", default=None, blank=True, null=True)
    num_std = models.FloatField(verbose_name="Std Deviation", default=None, blank=True, null=True)
    pct_25 = models.FloatField(verbose_name="25th Percentile", default=None, blank=True, null=True)
    pct_50 = models.FloatField(verbose_name="50th Percentile", default=None, blank=True, null=True)
    pct_75 = models.FloatField(verbose_name="75th Percentile", default=None, blank=True, null=True)
    
    def __str__(self):
        return self.column_name