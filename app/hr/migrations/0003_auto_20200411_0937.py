# Generated by Django 3.0.5 on 2020-04-11 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20200411_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmodel',
            name='catagory',
        ),
        migrations.RemoveField(
            model_name='itemmodel',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='itemmodel',
            name='packaging',
        ),
        migrations.RemoveField(
            model_name='itemmodel',
            name='retailPrice',
        ),
        migrations.RemoveField(
            model_name='itemmodel',
            name='warehouseName',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='orderQuantity',
        ),
    ]