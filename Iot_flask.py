from flask import Flask,render_template,redirect,request,jsonify
import datetime
import sqlite3
app = Flask(__name__)


insertQuery='INSERT INTO datas(Id,Model,HW,SW,Device_Name) VALUES(%s,%s,%s,%s,%s)'
fetchQuery='SELECT * from datas'
deleteQuery="""DELETE from datas where _id = ? """
particular_id = 'SELECT * FROM datas WHERE _id = ?'
dbfilename="Iot.db"

def welcome_msg():
    return "Flask Working fine -- welcome"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dash.html")
def dashboard():
    conn=sqlite3.connect("Iot.db")
    cursor=conn.cursor()
    cursor.execute(fetchQuery)
    receivedData=cursor.fetchall()
    return render_template("dash.html",Result=receivedData)

@app.route("/form.html")
def form():
    return render_template("form.html")



@app.route("/form_advanced.html",methods=['GET'])
def Dev_details():
    print("hello...")
    conn = sqlite3.connect("Iot.db")
    cursor = conn.cursor()
    _id = request.args.get('_id')
    print(_id)  # Assuming _id is passed as a parameter
    cursor.execute(particular_id, (_id,))
    receivedData = cursor.fetchall()
    return render_template("form_advanced.html", Result=receivedData)



def Createtable():
    Createtablequery="""CREATE TABLE IF NOT EXISTS "datas" (
                "Id" TEXT NOT NULL,
                "Model" TEXT NOT NULL,
                "HW" TEXT NOT NULL,
                "SW" TEXT NOT NULL,
                "Device_Name" TEXT NOT NULL,
                "_id" INTEGER NOT NULL, PRIMARY KEY("_id" AUTOINCREMENT)
                );
                """
   
    conn=sqlite3.connect("Iot.db")
    cursor=conn.cursor()
    cursor.execute(Createtablequery)
    conn.commit()
    conn.close()

@app.route("/insertdata", methods=['POST'])
def insert():
    try:
        data = request.form
        ID1 = data.get("id")
        Model1 = data.get("model")
        HW1 = data.get("hw_version")
        SW1 = data.get("sw_version")
        Device_Name1 = data.get("device_name")

        conn = sqlite3.connect("Iot.db")
        cursor = conn.cursor()

        insertQuery = 'INSERT INTO datas (Id, Model, HW, SW, Device_Name) VALUES (?, ?, ?, ?, ?)'
        cursor.execute(insertQuery, (ID1, Model1, HW1, SW1, Device_Name1))

        conn.commit()
        conn.close()

        return jsonify({"message": "Successfully inserted"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route("/insertdata",methods=['POST'])
def Fetch_all():
    con=sqlite3.connect("Iot.db")
    cursor=conn.cursor()
    cursor.execute(fetchQuery)
    receivedData=c.fetchall()
    return render_template("dash.html",results=receivedData)

@app.route("/deletedata", methods=['POST'])
def delete_record():
    try:
        ID = request.form["_id"]
        conn = sqlite3.connect("Iot.db")
        cursor = conn.cursor()
        print("SQL Query:",deleteQuery)
        cursor.execute(deleteQuery, (ID,))
        conn.commit()
        cursor.close()
        conn.close()
        return "Successfully deleted"

    except Exception as e:
        print("Exception:", str(e))
        return "An error occurred", 500

@app.route("/refresh")
def refresh():
    print("hii python")
    conn=sqlite3.connect("Iot.db")
    cursor=conn.cursor()
    cursor.execute(fetchQuery)
    receivedData=cursor.fetchall()
    #print(receivedData)
    data=[]
    for rows in receivedData:
        data.append({
        'id':rows[0],
        'Model':rows[1],
        'hw_version':rows[2],
        'sw_version':rows[3],
        'device_name':rows[4],
        '_Id':rows[5],
        })
    
    return jsonify(data)

if __name__ == "__main__":

    Createtable()
    
    app.run(host="0.0.0.0",debug=True)