# Generated by Django 4.1.1 on 2022-12-19 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Ordered_date',
            new_name='ordered_date',
        ),
    ]
