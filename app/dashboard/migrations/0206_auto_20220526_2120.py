# Generated by Django 2.2.24 on 2022-05-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0205_auto_20220526_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='dpopp_trust_bonus',
            new_name='passport_trust_bonus',
        ),
        migrations.AlterField(
            model_name='profile',
            name='passport_trust_bonus',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Trust Bonus score based on Gitcoin Passport', max_digits=5, null=True),
        ),
    ]