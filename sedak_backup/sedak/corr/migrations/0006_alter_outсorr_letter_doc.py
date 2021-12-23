# Generated by Django 3.2.9 on 2021-11-17 09:26

import corr.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corr', '0005_alter_outсorr_letter_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outсorr',
            name='letter_doc',
            field=models.FileField(blank=True, upload_to=corr.models.outcorr_doc_directory, validators=[django.core.validators.FileExtensionValidator(['docx', 'doc'])], verbose_name='doc листа'),
        ),
    ]
