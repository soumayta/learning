# Generated by Django 3.2.9 on 2021-12-05 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('customer', '0003_client_customer_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='product_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]
