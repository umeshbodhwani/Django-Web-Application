# Generated by Django 3.0 on 2019-12-07 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_tracker', '0003_auto_20191207_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='Above_Ground_Sighter_Measurement',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='Color_Notes',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='Combination_of_Color',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='Hectare',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='Hectare_Squirrel_Number',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='Highlight_Fur_Color',
        ),
    ]