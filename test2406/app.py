from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__, static_folder='static')

# Function to connect to SQLite database
def connect_db():
    conn = sqlite3.connect('clinic.db')
    return conn

# Route to serve HTML page for appointment form
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to fetch all appointments
@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()
    conn.close()
    return jsonify(appointments)

# API endpoint to create a new appointment
@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    patient_name = data['patient_name']
    appointment_date = data['appointment_date']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (patient_name, appointment_date) VALUES (?, ?)', (patient_name, appointment_date))
    conn.commit()

    # Fetch the newly inserted appointment for receipt
    cursor.execute('SELECT * FROM appointments WHERE patient_name = ? AND appointment_date = ?', (patient_name, appointment_date))
    appointment = cursor.fetchone()

    conn.close()

    return jsonify({
        'message': 'Appointment created successfully',
        'appointment': {
            'patient_name': appointment[1],
            'appointment_date': appointment[2]
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
