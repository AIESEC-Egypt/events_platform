from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import is_valid_path
from event.models import EwaEvent, Conference
from .forms import EwaEventForm, ConferenceForm, EwaDelegateForm, NationalConferenceDelegateForm, LocalConferenceDelegateForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.utils import timezone
# Create your views here


def send_mail(reciever_email, template):

    email = EmailMessage(
        'Event Request',
        template,
        settings.EMAIL_HOST_USER,
        [reciever_email],
    )
    email.fail_silently = False
    email.send()


def pre_registration_save(instance, event, event_type):
    instance.event = event
    if event_type == 'conference' and event.conference_type == 'Local':
        instance.lc = event.lc_name
    instance.id_front.field.upload_to = slugify(
        event.lc_name) + '/' + slugify(event.event_name) + '/' + slugify(instance.name)
    instance.id_back.field.upload_to = slugify(
        event.lc_name) + '/' + slugify(event.event_name) + '/' + slugify(instance.name)
    instance.cv.field.upload_to = slugify(
        event.lc_name) + '/' + slugify(event.event_name) + '/' + slugify(instance.name)
    instance.indemnity_form.field.upload_to = slugify(
        event.lc_name) + '/' + slugify(event.event_name) + '/' + slugify(instance.name)


def ewa(request):
    if request.method == 'POST':
        form = EwaEventForm(request.POST)
        if form.is_valid():
            form.save()
            template_path = 'mail/ewa_request_mail.html'
            template = render_to_string(template_path, {
                                        'lc_representative': request.POST['lc_representative'], 'lc': request.POST['lc_name']})
            mc_responsible = 'omar.rwiheb2@aiesec.net'
            send_mail(mc_responsible, template)
        return HttpResponse('form is submitted')
    else:
        form = EwaEventForm()
        return render(request, 'forms/ewa.html', {'form': form})


def conference(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            template_path = 'mail/conference_request_mail.html'
            template = render_to_string(template_path, {
                                        'lc_representative': request.POST['lc_representative'], 'lc': request.POST['lc_name']})
            mc_responsible = 'omar.rwiheb2@aiesec.net'
            send_mail(mc_responsible, template)
            return HttpResponse('form is submitted')
        return HttpResponse(str(form.errors.as_json()))
    else:
        form = ConferenceForm()
        return render(request, 'forms/conference.html', {'form': form})


def ewa_delegate(request, random_id):
    event = get_object_or_404(EwaEvent, random_id=random_id)
    new_delegate = None
    if request.method == 'POST':
        delegate_form = EwaDelegateForm(request.POST, request.FILES)
        if delegate_form.is_valid():
            new_delegate = delegate_form.save(commit=False)
            pre_registration_save(new_delegate, event, 'ewa')
            new_delegate.save()
            return HttpResponse('form is submitted and data is valid')
        return HttpResponse('form is submitted and data is not valid')
    else:
        delegate_form = EwaDelegateForm()

    if event.deadline < timezone.now():
        return HttpResponse('you missed the deadline')

    return render(request, 'forms/delegate.html', {'form': delegate_form})


def conference_delegate(request, random_id):
    event = get_object_or_404(Conference, random_id=random_id)
    print(event.event_name)
    new_delegate = None
    if request.method == 'POST':
        delegate_form = None
        if event.conference_type == "National":
            delegate_form = NationalConferenceDelegateForm(
                request.POST, request.FILES)
        else:
            delegate_form = LocalConferenceDelegateForm(
                request.POST, request.FILES)
        if delegate_form.is_valid():
            new_delegate = delegate_form.save(commit=False)
            pre_registration_save(new_delegate, event, 'conference')
            new_delegate.save()
            return HttpResponse('form is submitted and data is valid')
        return HttpResponse('form is submitted and data is not valid')
    else:
        if event.conference_type == "National":
            delegate_form = NationalConferenceDelegateForm()
        else:
            delegate_form = LocalConferenceDelegateForm()

    if event.deadline < timezone.now():
        return HttpResponse('you missed the deadline')

    return render(request, 'forms/delegate.html', {'form': delegate_form})


def past_events(request):
    x = {'myevents': Conference.objects.filter()}
    return render(request, 'past_events.html', x)


def main(request):
    return render(request, 'index.html')
