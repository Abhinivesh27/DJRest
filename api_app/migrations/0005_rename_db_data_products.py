# Generated by Django 3.2.5 on 2022-02-10 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_db_data_imagealt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='db_data',
            new_name='products',
        ),
    ]
