# Generated by Django 2.0.2 on 2018-04-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180417_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='des',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='src',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
