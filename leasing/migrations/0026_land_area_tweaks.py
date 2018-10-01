# Generated by Django 2.1.1 on 2018-09-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0025_add_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planunitaddress',
            name='plan_unit',
        ),
        migrations.RemoveField(
            model_name='plotaddress',
            name='plot',
        ),
        migrations.RemoveField(
            model_name='planunit',
            name='type',
        ),
        migrations.AlterField(
            model_name='leasearea',
            name='section_area',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Section area'),
        ),
        migrations.AlterField(
            model_name='planunit',
            name='section_area',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Section area'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='section_area',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Section area'),
        ),
        migrations.DeleteModel(
            name='PlanUnitAddress',
        ),
        migrations.DeleteModel(
            name='PlotAddress',
        ),
    ]
