# Generated by Django 3.2.5 on 2022-02-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_auto_20220210_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_data',
            name='imageAlt',
            field=models.CharField(default='loading...', max_length=100),
        ),
    ]
