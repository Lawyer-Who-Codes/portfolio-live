# Generated by Django 3.2.9 on 2021-12-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(default='django.png', null=True, upload_to=''),
        ),
    ]
