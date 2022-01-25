from django.utils import timezone
from django.db import models


class Category(models.Model): 
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name

class TodoList(models.Model):
    title = models.CharField(max_length=250) 
    content = models.TextField(blank=True) 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"),blank=True, null=True) 
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"),blank=True, null=True) 
    category = models.ForeignKey(Category, default="general",on_delete=models.PROTECT) 
    status=models.CharField(max_length=250,default='complete')
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #set name