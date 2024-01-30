# Generated by Django 4.1.2 on 2022-12-11 19:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_conference_email_ewaevent_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalConferenceDelegate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cv', models.FileField(blank=True, null=True, upload_to='')),
                ('indemnity_form', models.FileField(null=True, upload_to='')),
                ('id_front', models.ImageField(null=True, upload_to='')),
                ('id_back', models.ImageField(null=True, upload_to='')),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('role', models.CharField(blank=True, choices=[('MM', 'MM'), ('Member', 'Member'), ('Newbie', 'Newbie')], max_length=50, null=True)),
                ('function', models.CharField(blank=True, choices=[('F&L', 'F&L'), ('MXP', 'MXP'), ('BD', 'BD'), ('B2C', 'B2C'), ('IGV', 'IGV'), ('OGV', 'OGV'), ('IGT', 'IGT'), ('OGT', 'OGT'), ('Newbie', 'Newbie')], max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NationalConferenceDelegate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cv', models.FileField(blank=True, null=True, upload_to='')),
                ('indemnity_form', models.FileField(null=True, upload_to='')),
                ('id_front', models.ImageField(null=True, upload_to='')),
                ('id_back', models.ImageField(null=True, upload_to='')),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('lc', models.CharField(blank=True, choices=[('6TH OCTOBER UNIVERSITY', '6TH OCTOBER UNIVERSITY'), ('AAST ALEXANDRIA', 'AAST ALEXANDRIA'), ('AAST IN CAIRO', 'AAST IN CAIRO'), ('AIN SHAMS UNIVERSITY', 'AIN SHAMS UNIVERSITY'), ('ALEXANDRIA', 'ALEXANDRIA'), ('AUC', 'AUC'), ('BENI SUEF', 'BENI SUEF'), ('CAIRO UNIVERSITY', 'CAIRO UNIVERSITY'), ('DAMIETTA', 'DAMIETTA'), ('GUC', 'GUC'), ('HELWAN', 'HELWAN'), ('LUXOR & ASWAN', 'LUXOR & ASWAN'), ('MANSOURA', 'MANSOURA'), ('MC EGYPT', 'MC EGYPT'), ('MENOFIA', 'MENOFIA'), ('MIU', 'MIU'), ('MSA', 'MSA'), ('MUST', 'MUST'), ('SUEZ', 'SUEZ'), ('TANTA', 'TANTA'), ('ZAGAZIG', 'ZAGAZIG')], max_length=50, null=True, verbose_name='LC')),
                ('role', models.CharField(blank=True, choices=[('LCP', 'LCP'), ('LCVP', 'LCVP'), ('MM', 'MM'), ('Member', 'Member'), ('Alumni', 'Alumni')], max_length=50, null=True)),
                ('function', models.CharField(blank=True, choices=[('LCP', 'LCP'), ('F&L', 'F&L'), ('MXP', 'MXP'), ('BD', 'BD'), ('B2C', 'B2C'), ('IGV', 'IGV'), ('OGV', 'OGV'), ('IGT', 'IGT'), ('OGT', 'OGT'), ('Alumni', 'Alumni')], max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='conference',
            name='date',
            field=models.DateField(help_text='Please use the following format: YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='ewadelegate',
            name='function',
            field=models.CharField(blank=True, choices=[('LCP', 'LCP'), ('F&L', 'F&L'), ('MXP', 'MXP'), ('BD', 'BD'), ('B2C', 'B2C'), ('IGV', 'IGV'), ('OGV', 'OGV'), ('IGT', 'IGT'), ('OGT', 'OGT'), ('Alumni', 'Alumni')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ewaevent',
            name='date',
            field=models.DateField(help_text='Please use the following format: YYYY-MM-DD'),
        ),
        migrations.DeleteModel(
            name='ConferenceDelegate',
        ),
        migrations.AddField(
            model_name='nationalconferencedelegate',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.conference'),
        ),
        migrations.AddField(
            model_name='localconferencedelegate',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.conference'),
        ),
    ]