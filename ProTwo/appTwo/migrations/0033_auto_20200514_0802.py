# Generated by Django 3.0.5 on 2020-05-14 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0032_auto_20200514_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aptistudent',
            name='marks_obt',
            field=models.IntegerField(blank=True, null=True, verbose_name='Marks Obtained'),
        ),
        migrations.AlterField(
            model_name='aptistudent',
            name='test_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appTwo.AptiTest', verbose_name='Test no.:'),
        ),
    ]