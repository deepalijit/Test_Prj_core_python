
#Address Class
class Address():

    def set_city(self,c):
        self.city = c

    def get_city(self):
        return self.city

    def set_pin(self,p):
        self.pin = p

    def get_pin(self):
        return self.pin

#Student Class
class Student():
    def set_rn(self,rn):
        self.rn = rn
    def set_name(self,name):
        self.name = name
    def set_marks(self,marks):
        self.marks = marks
    def set_address(self,address):
        self.address = address

    def get_rn(self):
        return self.rn
    def get_name(self):
        return self.name
    def get_marks(self):
        return self.marks
    def get_address(self):
        return self.address

##    def __str__(self):
##        return f'{self.rn},{self.name},{self.marks},{self.address}'

class EmptyListError(Exception):
    def __init__(self,msg):
        self.msg = msg

student_list = []

a1=Address()
a1.set_city('Pune')
a1.set_pin(1)
#print(a1.get_city(),a1.get_pin())

a2=Address()
a2.set_city('Mumbai')
a2.set_pin(2)
#print(a2.get_city(),a2.get_pin())
   
address_list = [a1,a2]
#address_list = []
print('''select option to choose domain on which you want to perform operation
A for Address
S for Students
E for exit
''')

while True:
    ch = input('Enter option to select domain: ')
    if ch=='A':
        print('''select options for Address Record Operations:
        1.Create Address
        2.Update Address
        3.Delete Address
        4.Show Address
        5.Exit''')
        print()
        while True: 
            op1 =  int(input('Enter option for Address Record Operations: '))
            if op1 == 1:
                na = int(input('Enter no of address records you want to enter: '))
                for i in range(na):
                    city1 = input('Enter name of city: ')
                    pin1 = int(input('Enter pin of entered city: '))
                    a = Address()
                    a.set_city(city1)
                    a.set_pin(pin1)
                    address_list.append(a)
                    print('record created')
                    print(a.get_city())
                    print(a.get_pin())
                    print()
                print(len(address_list))
                print(address_list)


            if op1 == 2:
                cu = input("Enter city of wchich pin you want to update: ")
                for i in address_list:
                    if i.get_city() == cu:
                        i.set_pin(int(input('Enter new pin: ')))

                print()
            

            elif op1 == 3:
                cd = input('Enter name of city you want to delete: ')
                #print(cd)
                #cd.capitalize()
                for i in address_list:
                    #print('test1')
                    if i.get_city()==cd:
                        #print('test2')
                        address_list.remove(i)
                print()

            elif op1 == 4:
                for i in address_list:
                    print(i.get_city(),i.get_pin())
                    print()


            elif op1 == 5:
                break

    elif ch=='S':
        print('''select options for Student Record Operations:
        1.Create Student
        2.Update Student
        3.Delete Student
        4.Show Student
        5.Exit''')
        print()

        while True: 
            op2 =  int(input('Enter option for Student Record Operations: '))
            if op2 == 1:
                def check_list_len(given_list):
                    if len(given_list)>0:
                        return given_list
                    else:
                        raise EmptyListError('No adress record in list.Please enter address record first.')

                while True:
                    ns = int(input('Enter no of student records you want to enter: '))
                    try:
                        check_list_len(address_list)
                        
                        for i in range(ns):
                            s = Student()
                            s.set_rn(int(input('Enter student roll no: ')))
                            s.set_name(input('Enter student name: '))
                            s.set_marks(float(input('Enter students marks: ')))
                            p1 = int(input('Enter pin of city: '))
                            for addr in address_list:
                                #print('inside for',type(addr.get_pin()),type(p1))
                                if addr.get_pin() == p1:
                                    #print('inside if')
                                    s.set_address(addr)
                            print(type(s.get_rn()))
                            s.get_name()
                            s.get_marks()
                            
                            student_list.append(s)
                            print(s.rn)
                            print(s.name)
                            print(s.marks)
                            print(student_list)
                            print(s.address)
                            #print(s.get_rn(),s.get_name(),s.get_marks())
                        break
                    except EmptyListError as e:
                        print(e)
                        break

            if op2 == 4:
                for i in student_list:
                    print(i.get_rn(),i.get_name(),i.get_marks(),i.address.city)
            elif op2 == 5:
                break

    elif ch == 'E':
        break









  
