from helpers.mongoConnection import *
from helpers.checking import *
from bson import ObjectId

def insert_user(obj):
    if not check_params(obj,["user","group","message"]):
        return {"response":400,"message":"Bad Request: 'user' and 'group' are obligatory parameters"}
    q = {"user":obj["user"]}
    if check_exists(q,"users"):
        return {"response":400,"message":"Bad Request: there is already a user with that name"}
    res = write_coll("users",obj)
    return res.inserted_id

def list_users():
    res = read_coll("users",{})
    response = {c["user"]:str(c["_id"]) for c in res}
    return response

def list_groups():
    res = read_coll("users",{})
    response = {c["group"] for c in res}
    return response

def list_messsages():
    res = read_coll("users",{})
    response = {c["message"] for c in res}
    return response

def get_user(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"users"):
        return {"response":400,"message":"Bad Request: user with given group does not exist"}
    return read_coll("users",q)

def delete_user(obj):
    '''Function in which the endpoint delete/user will be based'''

    if not check_params(obj,["user"]):
        return {"message":"Bad Request: 'user' is an obligatory parameter"}
    q = {"user":obj["user"]}
    if not check_exists(q,"users"):
        return {"message":"Bad Request: user with given id does not exist"}
    res = delete_coll("user",obj)
    return {"response":200,"user":"User successfully deleted"}


def get_message(obj):
    if not check_params(obj,["message"]):
        return {"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"messages"):
        return {"message":"Bad Request: user with given id does not exist"}
    return read_coll("users",q)