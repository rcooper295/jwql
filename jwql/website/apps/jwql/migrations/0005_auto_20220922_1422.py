# Generated by Django 3.1.7 on 2022-09-22 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwql', '0004_auto_20220922_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnailfilterinfo',
            name='inst_handler',
        ),
        migrations.DeleteModel(
            name='InstrumentFilterHandler',
        ),
        migrations.DeleteModel(
            name='ThumbnailFilterInfo',
        ),
    ]