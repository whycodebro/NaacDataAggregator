# Generated by Django 3.2.5 on 2023-05-01 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0007_e_governance_e_library_resource_extension_activity_award_funds_grants_to_inst_hei_guidence_activity_'),
        ('student', '0002_student_collaborative_activity_participation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='prog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institute.program'),
        ),
    ]
