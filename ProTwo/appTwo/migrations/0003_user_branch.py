# Generated by Django 2.0.5 on 2018-08-13 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0002_user_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.CharField(choices=[('ETC', 'ETC'), ('EEE', 'EEE'), ('EE', 'EE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL'), ('IT', 'IT'), ('CSE', 'CSE')], default='', max_length=5),
            preserve_default=False,
        ),
    ]