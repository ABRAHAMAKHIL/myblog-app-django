# Generated by Django 3.0.5 on 2020-04-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_delete_gc_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(upload_to='pics/%y/%m/%d/'),
        ),
    ]
