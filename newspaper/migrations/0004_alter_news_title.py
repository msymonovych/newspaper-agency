# Generated by Django 5.0.3 on 2024-03-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspaper", "0003_alter_news_options_alter_redactor_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
