# Generated by Django 3.1.1 on 2020-10-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaffManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Phone_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
