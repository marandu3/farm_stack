#the purpose of serializer is to convert from one format to another example to convert from JSON format to dictionary

def convertdata(user)->dict:
    return {
        'id':str (user["_id"]),
        'username': str(user["username"])
    }

def convertdatas(users)->list[dict]:
    return [convertdata(user) for user in users]