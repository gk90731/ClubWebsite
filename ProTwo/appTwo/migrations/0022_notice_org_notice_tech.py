# Generated by Django 2.1.2 on 2019-03-30 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0021_final_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice_org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_notice_org', models.TextField(max_length=10000, verbose_name='Area to write latest notice for organising teams:')),
            ],
        ),
        migrations.CreateModel(
            name='notice_tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_notice_tech', models.TextField(max_length=10000, verbose_name='Area to write latest notice for trchnical teams:')),
            ],
        ),
    ]
