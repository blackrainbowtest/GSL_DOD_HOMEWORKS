class Job:
    def __init__(self, uname, salary, wHours):
        self.uname = uname
        self.salary = salary
        self.wHours = wHours

    def details(self):
        return f"Name: {self.uname}, Salary: {self.salary}, Worked hours: {self.wHours}"


class Doctor(Job):
    def __init__(self, uname, salary, wHours, specialty, yearsOfExp):
        super().__init__(uname, salary, wHours)
        self.specialty = specialty
        self.yearsOfExp = yearsOfExp

    def details(self):
        parentDetails = super().details()
        return f"{parentDetails}, Specialty: {self.specialty}, Years of Experience: {self.yearsOfExp}"


class Teacher(Job):
    def __init__(self, uname, salary, wHours, subject, position):
        super().__init__(uname, salary, wHours)
        self.subject = subject
        self.position = position

    def details(self):
        parentDetails = super().details()
        return f"{parentDetails}, Subject: {self.subject}, Position: {self.position}"


# used class Job
lawyer = Job("Mark Nazarbetyan", 147000, 10)
# used class Teacher
computerScienceTeacher = Teacher("Karapes Suqiasyan", 210000, 12, "Computer Science", "Doctor")
# used class Doctor
pediatricDoctor = Doctor("Hmayak Nalbandyan", 350000, 8, "Pediatrics", 7)

print(lawyer.details())
print(computerScienceTeacher.details())
print(pediatricDoctor.details())
