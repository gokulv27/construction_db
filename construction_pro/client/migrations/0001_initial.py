# Generated by Django 5.1.3 on 2024-11-17 14:04

import django.db.models.deletion
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
                ('client_lead_name', models.CharField(max_length=100)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='client.client')),
            ],
        ),
    ]