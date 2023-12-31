# Generated by Django 4.2.5 on 2023-10-04 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman_awal', '0017_alter_footers_nomor_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='footers',
            name='link_blibli',
            field=models.CharField(default='https://www.example.com', max_length=200, validators=[django.core.validators.RegexValidator(message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'.", regex='^(http|https)://[a-zA-Z0-9.-]+(\\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')]),
        ),
        migrations.AddField(
            model_name='footers',
            name='link_ig',
            field=models.CharField(default='https://www.example.com', max_length=200, validators=[django.core.validators.RegexValidator(message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'.", regex='^(http|https)://[a-zA-Z0-9.-]+(\\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')]),
        ),
        migrations.AddField(
            model_name='footers',
            name='link_shopee',
            field=models.CharField(default='https://www.example.com', max_length=200, validators=[django.core.validators.RegexValidator(message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'.", regex='^(http|https)://[a-zA-Z0-9.-]+(\\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')]),
        ),
        migrations.AddField(
            model_name='footers',
            name='link_tokped',
            field=models.CharField(default='https://www.example.com', max_length=200, validators=[django.core.validators.RegexValidator(message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'.", regex='^(http|https)://[a-zA-Z0-9.-]+(\\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')]),
        ),
        migrations.AlterField(
            model_name='footers',
            name='nomor_hp',
            field=models.CharField(default='https://www.example.com', max_length=15, validators=[django.core.validators.RegexValidator(message="Nomor telepon harus dimulai dengan '08' dan memiliki panjang minimal 10 karakter (termasuk '08').", regex='^08\\d{8,}$')]),
        ),
    ]
