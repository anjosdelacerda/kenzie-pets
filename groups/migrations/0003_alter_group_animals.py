# Generated by Django 4.1.2 on 2022-10-11 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0002_rename_weigth_animal_weight"),
        ("groups", "0002_group_animals"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="animals",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group",
                to="animals.animal",
            ),
        ),
    ]
