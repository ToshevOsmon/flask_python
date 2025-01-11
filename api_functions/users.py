import sqlite3
from flask import request, jsonify
import env_vars1


def user_register():

    chat_id = request.json.get("chat_id")
    if not chat_id or chat_id == None:
        return jsonify({"Errorjon:" : "Chat ID topilmadi", "status" : "error" }), 400
    name = request.json.get("name","Xoji aka")
    username = request.json.get("username",name)

    with sqlite3.connect(env_vars1.DB_NAME) as conn:
        cursor=conn.cursor()
        cursor.execute('INSERT INTO users (chat_id, name, username) VALUES (?, ?, ?)',(chat_id, name, username))
        conn.commit()
    return jsonify({"message": "User registered successfully", "status":"success"}), 200

def user_list():

    with sqlite3.connect(env_vars1.DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        user_list=[]
        for user in cursor.fetchall():
           user_list.append({
               "id":user[0],
               "chat_id":user[1],
               "name":user[2],
               "username":user[3],
               "created_at":user[4]
           })
    return jsonify({f"users": user_list, "status":"success"}), 201

def delete_user():
    chat_id = request.json.get("chat_id")
    if not chat_id or chat_id == None:
        return jsonify({"Errorjon:" : "Chat ID topilmadi", "status" : "error" }), 400
    with sqlite3.connect(env_vars1.DB_NAME) as conn:
        cursor = conn.cursor()    
        cursor.execute('SELECT id FROM users WHERE chat_id= ?',(chat_id,))
        user_id = cursor.fetchone()
        if not user_id:
            return jsonify({"Error" : "Chat ID bo'yicha ID topilmadi"}),404
        cursor.execute('DELETE FROM users WHERE chat_id = ?', (chat_id,))
        conn.commit()
    return jsonify({"message":"User deleted successfully","status":"success"}), 203              




