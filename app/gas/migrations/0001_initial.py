# Generated by Django 2.1.4 on 2018-12-26 17:16

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GasAdvisory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('body', models.TextField(blank=True, default='')),
                ('active_until', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Gas Advisories',
            },
        ),
        migrations.CreateModel(
            name='GasGuzzler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('gas_used', models.DecimalField(db_index=True, decimal_places=2, max_digits=50)),
                ('pct_total', models.DecimalField(decimal_places=2, max_digits=50)),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('ID', models.CharField(blank=True, default='', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Gas Guzzlers',
            },
        ),
        migrations.CreateModel(
            name='GasProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('gas_price', models.DecimalField(db_index=True, decimal_places=2, max_digits=50)),
                ('mean_time_to_confirm_blocks', models.DecimalField(decimal_places=2, max_digits=50)),
                ('mean_time_to_confirm_minutes', models.DecimalField(db_index=True, decimal_places=2, max_digits=50)),
                ('_99confident_confirm_time_blocks', models.DecimalField(decimal_places=2, max_digits=50)),
                ('_99confident_confirm_time_mins', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
            options={
                'verbose_name_plural': 'Gas Profiles',
            },
        ),
    ]