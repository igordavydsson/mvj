# Generated by Django 2.0.5 on 2018-05-31 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0010_make_relatedlease_type_optional'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lease',
            options={'permissions': (('view_lease', 'Can view lease'),)},
        ),
    ]
