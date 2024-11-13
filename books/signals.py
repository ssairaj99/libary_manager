from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Book)
def log_book_saved(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    logger.info(f"Book '{instance.title}' was {action}.")

@receiver(post_delete, sender=Book)
def log_book_deleted(sender, instance, **kwargs):
    logger.info(f"Book '{instance.title}' was deleted.")
