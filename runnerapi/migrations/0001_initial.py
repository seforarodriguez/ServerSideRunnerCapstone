# Generated by Django 4.1.3 on 2023-01-06 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('pace_of_run', models.IntegerField()),
                ('miles_to_run', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('county', models.CharField(max_length=100)),
                ('miles_available_to_run', models.IntegerField()),
                ('difficulty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.IntegerField()),
                ('zipcode', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventAttendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runnerapi.event')),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runnerapi.runner')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='events_assisting', through='runnerapi.EventAttendee', to='runnerapi.runner'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runnerapi.runner'),
        ),
        migrations.AddField(
            model_name='event',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runnerapi.park'),
        ),
    ]
