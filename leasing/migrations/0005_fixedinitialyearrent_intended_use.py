# Generated by Django 2.0.4 on 2018-04-26 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0004_add_sap_fields_to_receivabletype'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedinitialyearrent',
            name='intended_use',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.RentIntendedUse', verbose_name='Intended use'),
        ),
    ]
