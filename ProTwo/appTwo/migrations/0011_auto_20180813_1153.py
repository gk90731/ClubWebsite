# Generated by Django 2.0.5 on 2018-08-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0010_auto_20180813_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='FULL NAME'),
        ),
    ]