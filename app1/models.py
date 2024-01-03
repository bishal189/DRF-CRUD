from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=300)  
  created_at=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
