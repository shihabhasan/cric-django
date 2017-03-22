from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Cricketer(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    def get_runs(self):
        return self.runsbyyear_set.all().order_by('year').distinct().values('year', 'run')


class RunsByYear(models.Model):
    year = models.IntegerField()
    run = models.IntegerField()
    cricketer = models.ForeignKey(Cricketer, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.cricketer.name + ' scored ' + str(self.run) + ' runs in year' + str(self.year)