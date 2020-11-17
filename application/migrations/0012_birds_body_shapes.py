# Generated by Django 3.1.2 on 2020-11-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_birds_bill_shapes'),
    ]

    operations = [
        migrations.CreateModel(
            name='birds_body_shapes',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('body_shape', models.CharField(default='NULL', max_length=25, null=True)),
                ('body_example', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
        ),
    ]
