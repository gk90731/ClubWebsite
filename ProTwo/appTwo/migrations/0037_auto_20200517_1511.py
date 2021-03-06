# Generated by Django 3.0.6 on 2020-05-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0036_remove_aptistudent_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aptistudent',
            name='branch',
            field=models.CharField(choices=[('ETC', 'ETC'), ('EEE', 'EEE'), ('EE', 'EE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL'), ('IT', 'IT'), ('CS', 'CS'), ('MCA', 'MBA'), ('MBA', 'MBA')], max_length=10, verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='org_team',
            name='branch',
            field=models.CharField(choices=[('ETC', 'ETC'), ('EEE', 'EEE'), ('EE', 'EE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL'), ('IT', 'IT'), ('CS', 'CS'), ('MCA', 'MBA'), ('MBA', 'MBA')], max_length=5, verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='tech_team',
            name='branch',
            field=models.CharField(choices=[('ETC', 'ETC'), ('EEE', 'EEE'), ('EE', 'EE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL'), ('IT', 'IT'), ('CS', 'CS'), ('MCA', 'MBA'), ('MBA', 'MBA')], max_length=5, verbose_name='Branch'),
        ),
    ]
