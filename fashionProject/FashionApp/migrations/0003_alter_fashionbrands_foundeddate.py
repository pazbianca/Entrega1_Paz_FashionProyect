# Generated by Django 4.0.4 on 2022-06-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FashionApp', '0002_rename_founded_fashionbrands_foundeddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashionbrands',
            name='foundedDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]