from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_date = models.TextField()
    last_modified_date = models.TextField()