# Generated by Django 3.2.9 on 2021-12-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_id', models.IntegerField()),
                ('cus_name', models.CharField(max_length=25)),
                ('cus_review', models.CharField(max_length=45)),
            ],
        ),
    ]
