import os  # to get the files working directory
import re  # to validate email adress
# path defined globally
path = os.getcwd()
filePath = path+'/student.txt'


def ValidEmail(s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, s):
        return True
    return False


def isValidPhone(s):

    # 1) Begins with 0 or 91
    # 2) Then contains 6,7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(s)


def add():
    rool_no = input("Enter the rool number:")
    name = input("Enter the name of the student:")
    email = input("Enter the email of the studnet:")
    if not ValidEmail(email):
        print("Inavlid Email Entered please enter email again")
        email = input("Email:")
    ph_no = input("Contact NO:")
    if not isValidPhone(ph_no):
        print("Inavlid phone number Entered,please enter number again")
        ph_no = input("Phone Number")
    cg = input("Enter the CG:")

    file = open(filePath, "a")
    file.write(rool_no+"\t")
    file.write(name+"\t")
    file.write(email+"\t")
    file.write(ph_no+"\t")
    file.write(cg+"\t")
    file.write("\n")
    print("Student data sucessfully added")
    file.close()


def delete():
    rool = input("Enter the roll number to be deleted")
    file = open(filePath, "r")
    all = file.readlines()  # stores all data in one variable
    file.close()
    # rewriting all data except one to eb delted in the file
    file = open(filePath, "w")
    deleted = "Data to be deleted is not found"
    for data in all:
        # gets the roll number 1 is needed to restrict the size of the array
        d = data.split("\t", 1)
        if (d[0] != rool):
            file.writelines(data)
        else:
            deleted = data
    file.close()
    if (deleted == "Data to be deleted is not found"):
        print(deleted)
    else:
        print("The deleted record is", deleted)


def update():
    rool = input("Enter the roll number to be updated:")
    file = open(filePath, "r")
    all = file.readlines()  # stores all data in one variable
    file.close()
    file = open(filePath, "w")
    found = False
    for data in all:
        d = data.split("\t", 1)

        if (d[0] == rool):
            found = True
            nn = input("New Name:")
            ne = input("New email:")
            np = input("New phone number:")
            ncg = input("Enter the new cg:")
            file.writelines(d[0]+"\t"+nn+"\t"+ne+"\t"+np+"\t"+ncg+"\n")
        else:
            file.writelines(data)
    file.close()
    if found:
        print("Data was updated")
    else:
        print("The rool number entered in not found in the file")


def search():
    rool = input("Enter the roll number to be searched:")
    file = open(filePath, "r")
    all = file.readlines()  # stores all data in one variable
    file.close()
    found = False
    for data in all:
        d = data.split("\t", 1)
        if d[0] == rool:
            found = True
            foundata = data
    if found:
        print(foundata)
    else:
        print("The roll number entered is not found in the file")


def allData():
    print("The complete data in the file is:")
    file = open(filePath, "r")
    all = file.readlines()
    file.close()
    for data in all:
        print(data)


def main():
    print("Welcome to student details portal")

    while (True):
        print("1.Add new studnet")
        print("2.remove a student")
        print("3.Update details of a studnet")
        print("4.Search studnet")
        print("5.Display all students")
        print("6.Exit")
        op = int(input("Enter the choie form above menu:"))
        if op == 1:
            add()
        elif op == 2:
            delete()
        elif op == 3:
            update()
        elif op == 4:
            search()
        elif op == 5:
            allData()
        elif op == 6:
            print("exit sucessfull")
            break
        else:
            print("inavlid Input")


main()
