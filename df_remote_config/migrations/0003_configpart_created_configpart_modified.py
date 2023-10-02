# Generated by Django 4.2.5 on 2023-10-02 14:11

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ("df_remote_config", "0002_configattribute_alter_configpart_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="configpart",
            name="created",
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="created",
            ),
        ),
        migrations.AddField(
            model_name="configpart",
            name="modified",
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="modified",
            ),
        ),
    ]
