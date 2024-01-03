# Generated by Django 4.2.7 on 2024-01-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dron', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='droncategorymodel',
            name='weight_limit',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicationmodel',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]