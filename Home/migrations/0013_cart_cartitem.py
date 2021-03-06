# Generated by Django 3.0.5 on 2020-08-03 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Total_price', models.CharField(max_length=100)),
                ('No_of_items', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('Cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Cart')),
            ],
        ),
    ]
