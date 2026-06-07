from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel

@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    print("Signal Executed")
    raise Exception("Signal Exception")