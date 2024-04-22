from django.db import models

class Calculator(models.Model):
    principal_amount = models.FloatField()
    interest_rate = models.FloatField()
    time_period = models.FloatField()
