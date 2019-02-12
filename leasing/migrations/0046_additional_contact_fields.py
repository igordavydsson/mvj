# Generated by Django 2.1.7 on 2019-02-12 13:45

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0045_additional_lease_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='care_of',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='c/o'),
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Note'),
        ),
    ]