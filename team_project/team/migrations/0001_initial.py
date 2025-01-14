# Generated by Django 4.1.4 on 2022-12-16 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name', max_length=100)),
                ('location', models.CharField(default='no location', max_length=100)),
                ('division', models.CharField(default='no division', max_length=100)),
                ('win', models.CharField(default='no wins', max_length=100)),
                ('loss', models.CharField(default='no name', max_length=100)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='team.league')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name', max_length=100)),
                ('position', models.CharField(default='no position', max_length=100)),
                ('age', models.CharField(default='no age', max_length=100)),
                ('years_of_experience', models.CharField(default='no years of experience', max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='team.team')),
            ],
        ),
    ]
