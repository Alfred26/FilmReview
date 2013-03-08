from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    last_login = models.DateField(blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
