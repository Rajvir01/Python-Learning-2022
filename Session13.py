# DATA STRUCTURE - QUEUE IMPLEMENTATION


class Patient:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.next_patient = None
        self.previous_patient = None

    def show(self):
        print("==============")
        print(self.name, self.gender, self.age)
        print("==============")


class PatientQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("Patient queue created")

    def enqueue(self, patient):
        self.size += 1
        if self.head is None:
            self.head = patient
            self.tail = patient
        else:
            self.tail.next_patient = patient
            patient.previous_patient = self.tail
            self.tail = patient

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            temp = self.head
            self.head = self.head.next_patient
            del temp

    def iterate(self, direction =1):
        if direction == 1:
            print("ITERATING FORWARD")
            temp = self.head
            while True:
                temp.show()
                temp = temp.next_patient

                if temp.next_patient is None:
                    temp.show()
                    break

        else:
            print("ITERATING BACKWARDS")
            temp = self.tail
            while True:
                temp.show()
                temp = temp.previous_patient

                if temp.previous_patient is None:
                    temp.show()
                    break

    def peek(self, option=1):
        if option == 1:
            return self.head

        else:
            return self.tail

queue = PatientQueue()

queue.enqueue(Patient(name="John", gender="male", age=65))
queue.enqueue(Patient(name="ron", gender="male", age=55))
queue.enqueue(Patient(name="fiona", gender="female", age=45))
queue.enqueue(Patient(name="Johny", gender="male", age=54))
queue.enqueue(Patient(name="Jeny", gender="female", age=34))

queue.dequeue()
print("size is:", queue.size)
queue.peek().show()
queue.iterate()

