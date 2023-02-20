from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

"""
User extra data(contacts) i am using english name variables
and on verbose name i am using Portuguese
First Name, Last Name and e-mail are included on User Model
The funds field is the monetary is the value that user has
put on the app
"""
class Profile(models.Model):
    user     = models.OneToOneField(User, null=False, blank=False, verbose_name="Utilizador", 
                                on_delete=models.CASCADE)
    address  = models.CharField(max_length=150, null=True, blank=True, 
                                verbose_name="Morada")
    zip_code = models.CharField(max_length=12, null=True, blank=True, 
                                verbose_name="Código Postal")
    location = models.CharField(max_length=120, null=True, blank=True, 
                                verbose_name="Localização")
    phone    = models.IntegerField(null=True, blank=True, 
                                   verbose_name="Número de contato")
    funds    = models.FloatField(null=True, blank=True, verbose_name="Fundos")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'Perfil'
        verbose_name_plural = 'Perfis' 


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

"""
Bike models, here we have the values of the electric bikes,
like serial numbers, date that was bought, status of bike
"""
class Bike(models.Model):
    serie_number = models.CharField(max_length=500, null=False, blank=False, 
                                   verbose_name="Número de série")
    date_bought  = models.DateField(null=False, blank=False, 
                                    verbose_name="Data de Compra")
    status       = models.CharField(max_length=100, null=False, blank=False, 
                                    verbose_name="Estado")
    notes        = models.TextField(null=True, blank=True, verbose_name="Notas")

    class Meta:
        verbose_name        = 'Bicicleta'
        verbose_name_plural = 'Bicicletas' 

class UnlockPackage():
    name  = models.CharField(max_length=100, null=False, verbose_name="Nome")
    hours = models.FloatField(null=False, blank=False, verbose_name="Horas")
    price = models.FloatField(null=False, blank=False, verbose_name="Preço")

    class Meta:
        verbose_name        = 'Pacote'
        verbose_name_plural = 'Pacotes'
    





