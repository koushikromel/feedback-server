from django.db import models

# Create your models here.

class Feedback(models.Model):
  R = models.FloatField(default=0.0)
  Y = models.FloatField(default=0.0)
  B = models.FloatField(default=0.0)
  U = models.FloatField(default=0.0)
  RC = models.FloatField(default=0.0)
  YC = models.FloatField(default=0.0)
  BC = models.FloatField(default=0.0)
  UC = models.FloatField(default=0.0)
  UB = models.FloatField(default=0.0)

  class Meta:
    ordering = ["id"]
