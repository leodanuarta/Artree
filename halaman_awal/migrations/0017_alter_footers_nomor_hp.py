# Generated by Django 4.2.5 on 2023-10-04 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman_awal', '0016_footers_alter_aboutus_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footers',
            name='nomor_hp',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Nomor telepon harus dimulai dengan '08' dan memiliki panjang minimal 10 karakter (termasuk '08').", regex='^08\\d{8,}$')]),
        ),
    ]
