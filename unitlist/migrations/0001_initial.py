# Generated by Django 2.2.4 on 2020-10-10 15:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('att_id', models.IntegerField(default=0, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('att_desc', models.CharField(default='', max_length=100, validators=[django.core.validators.RegexValidator(message='半角英数字とアンダーバーのみにしてください', regex='^[a-zA-Z0-9_]+$')])),
                ('att_desc_lower', models.CharField(default='', max_length=100, validators=[django.core.validators.RegexValidator(message='半角小文字英数字とアンダーバーのみにしてください', regex='^[a-z0-9_]+$')])),
                ('att_desc_jp', models.CharField(default='', max_length=100)),
                ('att_advantage_id', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.IntegerField(default=0, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('role_desc', models.CharField(default='', max_length=100, validators=[django.core.validators.RegexValidator(message='半角小文字英数字とアンダーバーのみにしてください', regex='^[a-z0-9_]+$')])),
                ('role_desc_jp', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('unit_type_id', models.IntegerField(default=0, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('unit_type_desc', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_enable', models.BooleanField(default=False)),
                ('unit_no', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('unit_id', models.CharField(default='', max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='半角小文字英数字とアンダーバーのみにしてください', regex='^[a-z0-9_]+$')])),
                ('sub_name', models.CharField(blank=True, default='', max_length=100)),
                ('jp_name', models.CharField(blank=True, default='', max_length=100)),
                ('rarity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('skill_desc', models.CharField(blank=True, default='', max_length=500)),
                ('skill_wait', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('gender', models.CharField(blank=True, default='', max_length=100)),
                ('race', models.CharField(blank=True, default='', max_length=100)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unitlist.Attribute')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unitlist.Role')),
                ('unit_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unitlist.UnitType')),
            ],
        ),
    ]
