# Generated by Django 2.2.24 on 2022-05-24 10:25

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0206_auto_20220524_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='did',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dpopp_passport',
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('did', models.CharField(max_length=100, unique=True)),
                ('dpopp_passport', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
