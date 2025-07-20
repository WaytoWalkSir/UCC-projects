import uuid
import datetime

# Base Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Patient class
class Patient(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.patient_id = str(uuid.uuid4())[:8]

# Doctor class
class Doctor(Person):
    def __init__(self, name, specialty, schedule):
        super().__init__(name, None, None)
        self.doctor_id = str(uuid.uuid4())[:8]
        self.specialty = specialty
        self.schedule = schedule  # List of available datetime strings

# Appointment class
class Appointment:
    def __init__(self, patient_id, doctor_id, appointment_time):
        self.appointment_id = str(uuid.uuid4())[:8]
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_time = appointment_time

# Bill class
class Bill:
    def __init__(self, patient_name, consultation_fee, service_fees):
        self.hospital_name = "Kingston General Hospital"
        self.patient_name = patient_name
        self.consultation_fee = consultation_fee
        self.service_fees = service_fees
        self.total = consultation_fee + service_fees

    def display(self):
        print("\n======= RECEIPT =======")
        print(f"{self.hospital_name}")
        print(f"Patient Name: {self.patient_name}")
        print(f"Consultation Fee: JMD ${self.consultation_fee}")
        print(f"Additional Services: JMD ${self.service_fees}")
        print(f"Total Amount: JMD ${self.total}")
        print("=======================\n")

# Data storage
patients = {}
doctors = {}
appointments = {}

# Menu Functions
def register_patient():
    name = input("Enter patient's name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    patient = Patient(name, age, gender)
    patients[patient.patient_id] = patient
    print(f"Patient registered successfully. Patient ID: {patient.patient_id}")

def view_patients():
    if not patients:
        print("No patients registered.")
        return
    for pid, patient in patients.items():
        print(f"[{pid}] {patient.name}, Age: {patient.age}, Gender: {patient.gender}")

def add_doctor():
    name = input("Enter doctor's name: ")
    specialty = input("Enter specialty: ")
    schedule = input("Enter available schedule (comma-separated YYYY-MM-DD HH:MM): ").split(",")
    schedule = [s.strip() for s in schedule]
    doctor = Doctor(name, specialty, schedule)
    doctors[doctor.doctor_id] = doctor
    print(f"Doctor added successfully. Doctor ID: {doctor.doctor_id}")

def view_doctors():
    if not doctors:
        print("No doctors available.")
        return
    for did, doc in doctors.items():
        print(f"[{did}] {doc.name} ({doc.specialty}) - Available: {', '.join(doc.schedule)}")

def book_appointment():
    view_patients()
    pid = input("Enter patient ID: ")
    view_doctors()
    did = input("Enter doctor ID: ")
    appt_time = input("Enter appointment time (YYYY-MM-DD HH:MM): ")

    for appt in appointments.values():
        if appt.doctor_id == did and appt.appointment_time == appt_time:
            print("Error: This doctor already has an appointment at that time.")
            return
    appointment = Appointment(pid, did, appt_time)
    appointments[appointment.appointment_id] = appointment
    print(f"Appointment booked successfully. Appointment ID: {appointment.appointment_id}")

def view_appointments():
    if not appointments:
        print("No appointments scheduled.")
        return
    for aid, appt in appointments.items():
        p = patients[appt.patient_id].name
        d = doctors[appt.doctor_id].name
        print(f"[{aid}] {p} with Dr. {d} at {appt.appointment_time}")

def cancel_appointment():
    view_appointments()
    aid = input("Enter appointment ID to cancel: ")
    if aid in appointments:
        del appointments[aid]
        print("Appointment cancelled.")
    else:
        print("Invalid appointment ID.")

def generate_bill():
    view_patients()
    pid = input("Enter patient ID: ")
    if pid not in patients:
        print("Invalid patient ID.")
        return
    patient = patients[pid]
    try:
        service_fees = float(input("Enter additional service fees (JMD): "))
    except ValueError:
        print("Invalid fee input.")
        return
    bill = Bill(patient.name, 3000, service_fees)
    bill.display()

# Main Menu
def main_menu():
    while True:
        print("\n====== Hospital Management System ======")
        print("1. Register New Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. View Appointments")
        print("7. Cancel Appointment")
        print("8. Generate Bill")
        print("9. Exit")
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                register_patient()
            elif choice == 2:
                view_patients()
            elif choice == 3:
                add_doctor()
            elif choice == 4:
                view_doctors()
            elif choice == 5:
                book_appointment()
            elif choice == 6:
                view_appointments()
            elif choice == 7:
                cancel_appointment()
            elif choice == 8:
                generate_bill()
            elif choice == 9:
                print("Exiting system...")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

# Run the application
if __name__ == "__main__":
    main_menu()

