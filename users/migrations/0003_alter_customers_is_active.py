# Generated by Django 4.0.1 on 2022-01-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_alter_customers_is_active_alter_customers_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]