# Generated by Django 4.0.4 on 2022-04-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]