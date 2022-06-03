# Generated by Django 4.0.4 on 2022-05-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eagro', '0007_usercart_cproduct_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oprod_id', models.IntegerField()),
                ('oprod_size', models.CharField(max_length=20)),
                ('ousername', models.CharField(max_length=50)),
                ('oproduct_name', models.CharField(max_length=50)),
                ('oproduct_price', models.FloatField()),
                ('oproduct_desc', models.CharField(max_length=300)),
                ('oproduct_cat', models.CharField(max_length=30)),
                ('ouser_address', models.CharField(max_length=200)),
                ('ouser_mobile', models.CharField(max_length=14)),
            ],
        ),
    ]
