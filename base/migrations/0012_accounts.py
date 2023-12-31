# Generated by Django 4.2.2 on 2023-08-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_rename_averagevaluesetting_averagevalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('telegram', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phonenumber', models.IntegerField(blank=True, default=0, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
