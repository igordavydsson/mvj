# Generated by Django 2.1.1 on 2018-10-02 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0027_add_geometries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='y_value_start',
        ),
    ]