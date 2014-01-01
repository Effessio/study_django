# -*- coding: utf-8 -*-
from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/producer/{0}/'.format(self.id)


class Product(models.Model):
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    producer = models.ForeignKey(Producer)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return '{0} {1}'.format(self.sku, self.name)
