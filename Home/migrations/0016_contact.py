# Generated by Django 3.0.5 on 2020-08-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_remove_order_delievery_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Message', models.CharField(max_length=300)),
            ],
        ),
    ]
