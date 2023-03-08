from app import app
from model.user_models import user_model
from model.auth_model import auth_model
from flask import request,send_file
from datetime import datetime
obj = user_model()
auth = auth_model()

@app.route("/user/getall")
@auth.token_auth()
def user_getall_controller():
    return obj.user_getall_model()


@app.route("/user/addone",methods=['POST'])
@auth.token_auth()
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/update",methods=['PUT'])
def user_update_controller():
    return obj.user_update_model(request.form)

@app.route("/user/delete/<id>",methods=['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route("/user/patch/<id>",methods=['PATCH'])
def user_patch_controller(id):
    
    return obj.user_patch_model(request.form,id)

@app.route("/user/getall/limit/<limit>/page/<pageno>",methods=['GET'])
def user_pagination_controller(limit,pageno):
    return obj.user_pagination_model(limit,pageno)

@app.route("/user/<uid>/upload/avatar",methods=['PUT'])
def user_upload_avatar_controller(uid):
    file=request.files['avatar']
    #file.save(f"uploads/{file.filename}")
    uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    file_list= str(file.filename).split(".")
    file_ext= file_list[len(file_list)-1]
    uniquefilename= f"image_{uniqueFileName}.{file_ext}"
    filepath= f"uploads/{uniquefilename}"
    file.save(filepath)
    return obj.user_upload_avatar_model(uid,filepath)

@app.route('/uploads/<filename>')
def fetch_uploaded_file(filename):
    return send_file(f"uploads/{filename}")


@app.route("/user/login",methods=['POST'])
def user_login_controller():
    
    return obj.user_login_model(request.form)
