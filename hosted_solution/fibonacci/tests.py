# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from fibonacci import models
from fibonacci import views


# Create your tests here.
class ModelCreationTestCase(TestCase):
    def setUp(self):
        models.FibonacciSeries.objects.create(instance_position="3", instance_value="2")

    def test_record_is_created(self):
    	create_test = models.FibonacciSeries.objects.get(instance_position="3")
    	self.assertEqual(create_test.instance_position, "3")
    	self.assertEqual(create_test.instance_value, "2")


class FibonacciSeriesGenerationTestCase(TestCase):

	def test_series_generation(self):
		self.assertEqual("8", views.generateFibonacciSeries("6"))
		self.assertEqual("2", views.generateFibonacciSeries("3"))
