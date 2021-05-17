schema = {
    "results": {
        "type": "object",
        "properties": {
            "name": {"type": "object",
                     "properties": {"first": {"type": "string"}, "last": {"type": "string"}},
                     "required": ["first", "last"]},
            "cell": {"type": "string", "pattern": "[0-9()\-\.\s]+$"},
            "gender": {"type": "string"},
            "email": {"type": "string", "format": "email"},
            "location": {"type": "object",
                         "properties": {'street': {"type": "object",
                                                   "properties": {"name": {"type": "string"}},
                                                   "required": ["name"],
                                        "city": {"type": "string"},
                                        "country": {"type": "string"}},
                         "required": ["street", "city", "country"]}},
            "picture": {"type": "object",
                        "properties": {"large": {"type": "string"}, "thumbnail": {"type": "string"}},
                        "required": ["large", "thumbnail"]},
        "required": ["name", "cell", "gender", "email", "location", "picture"]
        }
    }
}