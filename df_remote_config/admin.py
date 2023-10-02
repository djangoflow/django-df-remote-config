from typing import Optional

from django.contrib import admin
from django.http import HttpRequest
from jsoneditor.forms import JSONEditor

from df_remote_config.models import ConfigPart, ConfigTag
from df_remote_config.schema import DEFAULT_SCHEMA


@admin.register(ConfigTag)
class ConfigTagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ConfigPart)
class ConfigPartAdmin(admin.ModelAdmin):
    list_display = ("name", "tags_", "sequence")

    def tags_(self, obj: ConfigPart) -> str:
        return ", ".join([tag.name for tag in obj.tags.all()])

    def get_readonly_fields(
        self, request: HttpRequest, obj: Optional[ConfigPart] = None
    ) -> list[str]:
        if obj:
            return ["name"]
        else:
            return []

    def get_form(self, request, obj=None, **kwargs):  # type: ignore
        form = super().get_form(request, obj, **kwargs)
        if not obj:
            form.base_fields.pop("json", None)
        else:
            form.base_fields["json"].widget = JSONEditor(
                jsonschema=obj.get_schema() or DEFAULT_SCHEMA
            )
        return form
