# Generated by Django 2.1.4 on 2019-01-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory_count', models.IntegerField()),
                ('genre', models.TextField()),
            ],
        ),
    ]
