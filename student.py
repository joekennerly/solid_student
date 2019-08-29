class Student:

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age}, and in cohort {self.cohort} {self.full_name}'

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return f"{self.__first_name}{self.__last_name}"
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, new_name):
        if type(new_name) is str:
            self.__first_name = new_name
        else:
            raise TypeError('Please enter a first name')

    @last_name.setter
    def last_name(self, new_name):
        if type(new_name) is str:
            self.__last_name = new_name
        else:
            raise TypeError('Please enter a last name')

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please enter an age')

    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('Please enter a cohort')

# CAN reset attribute
mike = Student()
mike.first_name = "mike"
mike.last_name = "rumph"
mike.age = 35
mike.cohort = 1
print(mike)

# CANNOT reset attribute
mike.full_name = "ruke mikph"