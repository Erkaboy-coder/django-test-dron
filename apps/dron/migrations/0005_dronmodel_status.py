# Generated by Django 4.2.7 on 2024-01-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dron', '0004_deliverymodel_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='dronmodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, '')], default=1),
        ),
    ]
