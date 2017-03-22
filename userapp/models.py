from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Cricketer(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class RunsByYear(models.Model):
    year = models.IntegerField()
    run = models.IntegerField()
    cricketer = models.ForeignKey(Cricketer, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.cricketer.name + ' scored ' + str(self.run) + ' runs in year' + str(self.year)