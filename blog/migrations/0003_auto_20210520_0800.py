# Generated by Django 3.0.7 on 2021-05-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210520_0650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='dob',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
