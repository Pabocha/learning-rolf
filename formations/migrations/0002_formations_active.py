# Generated by Django 5.0.4 on 2024-04-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formations',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
