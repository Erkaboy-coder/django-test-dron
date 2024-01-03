# Generated by Django 4.2.7 on 2024-01-03 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=250)),
                ('path', models.FileField(blank=True, upload_to='data/files/', verbose_name='files')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'File',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=256, null=True, verbose_name='firstname')),
                ('lastname', models.CharField(blank=True, max_length=256, null=True, verbose_name='lastname')),
                ('email', models.EmailField(blank=True, default='', max_length=250, verbose_name='email')),
                ('contact', models.CharField(blank=True, default='', max_length=250, verbose_name='contact')),
                ('live', models.IntegerField(choices=[(0, 'Faol emas'), (1, 'Faol')], default=1)),
                ('user', models.OneToOneField(help_text='User linked to this profile', on_delete=django.db.models.deletion.PROTECT, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Related user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
