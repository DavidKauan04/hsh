# Generated by Django 4.1.5 on 2023-01-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=50)),
                ("district", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=50)),
                ("number", models.CharField(max_length=4)),
                ("zipcode", models.CharField(max_length=11)),
            ],
        ),
    ]