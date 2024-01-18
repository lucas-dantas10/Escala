# Generated by Django 5.0.1 on 2024-01-18 15:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_participacao_missa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="missa",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="participacao",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
