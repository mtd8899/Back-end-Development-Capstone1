# Generated by Django 4.1.7 on 2023-10-21 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("concert", "0004_alter_concert_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="concert",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2023, 10, 21, 14, 40, 21, 131353)
            ),
        ),
    ]
