# Generated by Django 2.1.5 on 2019-02-12 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0042_contract_sign_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mortgagedocument',
            name='contract',
        ),
        migrations.DeleteModel(
            name='MortgageDocument',
        ),
    ]
