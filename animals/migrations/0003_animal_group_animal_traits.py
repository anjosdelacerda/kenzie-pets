# Generated by Django 4.1.2 on 2022-10-11 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0004_remove_group_animals"),
        ("traits", "0003_remove_trait_animals"),
        ("animals", "0002_rename_weigth_animal_weight"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="animals",
                to="groups.group",
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="traits",
            field=models.ManyToManyField(related_name="traits", to="traits.trait"),
        ),
    ]
