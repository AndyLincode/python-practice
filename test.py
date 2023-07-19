class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping...")

    def eat(self):
        print(f"{self.name} is eating.")


class Student(People):
    def __init__(self, name, age, student_id):
        People.__init__(self, name, age)
        self.student_id = student_id

    def eat(self, food):  # 覆蓋
        print(f"{self.name} is now eating {food}")


student1 = Student("Andy", 24, "AA001")
print(student1.name, student1.age, student1.student_id)  # Andy 24 AA001
student1.sleep()  # Andy is sleeping...
student1.eat("beef")  # Andy is now eating beef
