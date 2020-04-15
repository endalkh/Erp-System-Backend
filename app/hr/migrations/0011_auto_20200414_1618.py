# Generated by Django 3.0.5 on 2020-04-14 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0010_auto_20200414_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employemodel',
            name='roles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_detain', to='hr.RoleModel', verbose_name='Role'),
        ),
    ]