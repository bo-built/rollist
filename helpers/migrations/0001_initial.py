# Generated by Django 3.2.6 on 2021-11-10 15:17

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureFlag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('value', models.IntegerField(choices=[(0, 'Off'), (1, 'On')], default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('changed', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
