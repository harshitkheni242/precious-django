# Generated by Django 4.2.1 on 2023-12-15 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_categories_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
