# Generated by Django 4.1.5 on 2023-01-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peace', '0007_rename_firstname_akatsukiteam_fname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akatsukiteam',
            name='place',
            field=models.CharField(max_length=30),
        ),
    ]
