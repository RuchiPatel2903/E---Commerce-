# Generated by Django 3.2.13 on 2023-07-15 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='u_id',
        ),
    ]
