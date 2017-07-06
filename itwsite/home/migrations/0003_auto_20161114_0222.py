# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-13 20:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_menu_fri_menu_sat_menu_sun_menu_thr_menu_wed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usr_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('Room_number', models.CharField(max_length=6)),
                ('Phone_number', models.CharField(max_length=10)),
                ('user_mess', models.CharField(max_length=30)),
                ('hostel_name', models.CharField(max_length=30)),
                ('user_balance', models.IntegerField()),
                ('user_expense', models.IntegerField()),
                ('Branch_name', models.CharField(max_length=50)),
                ('Year', models.CharField(max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='messmaharaj',
            name='maharaj_dp',
        ),
    ]
