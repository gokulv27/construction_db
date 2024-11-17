# Generated by Django 5.1.3 on 2024-11-17 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('initials', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('PLANNING', 'Planning'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('ON_HOLD', 'On Hold')], default='PLANNING', max_length=20)),
                ('progress', models.IntegerField(default=0)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spent', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('land_facing', models.CharField(choices=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West')], max_length=1)),
                ('land_width', models.DecimalField(decimal_places=2, max_digits=8)),
                ('land_breadth', models.DecimalField(decimal_places=2, max_digits=8)),
                ('num_floors', models.IntegerField()),
                ('build_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('team', models.ManyToManyField(to='project.teammember')),
            ],
        ),
    ]
