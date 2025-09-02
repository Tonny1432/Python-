class encapsulation:
    def public( self):
        self.name =" Tonny"
        print(" The person name is:",self.name)
    def protected(self):
        self._age= 24
        print("The age of the person is:",self._age)
    def get_private(self):
        self.__gender= "Male"
        print("The gender of the person is:",self.__gender)
    def set_emp(self,emp_no):
        self__emp_no = emp_no
        print("the employes number is:",self__emp_no)

Encapse = encapsulation()
Encapse.public()
print(Encapse.name)
Encapse.protected()
print(Encapse._age)
Encapse.get_private()
Encapse.set_emp(8464651)
