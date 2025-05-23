# Generated by Django 4.1.5 on 2023-03-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_artikel_bild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='preis',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='kunde',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
