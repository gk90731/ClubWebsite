# Generated by Django 2.1.2 on 2019-03-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0015_auto_20190309_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_new',
            name='interest',
            field=models.CharField(help_text='(e.g. Python,Java,PCB designing,Circuiting,Android Development....etc....)', max_length=10000, verbose_name='What are you interested in?:'),
        ),
        migrations.AlterField(
            model_name='user_new',
            name='link',
            field=models.CharField(help_text='(also give link if uploaded on social sites)', max_length=10000, verbose_name='What Projects done till now?:'),
        ),
        migrations.AlterField(
            model_name='user_new',
            name='skills',
            field=models.CharField(help_text='(e.g. Python,Java,PCB designing,Circuiting,Android Development....etc....)', max_length=10000, verbose_name='What you Know?:'),
        ),
        migrations.AlterField(
            model_name='user_new',
            name='workshop',
            field=models.CharField(help_text='(e.g.Android development,Drone making,Robotics....etc..)', max_length=10000, verbose_name='Attended any workshop?:'),
        ),
    ]
