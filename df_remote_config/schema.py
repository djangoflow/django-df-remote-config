legal_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "terms_of_service": {"type": "string"},
        "privacy_policy": {"type": "string"},
    },
    "required": ["terms_of_service", "privacy_policy"],
}
