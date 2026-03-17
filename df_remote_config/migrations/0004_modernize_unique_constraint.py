from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("df_remote_config", "0003_configpart_created_configpart_modified"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="configattribute",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="configattribute",
            constraint=models.UniqueConstraint(
                fields=["name", "value"],
                name="configattribute_name_value_uniq",
            ),
        ),
    ]
