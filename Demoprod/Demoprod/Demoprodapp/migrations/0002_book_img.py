# Generated by Django 4.1.3 on 2022-11-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demoprodapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default=123, upload_to='gallery'),
            preserve_default=False,
        ),
    ]