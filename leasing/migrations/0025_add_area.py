# Generated by Django 2.1.1 on 2018-09-26 10:54

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import leasing.enums


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0024_fix_contract_type_verbose_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('type', enumfields.fields.EnumField(enum=leasing.enums.AreaType, max_length=30, verbose_name='Area type')),
                ('identifier', models.CharField(max_length=255, verbose_name='Identifier')),
                ('external_id', models.CharField(max_length=255, verbose_name='External ID')),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326, verbose_name='Geometry')),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='Metadata')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Area',
            },
        ),
        migrations.CreateModel(
            name='AreaSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('identifier', models.CharField(max_length=255, unique=True, verbose_name='Identifier')),
            ],
            options={
                'verbose_name': 'Area source',
                'verbose_name_plural': 'Area source',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='area',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='areas', to='leasing.AreaSource', verbose_name='Source'),
        ),
    ]