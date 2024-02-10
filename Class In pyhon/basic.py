#in java or c++

# public class Student {
#     String first_name;
#     String last_name;
#     double cgpa;
#     int age;
#
#     Student(String fname, String lname, double cgpa, int age){
#         first_name = fname;
#         last_name = lname;
#         this.cgpa = cgpa;
#         this.age = age;
#     }
#
#     void printFullname(){
#         println(first_name + last_name)
#         println(this.first_name + this.last_name)
#     }
# }
#
# obj = new Student("A", "B", 3.8, 22)

#----------------------------In Python----------------------------------#
#   here self means this

class Student:
    def __init__(self, fname, lname, cgpa, age):
         self.first_name = fname
         self.last_name = lname
         self.cgpa = cgpa
         self.age = age
    def information(self):
        print(self.first_name + " " + self.last_name + " " + str(self.cgpa) + " " + str( self.age))

obj = Student("Musfiqur","Rahman", 3.15, 23)
obj.information()