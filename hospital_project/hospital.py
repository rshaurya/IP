from tabulate import tabulate

pt_table = [['1234','Mudit','16', 'M', '11-12-2006', '24-02-22', '24-02-23', 'Indore', '1238794560'],
            ['1001', 'Atharva', '65', 'M', '02-12-1982', '14-07-2012', '15-07-2012', 'Lucknow', '1769785321'],
            ['1423', 'Labhi', '12', 'F', '09-01-2010', '10-02-2023', 'NULL', 'Delhi', '1347985234']]

p_heads = ['ID', 'Name', 'Age', 'Gender', 'DOB', 'Admit date', 'Discharge date', 'Location', 'Contact no']

def patient(pt_table):
    print('PATIENT')
    print('\n','1. View details','\n',
          '2. Admit new patient','\n',
          '3. Update patient details')
    opt = input('What would you like to do? ')

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
                '\n', '3. DOB', '\n',
                '\n', '4. Location', '\n', 
                '\n', '5. Contact no', '\n')
        opt = input('Enter your choice: ')
        ID = input('Enter patient id: ')
        
        if opt == '1':
            for i in pt_table:
                if ID in i:
                    name = input('Enter new name: ')
                    i[1] = name
                    print('Successfully updated! Id of patient is: ', ID)
                    print(tabulate(pt_table, p_heads, tablefmt="outline"))
                elif ID not in i:
                    print('ID is invalid')
                    break
        if opt == '2':
            for i in pt_table:
                if ID in i:
                    age = input('Enter new age: ')
                    i[2] = age
                    print('Successfully updated! Id of patient is: ', ID)
                    print(tabulate(pt_table, p_heads, tablefmt="outline"))
                elif ID not in i:
                    print('ID is invalid')
                    break
        if opt == '3':
            for i in pt_table:
                if ID in i:
                    dob = input('Enter new DOB: ')
                    i[4] = dob
                    print('Successfully updated! Id of patient is: ', ID)
                    print(tabulate(pt_table, p_heads, tablefmt="outline"))
                elif ID not in i:
                    print('ID is invalid')
                    break
        if opt == '4':
            for i in pt_table:
                if ID in i:
                    loc = input('Enter new location: ')
                    i[7] = loc
                    print('Successfully updated! Id of patient is: ', ID)
                    print(tabulate(pt_table, p_heads, tablefmt="outline"))        
                elif ID not in i:
                    print('ID is invalid')
                    break
        if opt == '5':
            for i in pt_table:
                if ID in i:
                    num = input('Enter new contact number: ')
                    i[8] = num
                    print('Successfully updated! Id of patient is: ', ID)
                    print(tabulate(pt_table, p_heads, tablefmt="outline"))
                elif ID not in i:
                    print('ID is invalid')
                    break
        

dr_table = [['1234', 'Dr. Labhi Ajmera', '37', 'F', 'Neurology', '13-0-2012', '60 Lpa'],
            ['1002', 'Dr. Atharva Dubey', '20', 'M', 'Biology', '02-02-2002', '75 Lpa'],
            ['1242', 'Dr. Mudit Palwadi', '47', 'F', 'Physiotherapy', '12-02-2003', '40 Lpa']]

d_heads = ['ID', 'Name', 'Age', 'Gender', 'Specialization', 'Hire date', 'Salary']

def doctor(dr_table):
    print('DOCTOR')
    print('\n', '1. View details', '\n',
                '2. Hire doctor', '\n',
                '3. Fire doctor', '\n'
                '4. Update details', '\n')
    opt = input('What would you like to do? ')

    if opt == '1':
        print('Details')
        print(tabulate(dr_table, d_heads, tablefmt="outline"))
    if opt == '2':
        print('Enter his/her details in the following order: ')
        print('ID, Name, Age, Gender, Specialisation, Hire date, Salary')

        tmp = []
        tmp.append(input('ID: '))
        tmp.append(input('Name: '))
        tmp.append(input('Age: '))
        tmp.append(input('Gender: '))
        tmp.append(input('Specialisation: '))
        tmp.append(input('Hire date: '))
        tmp.append(input('Salary: '))
        
        dr_table.append(tmp)
        print(tabulate(dr_table, d_heads, tablefmt="outline"))
    
    if opt == '3':
        print('Caution! You are about to fire staff!')
        print('Enter the details: ')
        ID = input('Enter ID: ')
        name = input('Enter name(optional. Type xyz if name is unknown): ')
        for i in dr_table:
            if ID in i:
                dr_table.pop(dr_table.index(i))
                print(tabulate(dr_table, d_heads, tablefmt='outline'))
            elif ID not in i:
                print('Invalid id')
                break
    if opt == '4':
        print('What do you want to update?')
        print('\n', '1. Name', '\n',
                '\n', '2. Specialisation', '\n',
                '\n', '3. Salary', '\n')
        opt = input('Enter your choice: ')
        ID = input("Enter doctor's id: ")
        if opt == '1':
            for i in dr_table:
                if ID in i:
                    name = input('Enter new name: ')
                    i[1] = name
                    print('Successfully updated! ID of the doctor is: ', ID)
                    print(tabulate(dr_table, d_heads, tablefmt='outline'))
                elif ID not in i:
                    print('Invalid id')
                    break
        if opt == '2':
            for i in dr_table:
                if ID in i:
                    spec = input('Enter new specialisation: ')
                    i[4] = spec
                    print('Successfully updated! ID of the doctor is: ', ID)
                    print(tabulate(dr_table, d_heads, tablefmt='outline'))
                elif ID not in i:
                    print('Invalid id')
                    break
        if opt == '3':
            for i in dr_table:
                if ID in i:
                    sal = input('Enter new salary: ')
                    i[6] = sal
                    print('Successfully updated! ID of the doctor is: ', ID)
                    print(tabulate(dr_table, d_heads, tablefmt='outline'))
                elif ID not in i:
                    print('Invalid id')
                    break

ward_table = [['001', 'Occupied', 'General'],
                ['002', 'Vacant', 'ICU'],
                ['003', 'Occupied', 'Operation Theatre'],
                ['004', 'Vacant', 'Research wing']]

ward_heads = ['Ward number', 'Status', 'Ward type']

def ward(ward_table):
    print('WARD')
    print('1. View ward details', '\n',
                '2. Update ward details', '\n')
    opt = input('What would you like to do? ')

    if opt == '1':
        print(tabulate(ward_table, ward_heads, tablefmt='outline'))
    if opt == '2':
        print('What would you like to update?')
        print('1. Ward number', '\n',
                '2. Ward Status', '\n')
        opt = input('Enter your choice: ')
        ID = input('Enter current ID of ward: ')

        if opt == '1':
            for i in ward_table:
                if ID in i:
                    new = input('Enter new ward number: ')
                    i[0] = new
                    print('SUccessfully updated! The new ward number is ', new)
                    print(tabulate(ward_table, ward_heads, tablefmt='outline'))
        if opt == '2':
            for i in ward_table:
                if ID in i:
                    new = input('Enter new ward status: ')
                    i[1] = new
                    print('SUccessfully updated! The new ward status is ', new)
                    print(tabulate(ward_table, ward_heads, tablefmt='outline'))



print('\n', 'Welcome to Kokilaben Ambani Hospital')

while True:
    print('View details of: ')
    print('\t 1) PATIENT')
    print('\t 2) DOCTOR')
    print('\t 3) WARD')
    print('\t 4) EXIT')

    num = input('Enter: ')
    if num =='1':
        patient(pt_table)

    elif num =='2':
        doctor(dr_table)
        
    elif num =='3':
        ward(ward_table)

    elif num =='4':
        print('You are exiting!')
        break