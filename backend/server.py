from flask import Flask,request
from attendance import Attendance,Session
import time 
import threading

session = Session("Session 1")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add_attendance',methods = ["POST"])
def add_attendance():
    format = {
        "name":str,
        "group":list
    }
    data = request.get_json()
    if not data:
        return {"error":"No data provided"}
    name = data[name]
    group = data[group]
    session.add_attendance(Attendance(name,group))
    return {"message":"Attendance added"}

def mark_attendance_periodically():
    while True:
        session.mark_attendances()
        time.sleep(300) 

if __name__ == '__main__':
    thread = threading.Thread(target=mark_attendance_periodically, daemon=True)
    thread.start()
    app.run()
