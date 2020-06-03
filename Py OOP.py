class person:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.age = age
        self.height = height

    def summary(self):
        return f"name: {self.name}, age: {self.age}, height:{self.height}"


man_list = [person("habib", 65, 5), person("babib", 12, 4.2), person("kabib", 18, 5.6), person("sabib", 39, 5.5),
            person("rabib", 6, 2)]

#or person in man_list:
#    print(person.summary())


class student(person):
    def __init__(self, name: str, age: int, height: int, id, mail):
        super().__init__(name, age, height)
        self.id=id
        self.mail=mail

    def summary(self):
         return f"name= {self.name}, ID= {self.id}, Mail={self.mail}"

    def __str__(self):
        return f"name= {self.name}, ID= {self.id}, Mail={self.mail}"

    def __repr__(self):
        return self.summary()


Student=student("shikhar",24,6,1602273,"shikharali13@gmailcom")

#print(Student.summary())

print(Student)  #with __str__or __repr__


