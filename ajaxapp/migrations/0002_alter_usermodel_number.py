# Generated by Django 4.1.1 on 2022-09-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='number',
            field=models.CharField(max_length=12),
        ),
    ]