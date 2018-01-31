# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=200)
    flag_path = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Sport(models.Model):
    name = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    name =  models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    sports = models.ManyToManyField(Sport)
    age = models.IntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)