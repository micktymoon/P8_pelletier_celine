# Generated by Django 3.1.5 on 2021-06-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210215_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutri_score',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
