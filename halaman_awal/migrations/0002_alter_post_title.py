# Generated by Django 4.2.5 on 2023-09-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman_awal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
