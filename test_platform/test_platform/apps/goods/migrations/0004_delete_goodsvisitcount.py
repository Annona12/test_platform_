# Generated by Django 4.2.7 on 2023-12-09 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_goodsvisitcount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GoodsVisitCount',
        ),
    ]
