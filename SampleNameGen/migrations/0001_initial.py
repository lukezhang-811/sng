# Generated by Django 4.2.11 on 2024-05-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('sample_id', models.TextField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('technology', models.CharField(max_length=100)),
                ('storage_type', models.CharField(max_length=100)),
                ('tissue_type', models.CharField(max_length=100)),
                ('sample_name', models.IntegerField()),
                ('origin', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
                ('replicate', models.CharField(max_length=100)),
            ],
        ),
    ]
