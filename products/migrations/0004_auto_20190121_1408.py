# Generated by Django 2.1.4 on 2019-01-21 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='products.Item'),
        ),
    ]
