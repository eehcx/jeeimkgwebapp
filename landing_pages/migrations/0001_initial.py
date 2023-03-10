# Generated by Django 4.1.6 on 2023-02-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('business_type', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('social_media', models.CharField(max_length=100)),
                ('monthly_revenue', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('needs', models.TextField()),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
