from django.db import models
from django.forms import DateField, FileField, IntegerField
from django.contrib.auth.models import User
from django.utils import timezone
from .choices import *
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class ConferenceType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class AIESECer(models.Model):
    AIESECer = models.BooleanField()

    def __str__(self):
        return self.AIESECer


class LocalCommittee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# abstract class for events


class Event(models.Model):
    lc_name = models.CharField(max_length=50, choices=LC)
    lc_representative = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    event_name = models.CharField(max_length=50, unique=True)
    date = models.DateField(
        help_text="Please use the following format: YYYY-MM-DD")
    price = models.IntegerField()
    delegates_number = models.IntegerField()
    status = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)
    registration_link = models.CharField(max_length=200, null=True, blank=True)
    random_id = models.CharField(
        max_length=200, default=uuid.uuid4(), unique=True)
    deadline = models.DateTimeField(
        default=timezone.now, null=True, blank=True)

    class Meta:
        abstract = True


class EwaEvent(Event):
    def __str__(self):
        return self.event_name + '_' + self.lc_name


class Conference(Event):
    conference_type = models.ForeignKey(
        ConferenceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name + '_' + self.lc_name


# delegates
class Delegate(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    cv = models.FileField(null=True, blank=True)
    indemnity_form = models.FileField(null=True)
    id_front = models.ImageField(null=True)
    id_back = models.ImageField(null=True)
    time_stamp = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class EwaDelegate(Delegate):
    event = models.ForeignKey(EwaEvent, on_delete=models.CASCADE, null=True)
    aiesecer = models.ForeignKey(AIESECer, on_delete=models.CASCADE)
    lc = models.ForeignKey(LocalCommittee, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, null=True,
                            blank=True, choices=NATIONAL_ROLE)
    function = models.CharField(
        max_length=50, null=True, blank=True, choices=NATIONAL_FUNCTION)

    def __str__(self):
        return self.name


class NationalConferenceDelegate(Delegate):
    event = models.ForeignKey(Conference, on_delete=models.CASCADE, null=True)
    lc = models.CharField(max_length=50, null=True,
                          blank=True, choices=LC, verbose_name='LC')
    role = models.CharField(max_length=50, null=True,
                            blank=True, choices=NATIONAL_ROLE)
    function = models.CharField(
        max_length=50, null=True, blank=True, choices=NATIONAL_FUNCTION)

    def __str__(self):
        return self.name


class LocalConferenceDelegate(Delegate):
    event = models.ForeignKey(Conference, on_delete=models.CASCADE, null=True)
    lc = models.CharField(max_length=50, null=True,
                          blank=True, choices=LC, verbose_name='LC')
    role = models.CharField(max_length=50, null=True,
                            blank=True, choices=LOCAL_ROLE)
    function = models.CharField(
        max_length=50, null=True, blank=True, choices=LOCAL_FUNCTION)

    def __str__(self):
        return self.name


# User

class Entity(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
    expa_id = models.IntegerField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expa_id = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100)
    home_lc = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)
    applications_count = models.IntegerField(default=0)
    joined_at = models.DateField(null=True, blank=True)
    access = models.CharField(max_length=400, null=True, blank=True)
    is_icx = models.BooleanField(default=False)
    is_ogx = models.BooleanField(default=False)
    role = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.full_name
