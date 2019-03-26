# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FibonacciSeries(models.Model):
	instance_position = models.TextField()
	instance_value = models.TextField()

	def __unicode__(self):
		return self.instance_position