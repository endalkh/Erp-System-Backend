# Generated by Django 3.0.5 on 2020-04-11 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatagoryModel',
            fields=[
                ('subCatagory', models.CharField(auto_created=True, max_length=100, unique=True)),
                ('catagory', models.CharField(auto_created=True, max_length=100, unique=True)),
                ('catagoryId', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('companyId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=100, unique=True, verbose_name='Company name')),
                ('generalManger', models.CharField(max_length=100, verbose_name='General manager')),
                ('contactPerson', models.CharField(max_length=100, verbose_name='Contact person')),
                ('workingField', models.CharField(max_length=100, verbose_name='Working Field')),
                ('paymentOption', models.CharField(choices=[('VAT', 'VAT'), ('TOT', 'TOT')], max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('tinNumber', models.IntegerField(verbose_name='Tin number')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('departmentId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('departmentName', models.CharField(blank=True, max_length=20, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceModel',
            fields=[
                ('invoiceId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('salesPerson', models.CharField(max_length=100)),
                ('subTotal', models.FloatField(verbose_name='Sub total')),
                ('Total', models.FloatField()),
                ('Tax', models.FloatField()),
                ('date', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('orderNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('orderName', models.CharField(max_length=100)),
                ('orderQuantity', models.IntegerField()),
                ('salesPerson', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50)),
                ('orderDate', models.DateField(max_length=20)),
                ('shipmentAddress', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.CompanyModel')),
            ],
        ),
        migrations.CreateModel(
            name='sivModel',
            fields=[
                ('sivId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('itemId', models.IntegerField()),
                ('itemName', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('sivDate', models.DateField()),
                ('warehouseName', models.CharField(max_length=100)),
                ('approve', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentScheduleModel',
            fields=[
                ('shipmentId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('shipmentNumber', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField(max_length=20)),
                ('departureDate', models.DateField(max_length=50)),
                ('deliveryDate', models.DateField(max_length=50)),
                ('deliveryPerson', models.CharField(max_length=100)),
                ('receivedStatus', models.CharField(max_length=100, verbose_name='Recieved Status')),
                ('conditionOnTrack', models.CharField(max_length=100, verbose_name='Condition on truack')),
                ('receivedBy', models.CharField(max_length=100, verbose_name='Recieved By')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hr.OrderModel')),
            ],
        ),
        migrations.CreateModel(
            name='RoleModel',
            fields=[
                ('roleId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('role', models.CharField(blank=True, max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DepartmentModel', verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('itemId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=100)),
                ('warehouseName', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('retailPrice', models.FloatField()),
                ('packaging', models.CharField(max_length=100)),
                ('discount', models.IntegerField(null=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.CatagoryModel', verbose_name='Catagory')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_order', to='hr.OrderModel')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLineItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('unitPrice', models.FloatField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('ItemId', models.IntegerField()),
                ('item_discount', models.FloatField(max_length=100)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.InvoiceModel')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeModel',
            fields=[
                ('employeId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(max_length=15, verbose_name='First name')),
                ('lastName', models.CharField(max_length=15, verbose_name='Last name')),
                ('email', models.CharField(blank=True, max_length=30, unique=True)),
                ('hiredDate', models.DateField(max_length=15, verbose_name='Hired date')),
                ('telephone', models.CharField(max_length=15)),
                ('birthDate', models.DateField(max_length=15, verbose_name='Birth date')),
                ('termOfEmployment', models.CharField(max_length=10, verbose_name='Term of Employment')),
                ('country', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.DepartmentModel', verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='claimModel',
            fields=[
                ('levelId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('level', models.CharField(blank=True, max_length=20)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.RoleModel', verbose_name='Role')),
            ],
        ),
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.OrderModel')),
            ],
            options={
                'unique_together': {('order', 'status')},
            },
        ),
    ]
