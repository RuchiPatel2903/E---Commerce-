# Generated by Django 3.2.13 on 2023-07-20 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0007_auto_20230718_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='O_tracker',
            fields=[
                ('otid', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('p_type', models.CharField(max_length=30)),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('ot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.o_tracker')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='O_item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.order')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
            ],
        ),
    ]
