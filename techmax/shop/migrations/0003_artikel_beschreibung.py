# Generated by Django 4.1.5 on 2023-01-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_bestllteartikel_bestellteartikel'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='beschreibung',
            field=models.TextField(blank=True, null=True),
        ),
    ]
