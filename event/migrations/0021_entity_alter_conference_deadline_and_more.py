# Generated by Django 4.1.2 on 2023-01-15 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0020_conference_deadline_ewaevent_deadline_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expa_id', models.IntegerField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.entity')),
            ],
        ),
        migrations.AlterField(
            model_name='conference',
            name='deadline',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='random_id',
            field=models.CharField(default=uuid.UUID('a60bdeaf-d449-4b43-875e-2c72024c05d2'), max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='ewaevent',
            name='deadline',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='ewaevent',
            name='random_id',
            field=models.CharField(default=uuid.UUID('a60bdeaf-d449-4b43-875e-2c72024c05d2'), max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expa_id', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('full_name', models.CharField(max_length=250)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('instagram', models.CharField(blank=True, max_length=500, null=True)),
                ('applications_count', models.IntegerField(default=0)),
                ('joined_at', models.DateField(blank=True, null=True)),
                ('access', models.CharField(blank=True, max_length=400, null=True)),
                ('is_icx', models.BooleanField(default=False)),
                ('is_ogx', models.BooleanField(default=False)),
                ('host_lc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.entity')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
