# Generated by Django 3.1.2 on 2020-11-17 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_conservation_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='birds',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('scientific_name', models.CharField(blank=True, default='NULL', max_length=100, null=True, unique=True)),
                ('common_name', models.CharField(blank=True, default='NULL', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.birds_bill_shapes')),
                ('body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.birds_body_shapes')),
                ('conservation_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.conservation_status')),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.bird_families')),
                ('wing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.birds_wing_shapes')),
            ],
        ),
    ]
