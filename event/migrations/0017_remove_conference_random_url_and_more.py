# Generated by Django 4.1.2 on 2023-01-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0016_remove_conference_registration_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='random_url',
        ),
        migrations.RemoveField(
            model_name='ewaevent',
            name='random_url',
        ),
        migrations.AddField(
            model_name='conference',
            name='registration_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ewaevent',
            name='registration_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
