# Generated by Django 2.1.2 on 2020-05-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0026_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
