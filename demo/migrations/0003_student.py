# Generated by Django 3.2.7 on 2021-09-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.CharField(max_length=50)),
                ('s_name', models.CharField(max_length=100)),
                ('s_percentage', models.FloatField()),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
