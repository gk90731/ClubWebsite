# Generated by Django 2.0.5 on 2018-08-13 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0007_user_workshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.IntegerField(default='0', max_length=10),
            preserve_default=False,
        ),
    ]