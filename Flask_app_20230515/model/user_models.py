import mysql.connector
#import json
from flask import make_response
from  datetime import datetime, timedelta
import jwt
from config.config import dbconfig
class user_model():
    
    def DB_connection():
        conn= mysql.connector.connect(host=dbconfig['hostname'],username=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'],port=dbconfig['port'])
        conn.autocommit=True
        cur = conn.cursor(dictionary=True)
        return conn,cur
    def DB_close(conn,cur):
        cur.close()
        conn.close()
        
    def user_getall_model(self):
        conn,cur= self.DB_connection()
        cur.execute("select * from flask_tutorial.user_details")
        result= cur.fetchall()
        self.DB_close(conn,cur)
        if len(result)>0:
            res= make_response({'message':result},200)
            res.headers['Access-Control-Allow-Origin']='*'
            return res
            #return json.dumps(result)
        else:
            return make_response({'message':"No Records found"},204)
        
    def user_addone_model(self,data):
      conn,cur= self.DB_connection()
      cur.execute(f"insert into flask_tutorial.user_details(name,email,phone,role,password) values ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
      self.DB_close(conn,cur)
      #print(data['email'])
      return make_response({'message':"user created successfully"},201)
    
    def user_update_model(self,data):
      conn,cur= self.DB_connection()
      cur.execute(f"update flask_tutorial.user_details set name ='{data['name']}',email ='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' where id={data['id']}")
      
      if cur.rowcount>0:
          self.DB_close(conn,cur)
          return make_response({'message':"user updated successfully"},201)
      else:
          return make_response({'message':"not updated"},204)
      
      
    def user_delete_model(self,id):
      conn,cur= self.DB_connection()
      cur.execute(f"delete from flask_tutorial.user_details  where id={id}")
      if cur.rowcount>0:
        self.DB_close(conn,cur)
        return make_response({'message':"user deleted successfully"},200)
        
      else:
         return make_response({'message':"not deleted"},204)
      
    

    def user_patch_model(self,data,id):
        
        conn,cur= self.DB_connection()
        query = "update flask_tutorial.user_details set"
        #print(data)
        for key in data:
            query = query +f" {key}='{data[key]}',"
        query= query[0:-1] +f" where id = {id}"    
        cur.execute(query)
        if cur.rowcount>0:
            return make_response({'message':"user updated successfully"},201)
            self.DB_close(conn,cur)
        else:
            return make_response({'message':"not updated"},204)
        
                
    def user_pagination_model(self,limit,pageno):
        limit= int(limit)
        pageno = int(pageno)
        rownum= (limit*pageno) -limit
        conn,cur= self.DB_connection()
        query= f"select * from flask_tutorial.user_details LIMIT {rownum},{limit}"
        print(query)
        #return make_response({'message':"user pagenation"},201)
        self.cur.execute(query)
        result=self.cur.fetchall()
        #print(result)
        if len(result)>0:
            res= make_response({"pageno":pageno,"limit":limit,'message':result},200)
            res.headers['Access-Control-Allow-Origin']='*'
            self.DB_close(conn,cur)
            return res
            #return json.dumps(result)
        else:
            return make_response({'message':"No Records found"},204)
        

    def user_upload_avatar_model(self,uid,filepath):
        conn,cur= self.DB_connection()
        cur.execute(f"Update flask_tutorial.user_details set avatar='{filepath}' where id = {uid}")
        if cur.rowcount>0:
            self.DB_close(conn,cur)
            return make_response({'message':"file uploaded successfully"},201)
        else:
            return make_response({'message':"not updated"},204)

    def user_login_model(self,data):
        conn,cur= self.DB_connection()
        cur.execute(f"select id,name,phone,avatar,role_id from flask_tutorial.user_details where email='{data['email']}'and password='{data['password']}' ")
        result = self.cur.fetchall()
        self.DB_close(conn,cur)
        userdata = result[0]
        exp_time = datetime.now() + timedelta(minutes=60)
        exp_epoc_time= int(exp_time.timestamp())
        payload = {
            "payload": userdata,
            "exp":exp_epoc_time,
        }
        jw_token=jwt.encode(payload,"SECRET",algorithm="HS256")
        return make_response({"token":jw_token},200)