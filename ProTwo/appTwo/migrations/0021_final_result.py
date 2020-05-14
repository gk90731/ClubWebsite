# Generated by Django 2.1.2 on 2019-03-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0020_auto_20190317_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='final_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Candidate_name', models.CharField(blank=True, max_length=100000, verbose_name='Name')),
                ('Email_id', models.EmailField(blank=True, max_length=100000, verbose_name='Email')),
                ('Branch', models.CharField(blank=True, max_length=100000, verbose_name='Branch')),
                ('Semester', models.CharField(blank=True, max_length=100000, verbose_name='Sememster')),
                ('Marks_obtained', models.IntegerField(default=0)),
            ],
        ),
    ]