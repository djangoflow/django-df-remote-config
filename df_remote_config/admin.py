from django.contrib import admin

from df_remote_config.models import ConfigItem, JSONSchema


@admin.register(JSONSchema)
class JSONSchemaAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ConfigItem)
class ConfigItemAdmin(admin.ModelAdmin):
    list_display = ("name", "schema_name")
