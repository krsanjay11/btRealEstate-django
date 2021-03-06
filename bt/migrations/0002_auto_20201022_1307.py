# Generated by Django 3.1.1 on 2020-10-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='sno',
            field=models.AutoField(default='2', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.CharField(default='', max_length=20),
        ),
    ]
