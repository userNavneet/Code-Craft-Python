patient_name=input("enter patient name: ")
patient_age=input("enter patient age: ")
is_patient_new=input("are you a new patient: enter 'True' or 'False' ")
boolian_input = bool(is_patient_new)
if(boolian_input == True):
    print(patient_name + " is a new patient")
    print(patient_age +' years old')
else:
    print(patient_name + " is an old patient")