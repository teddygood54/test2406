// scripts.js

// Function to handle form submission
async function submitForm() {
    const patientName = document.getElementById('patientName').value;
    const appointmentDate = document.getElementById('appointmentDate').value;

    try {
        const response = await axios.post('/api/appointments', {
            patient_name: patientName,
            appointment_date: appointmentDate
        });

        const appointment = response.data.appointment;
        displayReceipt(appointment);
    } catch (error) {
        console.error('Error creating appointment:', error);
    }
}

// Function to display appointment receipt
function displayReceipt(appointment) {
    document.getElementById('receiptPatientName').textContent = appointment.patient_name;
    document.getElementById('receiptAppointmentDate').textContent = appointment.appointment_date;

    // Show the receipt container and hide the form
    document.getElementById('appointmentForm').style.display = 'none';
    document.getElementById('receiptContainer').style.display = 'block';
}
