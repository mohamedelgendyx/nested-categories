from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.TextField()
  parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

  class Meta:
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name