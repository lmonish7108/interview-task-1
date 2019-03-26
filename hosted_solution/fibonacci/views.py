# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import time

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from fibonacci import models

def index(request):
	return render(request, "homepage.html")


def generateFibonacciSeries(nth_position):
	fib_series = []
	for i in range(int(nth_position)):
		if i < 2:
			fib_series.append(1)
		else:
			fib_series.append(fib_series[-1]+fib_series[-2])
	return str(fib_series[-1])


# Create your views here.
def getNthInstanceOfFibonacci(request):
	if request.POST:
		context = dict()
		start_time = time.time()
		nth_position = request.POST.get("position", '')

		try:
			position_value = models.FibonacciSeries.objects.get(instance_position=nth_position).instance_value
		except Exception as e:
			position_value = generateFibonacciSeries(nth_position)
			updated_record = models.FibonacciSeries.objects.create(instance_position=nth_position, 
																   instance_value=position_value)

		end_time = time.time()
		difference = end_time - start_time
		context.update({"nth_position": nth_position, 
						"position_value": position_value, 
						"time": difference})

		return render(request, "result_page.html", context)
	return HttpResponse("Its not a Post request.")


def get_latest_searches(request):
	searches = models.FibonacciSeries.objects.all()[:5]
	return HttpResponse(serializers.serialize('json', list(searches), fields=('instance_position', 'instance_value')), content_type='application/json')

