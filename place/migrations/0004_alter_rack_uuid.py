# Generated by Django 3.2 on 2022-05-19 14:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('41a79877-8d84-4fe5-8b17-3e0a4e9caaa0')),
        ),
    ]