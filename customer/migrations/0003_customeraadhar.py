# Generated by Django 4.2.1 on 2023-05-26 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customeraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_number', models.IntegerField()),
                ('adhar_name', models.CharField(max_length=20)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]