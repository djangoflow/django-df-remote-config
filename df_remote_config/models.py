from django.db import models

from df_remote_config.schema import CONFIG_SCHEMA_MAP


class JSONSchema(models.Model):
    name = models.CharField(max_length=255, unique=True)
    schema = models.JSONField()


class ConfigItem(models.Model):
    DEFAULT_NAME = "default"

    name = models.CharField(max_length=255, default=DEFAULT_NAME)
    schema_name = models.CharField(max_length=255)
    json = models.JSONField()

    def get_schema(self) -> dict:
        try:
            return JSONSchema.objects.get(name=self.schema_name).schema
        except JSONSchema.DoesNotExist:
            return CONFIG_SCHEMA_MAP[self.schema_name]
