import mysql.connector
#import json
from flask import make_response,request
import re
import jwt
import json
from  functools import wraps
from config.config import dbconfig
class auth_model():
    def __init__(self):
        ##connection establishment code
        try:
            self.conn= mysql.connector.connect(host=dbconfig['hostname'],username=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'],port=dbconfig['port'])
            self.conn.autocommit=True
            self.cur = self.conn.cursor(dictionary=True)
            print("Connection successful!!!")
        except:
            print("Some error")

    
    def token_auth(self,endpoint=""):
        def inner1(func):
            @wraps(func)
            def inner2(*args):
                endpoint =request.url_rule
                print(endpoint)
                autherization = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+) *$",autherization,flags=0):
                    token= split_auth=autherization.split(" ")[1]
                    try:
                       jwt_decoded=jwt.decode(token,"SECRET",algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR":"TOKEN_EXPIRED"},401)
                    role_id=jwt_decoded['payload']['role_id']
                    self.cur.execute(f"select roles from flask_tutorial.accesibility_view where endpoint='{endpoint}' ")
                    result = self.cur.fetchall()
                    if len(result)>0:
                        allowed_roles= json.loads(result[0]['roles'])
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                            return make_response({"ERROR":"NOT_AUTHERIZED"},404)
                    else:
                        return make_response({"ERROR":"UNKNOWN_ENDPOINT"},404)
                else:
                    return make_response({"ERROR":"INVALID_TOKEN"},401)
            return inner2
        return inner1