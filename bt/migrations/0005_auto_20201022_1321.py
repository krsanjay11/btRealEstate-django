# Generated by Django 3.1.1 on 2020-10-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bt', '0004_auto_20201022_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]