# Generated by Django 4.2 on 2023-05-12 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_options_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
    ]
