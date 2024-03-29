# Generated by Django 4.1.2 on 2023-01-17 08:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0025_alter_conference_random_id_alter_ewaevent_random_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='random_id',
            field=models.CharField(default=uuid.UUID('ea10ef39-0bbe-4a26-92fa-8b343aa400ab'), max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='ewaevent',
            name='random_id',
            field=models.CharField(default=uuid.UUID('ea10ef39-0bbe-4a26-92fa-8b343aa400ab'), max_length=200, unique=True),
        ),
    ]
