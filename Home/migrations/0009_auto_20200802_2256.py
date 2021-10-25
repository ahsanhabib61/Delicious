# Generated by Django 3.0.5 on 2020-08-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_address_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.AddField(
            model_name='address',
            name='Zip_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='Phone_NO',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_No',
            field=models.CharField(max_length=100),
        ),
    ]