# Generated by Django 2.1.5 on 2019-06-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_auto_20190531_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='intime',
            field=models.DateTimeField(),
        ),
    ]
