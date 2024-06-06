import json
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/sign', methods=['POST'])
def sign():
    name = request.form['nm']
    age = request.form['age']
    gender = request.form['gen']
    employee_ID = request.form['EI']
    password = request.form['pwd']
    
    form_data = {
        'Name': name,
        'Age': age,
        'Gender': gender,
        'Employee ID': employee_ID,
        'Password': password  
    }
        
    with open('biodata.txt', 'a') as file:
        file.write(json.dumps(form_data) + '\n')
    return 'Thank you'

@app.route('/login', methods=['POST'])
def login():
    employee_ID = request.form['EI']
    password = request.form['pwd']
    
    with open('biodata.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
               continue
            user = json.loads(line)
            if user['Employee ID'] == employee_ID and user['Password'] == password:
                return render_template('welcome.html', user=user)
    return 'Invalid credentials'

if __name__ == '__main__':
    app.run(debug=True)
