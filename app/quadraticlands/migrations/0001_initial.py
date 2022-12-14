# Generated by Django 2.2.4 on 2021-04-21 01:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import quadraticlands.models
from django.utils.translation import gettext_lazy as _


class Uint256Field(models.DecimalField):
    description = _("Ethereum uint256 number")
    '''
    Field to store ethereum uint256 values. Uses Decimal db type without decimals to store
    in the database, but retrieve as `int` instead of `Decimal` (https://docs.python.org/3/library/decimal.html)
    https://github.com/gnosis/gnosis-py/blob/master/gnosis/eth/django/models.py
    '''
    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] = 79  # 2 ** 256 is 78 digits
        kwargs['decimal_places'] = 0
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_digits']
        del kwargs['decimal_places']
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return int(value)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0172_auto_20210216_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuadLandsFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(unique=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(blank=True, default='')),
                ('answer', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='MissionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_of_use', models.BooleanField(default=False)),
                ('proof_of_receive', models.BooleanField(default=False)),
                ('proof_of_knowledge', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mission_status', to='dashboard.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='InitialTokenDistribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('claim_total', Uint256Field(default=0)),
                ('distribution', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initial_distribution', to='dashboard.Profile')),
            ],
        ),
    ]
