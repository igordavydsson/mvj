# Generated by Django 2.0.5 on 2018-05-28 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0008_plan_unit_changes'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaseAreaAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Postal code')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlanUnitAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Postal code')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlotAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Postal code')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='leasearea',
            name='address',
        ),
        migrations.RemoveField(
            model_name='leasearea',
            name='city',
        ),
        migrations.RemoveField(
            model_name='leasearea',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='planunit',
            name='address',
        ),
        migrations.RemoveField(
            model_name='planunit',
            name='city',
        ),
        migrations.RemoveField(
            model_name='planunit',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='address',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='city',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='plotaddress',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='leasing.Plot'),
        ),
        migrations.AddField(
            model_name='planunitaddress',
            name='plan_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='leasing.PlanUnit'),
        ),
        migrations.AddField(
            model_name='leaseareaaddress',
            name='lease_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='leasing.LeaseArea'),
        ),
    ]
