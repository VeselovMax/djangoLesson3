from django.db import models

class Counter(models.Model):
    count = models.IntegerField(default=0)
    class Meta:
        app_label = 'myproject'