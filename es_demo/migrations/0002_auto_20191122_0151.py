# Generated by Django 2.2.7 on 2019-11-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('es_demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=1000)),
                ('birthday', models.DateField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='SKU',
        ),
    ]
