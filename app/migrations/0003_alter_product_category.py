# Generated by Django 4.1.1 on 2023-01-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_customer_orderplaced_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('Mo', 'Mo'), ('ban', 'ban')], max_length=100),
        ),
    ]
