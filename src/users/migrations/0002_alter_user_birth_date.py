# Generated by Django 4.0.5 on 2022-06-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Birth date'),
        ),
    ]
