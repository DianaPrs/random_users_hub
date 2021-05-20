schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "gender": {"type": "string"},
        "name": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "first": {"type": "string"},
                "last": {"type": "string"},
            },
            "required": ["title", "first", "last"],
        },
        "location": {
            "type": "object",
            "properties": {
                "street": {
                    "type": "object",
                    "properties": {
                        "number": {"type": "integer"},
                        "name": {"type": "string"},
                    },
                    "required": ["number", "name"],
                },
                "city": {"type": "string"},
                "country": {"type": "string"},
            },
            "required": ["street", "city", "country"],
        },
        "email": {"type": "string", "format": "email"},
        "cell": {"type": "string", "pattern": "[0-9()\-\.\s]+$"},
        "picture": {
            "type": "object",
            "properties": {
                "large": {"type": "string"},
                "medium": {"type": "string"},
                "thumbnail": {"type": "string"},
            },
            "required": ["large", "medium", "thumbnail"],
        },
    },
    "required": ["gender", "name", "location", "email", "cell", "picture"],
}
