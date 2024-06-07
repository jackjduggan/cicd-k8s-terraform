from django.db import models

class Project(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    start_date  = models.DateField()
    end_date    = models.DateField(null=True, blank=True) # project may not be finished

    def __str__(self):
        return self.name