# Generated by Django 5.0.4 on 2024-05-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_review_email_review_name_alter_review_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
