# Generated by Django 4.2.5 on 2023-10-04 15:57

from django.db import migrations, models
import halaman_awal.models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman_awal', '0015_alter_aboutus_options_alter_sliders_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='footers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_hp', models.CharField(max_length=15, validators=[halaman_awal.models.validate_nomor_hp])),
            ],
        ),
        migrations.AlterModelTable(
            name='aboutus',
            table=None,
        ),
    ]
