# Generated by Django 4.0.1 on 2022-01-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='is_active',
            field=models.BooleanField(choices=[(True, 'Active'), (False, 'InActive')], default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]