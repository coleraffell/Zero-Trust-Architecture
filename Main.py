import subprocess
import sqlite3

database = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\IoT.db'
IoT1 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT1.exe'
IoT1Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT1_anomaly.exe'
IoT2 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT2.exe'
IoT2Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT2_anomaly.exe'
IoT3 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT3.exe'
IoT3Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT3_anomaly.exe'
IoT4 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT4.exe'
IoT4Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT4_anomaly.exe'
IoT5 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT5.exe'
IoT5Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT5_anomaly.exe'
IoT6 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT6.exe'
IoT6Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT6_anomaly.exe'
IoT7 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT7.exe'
IoT7Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT7_anomaly.exe'
IoT8 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT8.exe'
IoT8Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT8_anomaly.exe'
IoT9 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT9.exe'
IoT9Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT9_anomaly.exe'
IoT10 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT10.exe'
IoT10Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT10_anomaly.exe'


def getIoTAnom(file):
    p = subprocess.Popen(file, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print "IoT 1 Anomaly:"
    print "Command output: "
    print output
    #print "Command exit status/return code : ", p_status


def getIoT(file, IoT):
    p = subprocess.Popen(file, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    getOutput(IoT, output)
    #print "Command exit status/return code : ", p_status


def createDataBase():

    c.execute("""CREATE TABLE IoT1 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT1_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT2 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT2_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT3 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT3_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT4 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT4_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT5 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT5_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT6 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT6_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT7 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT7_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT8 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT8_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT9 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT9_CALL (
            Device integer,
            Parameter integer)""")
    c.execute("""CREATE TABLE IoT10 (
            num_inputs integer,
            inputs integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT10_CALL (
            Device integer,
            Parameter integer)""")


def storeIoT1(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT1 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT1 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT1_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(1)


def storeIoT2(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT2 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT2 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT2_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(2)


def storeIoT3(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT3 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT3 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT3_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(3)


def storeIoT4(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT4 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT4 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT4_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(4)


def storeIoT5(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT5 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT5 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT5_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(5)


def storeIoT6(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT6 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT6 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT6_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(6)


def storeIoT7(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT7 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT7 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT7_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(7)


def storeIoT8(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT8 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT8 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT8_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(8)


def storeIoT9(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT9 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT9 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT9_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(9)


def storeIoT10(inputArray, outputArray, callArray):

    a = 0
    for i in inputArray:
        if a == 0:
            c.execute("INSERT INTO IoT10 VALUES (?, ?, ?)", (len(inputArray), inputArray[a], outputArray[1]))
        else:
            c.execute("INSERT INTO IoT10 VALUES (?, ?, ?)", (0, int(inputArray[a]), 0))
        a += 1

    for i in callArray:
        c.execute("INSERT INTO IoT10_CALL VALUES (?, ?)", (i[2], i[5]))

    printDataBase(10)


def getOutput(IoT, output):

    print "IoT device " + str(IoT)
    print "Command output: "
    print output
    print "********"
    splitOutput = output.split()

    # ***** Record input from control centres *****
    inputs = []
    input = False
    for i in splitOutput:
        if i == 'Call':
            input = False
        if i == 'Input':
            input = True
        if input:
            inputs.append(i)
    a = 0
    inputArray = []
    for i in inputs:
        if a > 3:
            inputArray.append(i)
        a += 1

    # ***** Record IoT device calls *****
    callIoT = []
    call = False
    for i in splitOutput:
        if i == 'Output:':
            call = False
        if i == 'Call':
            call = True
        if call:
            callIoT.append(i)
    # Get the specific line
    callArray = []
    # Because call IoT is 6 indexes
    n = 6
    for index in range(0, len(callIoT), n):
        callArray.append(callIoT[index:index+n])

    # ***** Record output *****
    outputArray = []
    output = False
    for i in splitOutput:
        if i == 'Output:':
            output = True
        if output:
            outputArray.append(i)

    if IoT == 1:
        storeIoT1(inputArray, outputArray, callArray)
    if IoT == 2:
        storeIoT2(inputArray, outputArray, callArray)
    if IoT == 3:
        storeIoT3(inputArray, outputArray, callArray)
    if IoT == 4:
        storeIoT4(inputArray, outputArray, callArray)
    if IoT == 5:
        storeIoT5(inputArray, outputArray, callArray)
    if IoT == 6:
        storeIoT6(inputArray, outputArray, callArray)
    if IoT == 7:
        storeIoT7(inputArray, outputArray, callArray)
    if IoT == 8:
        storeIoT8(inputArray, outputArray, callArray)
    if IoT == 9:
        storeIoT9(inputArray, outputArray, callArray)
    if IoT == 10:
        storeIoT10(inputArray, outputArray, callArray)


def printDataBase(IoT_Device):

    if IoT_Device == 1:
        print '***IoT table 1***'
        c.execute("SELECT * FROM IoT1")
        print c.fetchall()
        print '***IoT 1 Call table***'
        c.execute("SELECT * FROM IoT1_CALL")
        print c.fetchall()

    if IoT_Device == 2:
        print '***IoT table 2***'
        c.execute("SELECT * FROM IoT2")
        print c.fetchall()
        print '***IoT 2 Call table***'
        c.execute("SELECT * FROM IoT2_CALL")
        print c.fetchall()

    if IoT_Device == 3:
        print '***IoT table 3***'
        c.execute("SELECT * FROM IoT3")
        print c.fetchall()
        print '***IoT 3 Call table***'
        c.execute("SELECT * FROM IoT3_CALL")
        print c.fetchall()

    if IoT_Device == 4:
        print '***IoT table 4***'
        c.execute("SELECT * FROM IoT4")
        print c.fetchall()
        print '***IoT 4 Call table***'
        c.execute("SELECT * FROM IoT4_CALL")
        print c.fetchall()

    if IoT_Device == 5:
        print '***IoT table 5***'
        c.execute("SELECT * FROM IoT5")
        print c.fetchall()
        print '***IoT 5 Call table***'
        c.execute("SELECT * FROM IoT5_CALL")
        print c.fetchall()

    if IoT_Device == 6:
        print '***IoT table 6***'
        c.execute("SELECT * FROM IoT6")
        print c.fetchall()
        print '***IoT 6 Call table***'
        c.execute("SELECT * FROM IoT6_CALL")
        print c.fetchall()

    if IoT_Device == 7:
        print '***IoT table 7***'
        c.execute("SELECT * FROM IoT7")
        print c.fetchall()
        print '***IoT 7 Call table***'
        c.execute("SELECT * FROM IoT7_CALL")
        print c.fetchall()

    if IoT_Device == 8:
        print '***IoT table 8***'
        c.execute("SELECT * FROM IoT8")
        print c.fetchall()
        print '***IoT 8 Call table***'
        c.execute("SELECT * FROM IoT8_CALL")
        print c.fetchall()

    if IoT_Device == 9:
        print '***IoT table 9***'
        c.execute("SELECT * FROM IoT9")
        print c.fetchall()
        print '***IoT 9 Call table***'
        c.execute("SELECT * FROM IoT9_CALL")
        print c.fetchall()

    if IoT_Device == 10:
        print '***IoT table 10***'
        c.execute("SELECT * FROM IoT10")
        print c.fetchall()
        print '***IoT 10 Call table***'
        c.execute("SELECT * FROM IoT10_CALL")
        print c.fetchall()



print "Connecting to DB"
conn = sqlite3.connect(database)
c = conn.cursor()
print "Connected!"

# Auto fill table
a = 0
fillEach = 0

while 1:

    conn.commit()
    print ''
    print ' ******************** '
    print 'A: ' + str(a)
    print 'Table entries: ' + str(fillEach)
    print ' ******************** '
    print ''

    if a == 1:
        getIoT(IoT1, 1)
    if a == 2:
        getIoT(IoT2, 2)
    if a == 3:
        getIoT(IoT3, 3)
    if a == 4:
        getIoT(IoT4, 4)
    if a == 5:
        getIoT(IoT5, 5)
    if a == 6:
        getIoT(IoT6, 6)
    if a == 7:
        getIoT(IoT7, 7)
    if a == 8:
        getIoT(IoT8, 8)
    if a == 9:
        getIoT(IoT9, 9)
    if a == 10:
        getIoT(IoT10, 10)
    if a == 11:
        print '*****Reset*****'
        a = 0
        fillEach += 1
    if fillEach == 500:
        break
    a += 1
