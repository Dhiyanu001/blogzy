# Generated by Django 4.1.4 on 2023-02-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', 'Programming/Technology'), ('2', 'Health/Fitness'), ('3', 'Personal Experience'), ('4', 'Fashion'), ('5', 'Food'), ('6', 'Travel'), ('7', 'Placements'), ('8', 'Exams'), ('9', 'sports'), ('10', 'Education'), ('11', 'Awards'), ('12', 'Information'), ('13', 'Other')], default='1', max_length=20),
        ),
    ]
