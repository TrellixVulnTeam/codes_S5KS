# models.py
# -*- coding: utf-8 -*-

from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)

# 加入更复杂的模型
class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

# 加入更复杂的模型
class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name