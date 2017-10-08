from __future__ import unicode_literals
import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class Item(models.Model):
    title = models.CharField(max_length=140)
    created_date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=None)
    completed_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=40)
    priority = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo-task_detail', kwargs={'task_id': self.id, })
    
    def save(self):
        if self.completed:
            self.completed_date = datetime.datetime.now()
        super(Item, self).save()

    class Meta:
        ordering = ["priority"]
