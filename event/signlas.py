from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import EwaEvent, Conference
from .views import send_mail
from django.template.loader import render_to_string


@receiver(pre_save, sender=Conference)
@receiver(pre_save, sender=EwaEvent)
def link_generator(sender, instance, *args, **kwargs):
    if instance.id and instance.status and not instance.email_sent:
        instance.email_sent = True
        template_path = 'mail/registration_link_confimration.html'
        template = render_to_string(
            template_path, {'event_name': instance.event_name})
        send_mail(instance.email, template)
        if sender == EwaEvent:
            instance.registration_link = 'http://127.0.0.1:8000/ewa/register/' + \
                str(instance.random_id) + '/'
        else:
            instance.registration_link = 'http://127.0.0.1:8000/conference/register/' + \
                str(instance.random_id) + '/'
