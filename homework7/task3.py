# Создайте программу, имитирующую работу клиники. Создайте пациента, задайте ему план
# лечения и продемонстрируйте работу программы.

class Doctor:
    def treat(self):
        print("Врач проводит лечение")

class Surgeon(Doctor):
    def treat(self):
        print("Хирург проводит операцию")

class Dentist(Doctor):
    def treat(self):
        print("Дантист лечит зубы")

class Therapist(Doctor):
    def treat(self):
        print("Терапевт проводит лечение")

    def assign_doctor(self, patient):
        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            patient.doctor = Dentist()
        else:
            patient.doctor = Therapist()

        print(f"Пациенту назначен: {patient.doctor.__class__.__name__}")

class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None

print("Пациент 1: план лечения - 1")
patient1 = Patient(1)
therapist = Therapist()
therapist.assign_doctor(patient1)
patient1.doctor.treat()
print()

print("Пациент 2: план лечения - 2")
patient2 = Patient(2)
therapist.assign_doctor(patient2)
patient2.doctor.treat()
print()

print("Пациент 3: план лечения - 5")
patient3 = Patient(3)
therapist.assign_doctor(patient3)
patient3.doctor.treat()
print()