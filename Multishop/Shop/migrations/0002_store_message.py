# Generated by Django 3.2.13 on 2023-07-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='message',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
