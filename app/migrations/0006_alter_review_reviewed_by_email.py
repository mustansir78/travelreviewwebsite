# Generated by Django 4.1.4 on 2023-01-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_item_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewed_by_email',
            field=models.EmailField(max_length=254),
        ),
    ]