from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Mydata(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    body = models.TextField(max_length=140, blank=True)
    title = models.CharField(max_length=50, blank=True)
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name