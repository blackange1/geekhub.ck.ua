# Generated by Django 4.0.2 on 2022-02-08 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField(unique=True)),
            ],
        ),
    ]