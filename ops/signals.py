from django.db.models.signals import post_save
from .models import VehicleProfile, Vehicle
from django.dispatch import receiver


@receiver(post_save, sender=Vehicle)
def create_profile(sender, instance, created, **kwargs):
    if created:
        VehicleProfile.objects.create(car=instance)


@receiver(post_save, sender=Vehicle)
def save_profile(sender, instance, **kwargs):
    # instance.Vehic.save()
    pass
