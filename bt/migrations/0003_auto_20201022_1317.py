# Generated by Django 3.1.1 on 2020-10-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bt', '0002_auto_20201022_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
