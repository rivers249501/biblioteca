# Generated by Django 3.2 on 2022-05-19 02:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7504e51d-a4dd-4961-a8a1-4fb67a492384')),
        ),
    ]
