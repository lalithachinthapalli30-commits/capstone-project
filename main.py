# Smart Healthcare Assistant & Appointment Platform
# Main Program

doctors = [
    {"id": 1, "name": "Dr. Ananya Sharma", "specialization": "Cardiologist"},
    {"id": 2, "name": "Dr. Rahul Kumar", "specialization": "Dermatologist"},
    {"id": 3, "name": "Dr. Priya Reddy", "specialization": "General Physician"},
    {"id": 4, "name": "Dr. Arjun Singh", "specialization": "Orthopedic"},
]

patients = []
appointments = []


def register_patient():
    print("\n--- Patient Registration ---")

    name = input("Enter patient name: ")
    age = input("Enter age: ")
    phone = input("Enter phone number: ")

    patient = {
        "id": len(patients) + 1,
        "name": name,
        "age": age,
        "phone": phone
    }

    patients.append(patient)

    print("\nPatient registered successfully!")
    print("Patient ID:", patient["id"])


def show_doctors():
    print("\n--- Available Doctors ---")

    for doctor in doctors:
        print(
            f"{doctor['id']}. {doctor['name']} "
            f"- {doctor['specialization']}"
        )


def book_appointment():
    if not patients:
        print("\nPlease register a patient first.")
        return

    print("\n--- Book Appointment ---")

    patient_id = int(input("Enter patient ID: "))

    patient = next(
        (p for p in patients if p["id"] == patient_id),
        None
    )

    if not patient:
        print("Patient not found.")
        return

    show_doctors()

    doctor_id = int(input("Enter doctor ID: "))

    doctor = next(
        (d for d in doctors if d["id"] == doctor_id),
        None
    )

    if not doctor:
        print("Doctor not found.")
        return

    date = input("Enter appointment date (DD-MM-YYYY): ")
    time = input("Enter appointment time: ")

    appointment = {
        "id": len(appointments) + 1,
        "patient": patient["name"],
        "doctor": doctor["name"],
        "specialization": doctor["specialization"],
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    print("\nAppointment booked successfully!")
    print("Appointment ID:", appointment["id"])


def view_appointments():
    print("\n--- Appointments ---")

    if not appointments:
        print("No appointments available.")
        return

    for appointment in appointments:
        print("\nAppointment ID:", appointment["id"])
        print("Patient:", appointment["patient"])
        print("Doctor:", appointment["doctor"])
        print("Specialization:", appointment["specialization"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])


def healthcare_assistant():
    print("\n--- Smart Healthcare Assistant ---")

    print("1. Fever")
    print("2. Headache")
    print("3. Cough")
    print("4. Stomach Pain")
    print("5. Exit")

    choice = input("Select your symptom: ")

    suggestions = {
        "1": "Stay hydrated and monitor your temperature. Consult a doctor if fever persists.",
        "2": "Rest, stay hydrated, and avoid excessive screen time. Consult a doctor if severe.",
        "3": "Stay hydrated and rest. Consult a doctor if breathing difficulty occurs.",
        "4": "Drink sufficient water and eat light food. Consult a doctor if pain is severe.",
        "5": "Returning to main menu."
    }

    print("\nAssistant:", suggestions.get(
        choice,
        "Invalid choice. Please select a valid option."
    ))


def main():
    while True:
        print("\n========================================")
        print(" SMART HEALTHCARE ASSISTANT")
        print(" APPOINTMENT PLATFORM")
        print("========================================")

        print("1. Register Patient")
        print("2. View Doctors")
        print("3. Book Appointment")
        print("4. View Appointments")
        print("5. Healthcare Assistant")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            register_patient()

        elif choice == "2":
            show_doctors()

        elif choice == "3":
            book_appointment()

        elif choice == "4":
            view_appointments()

        elif choice == "5":
            healthcare_assistant()

        elif choice == "6":
            print("\nThank you for using Smart Healthcare Assistant!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()

