from django.db import models

# Create your models here.

class Modules(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"
    
    def __str__(self):
        return self.titre

class Formations(models.Model):

    titre = models.CharField(max_length=255)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    duree = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Formation')
        verbose_name_plural = ('Formations')

    def __str__(self):
        return self.titre
    

    

