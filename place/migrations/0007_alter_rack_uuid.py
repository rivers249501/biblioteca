# Generated by Django 3.2 on 2022-05-19 19:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7e7e7a50-f97a-4dc5-9ec0-78ba22fc791e')),
        ),
    ]
