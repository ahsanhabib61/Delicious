# Generated by Django 3.0.5 on 2020-07-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20200715_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='Price',
            field=models.IntegerField(),
        ),
    ]