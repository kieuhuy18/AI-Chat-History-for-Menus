from bson import ObjectId

def serialize_mongo(doc: dict):
    doc["_id"] = str(doc["_id"])
    return doc
