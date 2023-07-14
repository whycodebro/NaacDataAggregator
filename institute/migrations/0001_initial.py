# Generated by Django 3.2.5 on 2022-11-17 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginandregister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('prog_id', models.IntegerField(primary_key=True, serialize=False)),
                ('prog_code', models.CharField(max_length=30)),
                ('prog_name', models.CharField(max_length=50)),
                ('prog_type', models.CharField(max_length=20)),
                ('year_of_intro', models.IntegerField(null=True)),
                ('year_of_implementation', models.IntegerField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('cbcs_ecs_status', models.CharField(max_length=10)),
                ('cbcs_ecs_year_implementation', models.IntegerField(null=True)),
                ('prog_head_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loginandregister.alluser')),
            ],
        ),
    ]