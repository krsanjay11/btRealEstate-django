# Generated by Django 3.1.1 on 2020-10-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bt', '0005_auto_20201022_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]