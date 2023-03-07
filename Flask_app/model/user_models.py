import mysql.connector
#import json
from flask import make_response
from  datetime import datetime, timedelta
import jwt
class user_model():
    def __init__(self):
        ##connection establishment code
        try:
            self.conn= mysql.connector.connect(host='localhost',username='sujan',password='harika123',database='groc_store',port=3306)
            self.conn.autocommit=True
            self.cur = self.conn.cursor(dictionary=True)
            print("Connection successful!!!")
        except:
            print("Connection Failed")
    def user_getall_model(self):
        self.cur.execute("select * from flask_tutorial.user_details")
        result=self.cur.fetchall()
        #print(result)
        if len(result)>0:
            res= make_response({'message':result},200)
            res.headers['Access-Control-Allow-Origin']='*'
            return res
            #return json.dumps(result)
        else:
            return make_response({'message':"No Records found"},204)
        
    def user_addone_model(self,data):
      self.cur.execute(f"insert into flask_tutorial.user_details(name,email,phone,role,password) values ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
      
      #print(data['email'])
      return make_response({'message':"user created successfully"},201)
    
    def user_update_model(self,data):
      self.cur.execute(f"update flask_tutorial.user_details set name ='{data['name']}',email ='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' where id={data['id']}")
      if self.cur.rowcount>0:
          return make_response({'message':"user updated successfully"},201)
      else:
          return make_response({'message':"not updated"},204)
      
    def user_delete_model(self,id):
      self.cur.execute(f"delete from flask_tutorial.user_details  where id={id}")
      if self.cur.rowcount>0:
          return make_response({'message':"user deleted successfully"},200)
      else:
          return make_response({'message':"not deleted"},204)
    

    def user_patch_model(self,data,id):
        query = "update flask_tutorial.user_details set"
        #print(data)
        for key in data:
            query = query +f" {key}='{data[key]}',"
        query= query[0:-1] +f" where id = {id}"    
        self.cur.execute(query)
        if self.cur.rowcount>0:
            return make_response({'message':"user updated successfully"},201)
        else:
            return make_response({'message':"not updated"},204)
                
    def user_pagination_model(self,limit,pageno):
        limit= int(limit)
        pageno = int(pageno)
        rownum= (limit*pageno) -limit
        query= f"select * from flask_tutorial.user_details LIMIT {rownum},{limit}"
        print(query)
        #return make_response({'message':"user pagenation"},201)
        self.cur.execute(query)
        result=self.cur.fetchall()
        #print(result)
        if len(result)>0:
            res= make_response({"pageno":pageno,"limit":limit,'message':result},200)
            res.headers['Access-Control-Allow-Origin']='*'
            return res
            #return json.dumps(result)
        else:
            return make_response({'message':"No Records found"},204)

    def user_upload_avatar_model(self,uid,filepath):
        self.cur.execute(f"Update flask_tutorial.user_details set avatar='{filepath}' where id = {uid}")
        if self.cur.rowcount>0:
            return make_response({'message':"file uploaded successfully"},201)
        else:
            return make_response({'message':"not updated"},204)

    def user_login_model(self,data):
        self.cur.execute(f"select id,name,phone,avatar,role_id from flask_tutorial.user_details where email='{data['email']}'and password='{data['password']}' ")
        result = self.cur.fetchall()
        userdata = result[0]
        exp_time = datetime.now() + timedelta(minutes=60)
        exp_epoc_time= int(exp_time.timestamp())
        payload = {
            "payload": userdata,
            "exp":exp_epoc_time,
        }
        jw_token=jwt.encode(payload,"SECRET",algorithm="HS256")
        return make_response({"token":jw_token},200)