# Generated by Django 3.0.5 on 2020-05-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200420_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
