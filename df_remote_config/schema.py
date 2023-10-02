legal_schema = {
    "type": "object",
    "properties": {
        "terms_of_service": {"type": "string"},
        "privacy_policy": {"type": "string"},
    },
    "required": ["terms_of_service", "privacy_policy"],
}

DEFAULT_SCHEMA = {
    "type": "object",
    "properties": {},
    "required": [],
    "additionalProperties": True,
}
