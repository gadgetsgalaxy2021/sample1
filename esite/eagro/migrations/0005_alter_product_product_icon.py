# Generated by Django 4.0.4 on 2022-05-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eagro', '0004_alter_product_product_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_icon',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
