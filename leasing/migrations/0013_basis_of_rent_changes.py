# Generated by Django 2.0.6 on 2018-06-11 12:28

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import leasing.enums


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0012_add_area_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasisOfRentBuildPermissionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='basisofrentdecision',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='basisofrentrate',
            name='intended_use',
        ),
        migrations.RemoveField(
            model_name='basisofrentrate',
            name='period',
        ),
        migrations.AddField(
            model_name='basisofrentdecision',
            name='decision_date',
            field=models.DateField(blank=True, null=True, verbose_name='Decision date'),
        ),
        migrations.AddField(
            model_name='basisofrentdecision',
            name='decision_maker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='basis_of_rent_decisions', to='leasing.DecisionMaker', verbose_name='Decision maker'),
        ),
        migrations.AddField(
            model_name='basisofrentdecision',
            name='reference_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Reference number'),
        ),
        migrations.AddField(
            model_name='basisofrentdecision',
            name='section',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='basisofrentrate',
            name='area_unit',
            field=enumfields.fields.EnumField(blank=True, enum=leasing.enums.AreaUnit, max_length=20, null=True, verbose_name='Area unit'),
        ),
        migrations.AlterField(
            model_name='basisofrent',
            name='index',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.Index', verbose_name='Index'),
        ),
        migrations.AddField(
            model_name='basisofrentrate',
            name='build_permission_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.BasisOfRentBuildPermissionType', verbose_name='Build permission type'),
        ),
    ]
