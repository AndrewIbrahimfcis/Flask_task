from os import name, stat
from flask import Flask, render_template, request,jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'database'

mysql = MySQL(app)

#creating table of customers
#CREATE TABLE MyUsers ( customer_id int NOT NULL,Name VARCHAR(30) NOT NULL,address char(50),city char(50),state char(25),zip_code char(10));

#An endpoint to add new customer.

@app.route('/Customer',methods=['POST'])
def Add_CustomerInfo():
    id = request.json['id']
    Name = request.json['name']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Customer(customer_id,Name,address,city,state,zipcode) VALUES (%s,%s)", (id,Name,address,city,state,zipcode))
    mysql.connection.commit()
    cur.close()
    return 'successfully Added'


#get all customers for test

@app.route('/Customer', methods=['GET'])
def Get_AllCustomersInfo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from Customer")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


#An endpoint to get customer.

@app.route('/Customer/<id>', methods=['GET'])
def Get_CustomerInfo(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from Customer WHERE id = (%s)", (id))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


#An endpoint to update customer

@app.route('/Customer/<id>', methods=['PUT'])
def update_CustomerInfo(id):
    Name = request.json['name']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    cur = mysql.connection.cursor()
    name = request.json['name']
    cur.execute("UPDATE Customer SET  name = (%s) ,address=(%s),city=(%s),state=(%s),zipcode=(%s) WHERE id = (%s)", (Name,address,city,state,zipcode,id))
    mysql.connection.commit()
    cur.close()
    return "Updated successfully"

#An endpoint to delete customer

@app.route('/Customer/<id>', methods=['DELETE'])
def Delete_CustomerInfo(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Customer WHERE id = (%s);", (id))
    mysql.connection.commit()
    cur.close()
    return "successfully deleted"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')