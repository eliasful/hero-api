# Generated by Django 2.1.3 on 2018-11-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_auto_20181128_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='favorite',
            field=models.TextField(),
        ),
    ]
