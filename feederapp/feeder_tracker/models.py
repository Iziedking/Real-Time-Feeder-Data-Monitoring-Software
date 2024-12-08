from django.db import models

class Feeder(models.Model):
  feeder_33 = models.CharField(max_length=100, unique=True)
  ia = models.FloatField(default=0)
  ia = models.FloatField(default=0)
  ia = models.FloatField(default=0)
  ia = models.FloatField(default=0)
  ia = models.FloatField(default=0)
  ia = models.FloatField(default=0)
  ia = models.FloatField(default=0)
  ia = models.FloatField(default=0)

  def __string__(self):
    return self.feeder_33
