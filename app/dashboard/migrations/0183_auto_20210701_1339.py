# Generated by Django 2.2.24 on 2021-07-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0182_auto_20210701_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earning',
            name='token_value',
            field=models.DecimalField(decimal_places=18, default=0, max_digits=50),
        ),
    ]