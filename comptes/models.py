from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class Utilisateurs(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',  # Exemple : +33612345678
        message="Le numéro de téléphone doit être au format '+221612345678'."
    )

   
    telephone = models.CharField(validators=[phone_regex], max_length=17, blank=True, error_messages={
                             'required': 'Ce champ est obligatoire.', 'invalid': 'Votre numéro de téléphone ne doit pas contenir des espaces.'})
