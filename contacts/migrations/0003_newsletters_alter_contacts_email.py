# Generated by Django 5.0.4 on 2024-04-23 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_prenom_contacts_sujet'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'News Letter',
                'verbose_name_plural': 'News Letters',
            },
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
