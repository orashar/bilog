# Generated by Django 3.1.4 on 2021-02-01 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thebilog', '0003_auto_20210129_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]
