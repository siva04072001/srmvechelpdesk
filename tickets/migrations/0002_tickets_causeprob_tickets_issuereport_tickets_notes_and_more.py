# Generated by Django 4.0.3 on 2022-06-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='causeProb',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='issueReport',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='notes',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='problemDesc',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='solGiven',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
