# Generated by Django 3.1.2 on 2020-10-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_libro_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='ISBN',
            field=models.IntegerField(default=0),
        ),
    ]
