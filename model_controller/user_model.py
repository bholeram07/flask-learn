import mysql.connector
from flask import make_response
class get_all_model():
        def __init__(self):
            try:
             self.con=mysql.connector.connect(host='localhost',user='root',password='12345678',database='bank')
             self.cur=self.con.cursor(dictionary=True)
             self.con.autocommit=True
             print("connection successful")
            except:
               print('some error')
        def get_all(self):
          self.cur.execute("Select * from customer")
          result=self.cur.fetchall()
          if len(result):
               return make_response({"list": result},200)
          else:
              return make_response({"message":"No data to appear"},204)
               
         
        
        def add_one(self,data):
            self.cur.execute(f"INSERT INTO customer (customer_id,first_name,middle_name,last_name,city,mobile_no,occupation,date_of_birth) VALUES ('{data['customer_id']}','{data['first_name']}','{data['middle_name']}','{data['last_name']}','{data['city']}','{data['mobile_no']}','{data['occupation']}','{data['date_of_birth']}')")
            return make_response({"message":"User created Successfully"},201)
    

        def update_one(self,data):
             self.cur.execute(f"UPDATE customer SET first_name='{data['first_name']}',middle_name='{data['middle_name']}',last_name='{data['last_name']}',city='{data['city']}',mobile_no='{data['mobile_no']}',occupation='{data['occupation']}',date_of_birth='{data['date_of_birth']}' where customer_id={data['customer_id']}")
             if self.cur.rowcount>0:
                return make_response({"message":"User Updated Successfully"},204)
             else:
                return make_response({"message": "Nothing to Update"},202)
    
        
        def delete_user(self,id):
            self.cur.execute(f"Delete from customer where customer_id ={id}")
            if self.cur.rowcount>0:
                return make_response({"message":"User Deleted Successfully"},200)
            else:
                return make_response({"message":"Nothing to delete"},204)

