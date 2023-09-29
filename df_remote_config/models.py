from django.db import models

from df_remote_config.schema import CONFIG_SCHEMA_MAP


class ConfigTag(models.Model):
    name = models.CharField(max_lenght=255, unique=True)


class ConfigPart(models.Model):
    schema = models.CharField()
    sequence = models.SmallInteger()
    tags = models.Many2Many(ConfigTag, blank=True)
    json = models.JSONField()

    def get_schema(self) -> dict:
        return get_schema_by_name(self.schema_name)


def get_schema_by_name(name: str) -> dict:
    try:
        return JSONSchema.objects.get(name=name).schema
    except JSONSchema.DoesNotExist:
        return CONFIG_SCHEMA_MAP[name]
