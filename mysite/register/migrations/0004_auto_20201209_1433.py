# Generated by Django 3.1.1 on 2020-12-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20201209_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default='1999-10-01', max_length=8),
        ),
    ]
