# Generated by Django 3.2.9 on 2021-11-23 14:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_skill_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
