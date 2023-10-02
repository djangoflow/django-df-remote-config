from typing import Optional

from django.db import models
from django.utils.module_loading import import_string

from df_remote_config.fields import NoMigrationsChoicesField
from df_remote_config.settings import api_settings


class ConfigTag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class ConfigPart(models.Model):
    name = NoMigrationsChoicesField(
        max_length=255, choices=[(part, part) for part in api_settings.PARTS]
    )
    sequence = models.PositiveIntegerField(default=1000)
    tags = models.ManyToManyField(ConfigTag, blank=True)
    json = models.JSONField(blank=True, default=dict)

    def __str__(self) -> str:
        return f"ConfigPart<{self.id}>: {self.name}"

    def get_schema(self) -> Optional[dict]:
        if schema_path := api_settings.PARTS[self.name].get("SCHEMA"):
            return import_string(schema_path)
        return None


#
#
# def get_schema_by_name(name: str) -> dict:
#     try:
#         return JSONSchema.objects.get(name=name).schema
#     except JSONSchema.DoesNotExist:
#         return CONFIG_SCHEMA_MAP[name]
