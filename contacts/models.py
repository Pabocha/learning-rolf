from django.db import models

# Create your models here.

class Contacts(models.Model):

    nom = models.CharField(max_length=255)
    sujet = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom
    
class NewsLetters(models.Model):
    
    email = models.EmailField()

    class Meta:
        verbose_name = "News Letter"
        verbose_name_plural = "News Letters"
    
    def __str__(self):
        return self.email