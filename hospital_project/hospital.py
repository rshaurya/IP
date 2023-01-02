# patient details
# dict -- key-pID
#PID - 2 lists > personal details > hospital status
    # view details
    # admit new patient
    # update patient details

from tabulate import tabulate
pt_table = [['1234','Mudit','16', 'M', '11-12-2006', '24-02-22', '24-02-23', 'Indore', '1238794560'],
            ['1001', 'Atharva', '65', 'M', '02-12-1982', '14-07-2012', '15-07-2012', 'Multiverse', '1769785321']]
p_heads = ['ID', 'Name', 'Age', 'Gender', 'DOB', 'Admit date', 'Discharge date', 'Location', 'Contact no']

def patient(pt_table):
    print('PATIENT')
    print('\n','1. view details','\n',
          '2. admit new patient','\n',
          '3. update patient details')

    opt = input('what would you like to do? ')
    if opt == '1':
        print('Personal Details')
        print(tabulate(pt_table, p_heads, tablefmt="outline"))

    if opt == '2':
        print('Enter his/her details in the following order: ')
        print('Patient ID, Name, Age, Gender, DOB, Admit date, Discharge date, Location, Contact no')

        tmp = []
        tmp.append(input('ID: '))
        tmp.append(input('Name: '))
        tmp.append(input('Age: '))
        tmp.append(input('Gender: '))
        tmp.append(input('DOB: '))
        tmp.append(input('Admit date: '))
        tmp.append(input('Discharge date: '))
        tmp.append(input('Location: '))
        tmp.append(input('Contact no: '))
        
        pt_table.append(tmp)
        print(tabulate(pt_table, p_heads, tablefmt="outline"))


    if opt == '3':
        print('What do you want to update?')
        print('\n', '1. Name', '\n',
                '\n', '2. Age', '\n',
                '\n', '3. Gender', '\n',
                '\n', '4. DOB', '\n',
                '\n', '5. Location', '\n', 
                '\n', '6. Contact no', '\n')
        
        opt = input('Enter your choice: ')
        id = input('Enter patient id: ')
        
        for i in pt_table:
            if id in i:
                
        

#doctor details
# dict -- key-dID
#single list
    # view details
    # hire doctor
    # fire doctor
    # update details      

dr_table = [['Dr. Labhi Ajmera', '37', 'F', 'Neurology', '13-0-2012', '60 Lpa']]
d_heads = ['name', 'age', 'gender', 'specialization', 'hire date', 'salary']
def doctor(dr_table):
    print('DOCTOR')
    print('\n', '1. View details', '\n',
                '2. Hire doctor', '\n',
                '3. Fire doctor', '\n'
                '4. Update details', '\n')
    
    opt = input('What would you like to do? ')
    if opt == '1':
        print('Personal Details')
        print(tabulate(dr_table, d_heads, tablefmt="outline"))


# ward details
#  dict -- key- ward no.
    # view details
    # upate details

ward_dict = {}
def ward(ward_dict):
    print('working ward func!')

    
# department details
#dict -- key -dept
# list - employee names in dept
    # view departments
    # add new dept
    # add new empl

dept_dict = {}
def dept(dept_dict):
    print('working dept func!')



print('Welcome to ____ hospital')
print('\n')
print('View details of: ')
print('\t 1) PATIENT')
print('\t 2) DOCTOR')
print('\t 3) WARD')
print('\t 4) DEPARTMENT')

num = input('Enter: ')
if num =='1':
    patient(pt_table)

if num =='2':
    doctor(dr_table)
    
if num =='3':
    ward(ward_dict)

if num =='4':
    dept(dept_dict)

