# Generated by Django 2.1.3 on 2019-01-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0037_make_lease_basis_of_rent_archivable'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicepayment',
            name='filing_code',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Name'),
        ),
    ]
