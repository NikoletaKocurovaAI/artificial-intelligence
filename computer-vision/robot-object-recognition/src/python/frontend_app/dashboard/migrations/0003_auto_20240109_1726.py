# Generated by Django 3.0.10 on 2024-01-09 17:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_auto_20240109_1721"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="RobotTemp",
            new_name="Robot",
        ),
    ]
