# Generated by Django 4.2.4 on 2023-08-07 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_score_scores_score_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]