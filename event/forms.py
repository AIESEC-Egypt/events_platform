from django import forms
from django import forms
from .models import EwaEvent, Conference, EwaDelegate, NationalConferenceDelegate, LocalConferenceDelegate


class EwaEventForm(forms.ModelForm):
    class Meta:
        model = EwaEvent
        exclude = ('status', 'email_sent', 'registration_link',
                   'random_id', 'deadline')


class EwaDelegateForm(forms.ModelForm):
    class Meta:
        model = EwaDelegate
        exclude = ('event', 'time_stamp')


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        exclude = ('status', 'email_sent', 'registration_link',
                   'random_id', 'deadline')


class NationalConferenceDelegateForm(forms.ModelForm):
    class Meta:
        model = NationalConferenceDelegate
        exclude = ('event', 'time_stamp')


class LocalConferenceDelegateForm(forms.ModelForm):
    class Meta:
        model = LocalConferenceDelegate
        exclude = ('event', 'time_stamp', 'lc')
