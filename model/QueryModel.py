import mysql.connector
import json
from flask import make_response

#create table lola (name varchar(100),sal varchar(200)) 
#INSERT INTO lola(name,sal) VALUES ('saurav','50000')
class QueryModel():
    def __init__(self):
        #constructor 
        try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="Lola@121")
            self.conn.autocommit=True 
            self.cur=self.conn.cursor(dictionary=True)
            self.conn.autocommit=True
            self.cur=self.conn.cursor(dictionary=True)
            print("Connection Is SuccessFull")
        except Exception as e:
            print('some error in connection')
            print(e)
    def openCursor(self):
        self.cur=self.conn.cursor(dictionary=True) 
    def closeCursor(self):
        self.cur.close()        
    def ExecuteQuery(self,data):
        self.openCursor()
        print("request",data)
        result=[]
        error=""
        rowcount=0
        try:
            self.cur.execute("use "+data['database'])
            self.cur.execute(data['query'])
            rowcount=self.cur.rowcount
            result=self.cur.fetchall()
            print(result)
        except Exception as e:
            print('some error')
            print(e)
            error=e
        finally:
            self.closeCursor()
        json.dumps(result)
        errr={"error_message": str(error)}
        json.dumps(errr)
        res=make_response({"result": result,"message":"","rowcount":rowcount,"error":errr},200)
        res.headers['Access-Control-Allow-Origin']="*"
        return res

    def CreateNewDatabase(self,data):
        self.openCursor()
        result=[]
        error=""
        try:
            self.cur.execute("CREATE DATABASE "+data['database'])
        except Exception as e:
            print('some error')
            print(e)
            error=e
        finally:
            self.closeCursor()    

        json.dumps(result)
        errr={"error_message": str(error)}
        json.dumps(errr)
        res=make_response({"result": result,"message":"Schema Created Successfully ! ","error":errr},200)
        res.headers['Access-Control-Allow-Origin']="*"
        return res
    def GetAllDatabase(self):
        self.openCursor()
       
        result=[]
        error=""
        try:
            
            self.cur.execute("SHOW DATABASES")
            print("self cur")
            print(self.cur)
            result=self.cur.fetchall()
            print(result)
        except Exception as e:
            print('some error')
            print(e)
            error=e
        finally:
            self.closeCursor()    

        json.dumps(result)
        errr={"error_message": str(error)}
        json.dumps(errr)
        res=make_response({"result": result,"message":"","error":errr},200)
        res.headers['Access-Control-Allow-Origin']="*"
        return res    
    