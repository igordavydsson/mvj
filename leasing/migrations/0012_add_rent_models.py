# Generated by Django 2.0.4 on 2018-04-05 12:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import leasing.enums


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0011_rename_period_type_enum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('period', enumfields.fields.EnumField(enum=leasing.enums.PeriodType, max_length=30, verbose_name='Period')),
                ('base_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Base amount')),
                ('base_amount_period', enumfields.fields.EnumField(enum=leasing.enums.PeriodType, max_length=30, verbose_name='Base amount period')),
                ('base_year_rent', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Base year rent')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FixedInitialYearRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndexAdjustedRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('factor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Factor')),
            ],
        ),
        migrations.CreateModel(
            name='LeaseBasisOfRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_m2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Floor m2')),
                ('index', models.PositiveIntegerField(blank=True, null=True, verbose_name='Index')),
                ('amount_per_floor_m2_index_100', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount per floor m^2 (index 100)')),
                ('amount_per_floor_m2_index', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount per floor m^2 (index)')),
                ('percent', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Percent')),
                ('year_rent_index_100', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Year rent (index 100)')),
                ('year_rent_index', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Year rent (index)')),
            ],
        ),
        migrations.CreateModel(
            name='PayableRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('difference_percent', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Difference percent')),
                ('calendar_year_rent', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Calendar year rent')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('type', enumfields.fields.EnumField(enum=leasing.enums.RentType, max_length=30, verbose_name='Type')),
                ('cycle', enumfields.fields.EnumField(blank=True, enum=leasing.enums.RentCycle, max_length=30, null=True, verbose_name='Cycle')),
                ('index_type', enumfields.fields.EnumField(blank=True, enum=leasing.enums.IndexType, max_length=30, null=True, verbose_name='Index type')),
                ('due_dates_type', enumfields.fields.EnumField(blank=True, enum=leasing.enums.DueDatesType, max_length=30, null=True, verbose_name='Due dates type')),
                ('due_dates_per_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Due dates per year')),
                ('elementary_index', models.PositiveIntegerField(blank=True, null=True, verbose_name='Elementary index')),
                ('index_rounding', models.PositiveIntegerField(blank=True, null=True, verbose_name='Index rounding')),
                ('x_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='X value')),
                ('y_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Y value')),
                ('y_value_start', models.PositiveIntegerField(blank=True, null=True, verbose_name='Y value start')),
                ('equalization_start_date', models.DateField(blank=True, null=True, verbose_name='Equalization start date')),
                ('equalization_end_date', models.DateField(blank=True, null=True, verbose_name='Equalization end date')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active?')),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rents', to='leasing.Lease', verbose_name='Lease')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RentAdjustment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('type', enumfields.fields.EnumField(enum=leasing.enums.RentAdjustmentType, max_length=30, verbose_name='Type')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('full_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Full amount')),
                ('amount_type', enumfields.fields.EnumField(enum=leasing.enums.RentAdjustmentAmountType, max_length=30, verbose_name='Amount type')),
                ('amount_left', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount left')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('decision', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.Decision', verbose_name='Decision')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RentDueDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('day', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='Day')),
                ('month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Month')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='due_dates', to='leasing.Rent', verbose_name='Rent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RentIntendedUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='rentadjustment',
            name='intended_use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leasing.RentIntendedUse', verbose_name='Intended use'),
        ),
        migrations.AddField(
            model_name='rentadjustment',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_adjustments', to='leasing.Rent', verbose_name='Rent'),
        ),
        migrations.AddField(
            model_name='payablerent',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payable_rents', to='leasing.Rent', verbose_name='Rent'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='intended_use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leasing.RentIntendedUse', verbose_name='Intended use'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='lease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='basis_of_rents', to='leasing.Lease', verbose_name='Lease'),
        ),
        migrations.AddField(
            model_name='indexadjustedrent',
            name='intended_use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leasing.RentIntendedUse', verbose_name='Intended use'),
        ),
        migrations.AddField(
            model_name='indexadjustedrent',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='index_adjusted_rents', to='leasing.Rent', verbose_name='Rent'),
        ),
        migrations.AddField(
            model_name='fixedinitialyearrent',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_initial_year_rents', to='leasing.Rent', verbose_name='Rent'),
        ),
        migrations.AddField(
            model_name='contractrent',
            name='intended_use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leasing.RentIntendedUse', verbose_name='Intended use'),
        ),
        migrations.AddField(
            model_name='contractrent',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_rents', to='leasing.Rent', verbose_name='Rent'),
        ),
    ]