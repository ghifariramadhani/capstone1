# MUHAMMAD GHIFARI RAMADHANI
# CAPSTONE PROJECT MODULE 1 : DATA KARYAWAN
# CRUD (CREATE, READ, UPDATE, AND DELETE)

dataKaryawan = [
    {
        'EmpID': 'Emp001',
        'Name': 'Muhammad',
        'Position': 'Manager',
        'Department': 'Finance',
    },
    {
        'EmpID': 'Emp002',
        'Name': 'Ghifari',
        'Position': 'HumanResource',
        'Department': 'Finance',
    },
    {
        'EmpID': 'Emp003',
        'Name': 'Ramadhani',
        'Position': 'StaffMember',
        'Department': 'Finance',
    }
]

# READ Function
def read():
    while True:
        print('''
-------------------------------       
   EMPLOYEES DATA MAIN MENU 
-------------------------------
    1. View Employees Data
    2. View an Employee Data
    3. Main Menu
            ''')

        inputRead = int(input('Please Select An Option (1-3):  '))

        if inputRead == 1:
            print('Employees Data\n')
            print('EmpID\t Name        \t Position  \t Department\n')
            for i,j in enumerate(dataKaryawan) :
                print('{}\t {}  \t {}\t {}'.format(j['EmpID'],j['Name'],j['Position'],j['Department']))

        elif inputRead == 2:
            read2 = (input('Insert Employee ID : ')).capitalize()
            print(f'Employee ID : {read2}')

            for i,j in enumerate(dataKaryawan) :
                if read2 == j['EmpID'] :
                    print('EmpID\t Name        \t Position  \t Department\n')
                    print('{}\t {}  \t {}\t {}'.format(j['EmpID'],j['Name'],j['Position'],j['Department']))
                    break

                elif read2 != j['EmpID'] and (i == len(dataKaryawan)-1):
                    print('=========== DATA NOT FOUND ============')
                    break        

        elif inputRead == 3:
            break
        
        else:
            print('=========== PLEASE CHOOSE CORRECTLY ===========')

# CREATE Function
def create():
    while True:
        print('''
-------------------------------
      CREATE EMPLOYEE DATA 
-------------------------------
    1. Add New Employee Data
    2. Main Menu
                ''')
        inputCreate = int(input('Please Select An Option (1-2): '))

        if inputCreate == 1 :
            inputCreate2 = (input('Enter Emmployee ID : ')).capitalize()
            for i,j in enumerate(dataKaryawan) :
                if inputCreate2 == j['EmpID'] :
                    print('Data Exists')
                    break

                elif inputCreate2 != j['EmpID'] and (i == len(dataKaryawan)-1):
                    namaKaryawan = str(input('Employee Name: '))
                    jabatanKaryawan = input('Employee Position: ').capitalize()
                    departemenKaryawan = input('Employee Department: ').capitalize()
                    simpanData = input('Create Data? (Y/N): ').upper()
                
                    if simpanData == 'Y' :
                        print('Data Created')
                        dataKaryawan.append({
                            'EmpID' : inputCreate2,
                            'Name': namaKaryawan,
                            'Position': jabatanKaryawan,
                            'Department': departemenKaryawan,
                            })
                    elif simpanData == 'N' :
                        print('Data Not Created (N)')
                    else:
                        print('=========== DATA NOT CREATED, PLEASE CHOOSE BETWEEN Y/N ===========')
                    break
        
        elif inputCreate == 2:
            break
        
        else:
            print('=========== NOT VALID, PLEASE SELECT BETWEEN 1-2 ===========')

# UPDATE Function
def update():
    while True:
        print('''
-------------------------------
     UPDATE EMPLOYEE DATA 
-------------------------------
    1. Update Data
    2. Main Menu
                ''')
        inputUpdate = int(input('Please Select An Option (1-2): '))

        if inputUpdate == 1:
            inputUpdate2 = (input('Enter Employee ID : ')).capitalize()

            for i,j in enumerate(dataKaryawan) :
                if inputUpdate2 == j['EmpID'] :
                    print('EmpID\t Name        \t Position\t Department')
                    print('{}\t {}  \t {}\t {}'.format(j['EmpID'],j['Name'],j['Position'],j['Department']))
                    
                    inputUpdate3 = input('Select Y To Continue or N To Cancel (Y/N): ').capitalize()
                    if inputUpdate3 == 'Y':
                        kolomUpdate = input('Insert The Column You Want To Update: ').capitalize()
                        for key in j.keys():
                            if kolomUpdate == key :
                                inputUpdate4 = input(f'Insert New {kolomUpdate}: ').capitalize()
                                inputUpdate5 = input('Update Data? (Y/N): ').upper()
                                if inputUpdate5 == 'Y':
                                    j[kolomUpdate] = inputUpdate4
                                    print('Data Updated')
                                elif inputUpdate5 == 'N':
                                    print('Data Not Updated')
                                else:
                                    print('=========== DATA NOT UPDATED, PLEASE CHOOSE BETWEEN Y/N ===========')
                                break

                    else:
                        break
                    break

                elif inputUpdate2 != j['EmpID'] and (i == len(dataKaryawan)-1):
                    print('=========== DATA DOES NOT EXIST ===========')
                    break

        elif inputUpdate == 2:
            break

        else:
            print('=========== NOT VALID, PLEASE SELECT BETWEEN 1-2 ===========')

# DELETE Function
def delete():
    while True:
        print('''
-------------------------------
     DELETE EMPLOYEE DATA
-------------------------------
    1. Delete Data
    2. Main Menu
        ''')
        inputDelete = int(input('Please Select An Option (1-2): '))

        if inputDelete == 1:
            inputDelete2 = (input('Enter Employee ID : ')).capitalize()
        
            for i,j in enumerate(dataKaryawan) :
                if inputDelete2 == j['EmpID'] :
                    print('EmpID\t Name        \t Position\t Department')
                    print('{}\t {}  \t {}\t {}'.format(j['EmpID'],j['Name'],j['Position'],j['Department']))

                    deleteData = input('Delete Data? (Y/N): ').upper()
                    if deleteData == 'Y' :
                        del dataKaryawan[i]
                        print('Data Deleted')
                    elif deleteData == 'N' :
                        print('Data Not Deleted')
                    else:
                        print('=========== DATA NOT DELETED, PLEASE CHOOSE BETWEEN Y/N ===========')
                    break

                elif inputDelete2 != j['EmpID'] and (i == len(dataKaryawan)-1):
                    print('=========== DATA DOES NOT EXIST ============')
                    break

        elif inputDelete == 2:
            break
            
        else:
            print('=========== NOT VALID, PLEASE SELECT BETWEEN 1-2 ===========')

# TAMPILAN MAIN MENU
while True:
    print('''
-----------------------------------------
        PURWADHIKA EMPLOYEE DATA
-----------------------------------------
    1. Show Employees Data
    2. Create Employee Data
    3. Update Employee Data
    4. Delete Employee Data
    5. Exit
    ''')
    menuNumber = int(input('Select The Menu You Want To Choose (1-5): '))

    if menuNumber == 1:
        read()
    elif menuNumber == 2:
        create()
    elif menuNumber == 3:
        update()
    elif menuNumber == 4:
        delete()
    elif menuNumber == 5:
        break
    else :
        print('=========== NOT VALID, PLEASE SELECT BETWEEN 1-5 ===========')