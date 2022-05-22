import subprocess
import sqlite3

database = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\DataCollect.db'
IoT1 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT1.exe'
IoT1_anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT1_anomaly.exe'
IoT2 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT2.exe'
IoT3 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT3.exe'
IoT4 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT4.exe'
IoT5 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT5.exe'
IoT6 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT6.exe'
IoT7 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT7.exe'
IoT8 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT8.exe'
IoT9 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT9.exe'
IoT10 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT10.exe'


def getIoT(inputFile, IoT):
    p = subprocess.Popen(inputFile, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    getOutput(IoT, output)
    # print "Command exit status/return code : ", p_status


def getIoTInputs(splitOutput):

    # ***** Record input from control centres *****
    inputs = []
    inputBool = False
    for i in splitOutput:
        if i == 'Call':
            inputBool = False
        if i == 'Input':
            inputBool = True
        if inputBool:
            inputs.append(i)
    a = 0
    inputArray = []
    for i in inputs:
        if a > 3:
            inputArray.append(i)
        a += 1
    return inputArray


def getDeviceArray(splitOutput):

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

    return callArray


def getIoTOutputs(splitOutput):

    # ***** Record output *****
    outputArray = []
    output = False
    for i in splitOutput:
        if i == 'Output:':
            output = True
        if output:
            outputArray.append(i)

    return outputArray


def getDeviceCalls(callArray):

    deviceCalls = []
    for i in callArray:
        deviceCalls.append(i[2])

    return deviceCalls


def getDeviceParameters(callArray):

    deviceCalls = []
    for i in callArray:
        deviceCalls.append(i[5])

    return deviceCalls


def getInputVsParameter(inputList, paramList):

    listResult = []

    for i in inputList:
        for a in paramList:
            result = int(i) - int(a)
            if result < 0:
                result *= -1
                listResult.append(result)
            else:
                listResult.append(result)

    return listResult


def getParameterVsOutput(paramList, output):

    listResult = []

    for i in paramList:

        result = int(i) - int(output)
        if result < 0:
            result *= -1
            listResult.append(result)
        else:
            listResult.append(result)

    return listResult


def storeIoT(IoTDevice, inputArray, outputArray, callArray):

    IoT = "IoT"+str(IoTDevice)
    IoT_Calls = IoT + "_Calls"
    print "storing: " + IoT + ", " + IoT_Calls

    print inputArray
    print outputArray
    print callArray

    numInputs = len(inputArray)
    inputs = str(inputArray)
    numCalls = len(callArray)
    highestInput = max(inputArray)
    output = outputArray[1]
    deviceCalls = getDeviceCalls(callArray)

    c.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(IoT), (numInputs, inputs,
        numCalls, highestInput, output, deviceCalls.__contains__("1"), deviceCalls.__contains__("2"),
        deviceCalls.__contains__("3"), deviceCalls.__contains__("4"), deviceCalls.__contains__("5"),
        deviceCalls.__contains__("6"), deviceCalls.__contains__("7"), deviceCalls.__contains__("8"),
        deviceCalls.__contains__("9"), deviceCalls.__contains__("10")))

    input_vs_parameter = max(getInputVsParameter(inputArray, getDeviceParameters(callArray)))
    parameter_vs_output = max(getParameterVsOutput(getDeviceParameters(callArray), output))

    c.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(IoT_Calls), (input_vs_parameter,
        parameter_vs_output, getIoTDeviceParameter(1, callArray), getIoTDeviceParameter(2, callArray),
        getIoTDeviceParameter(3, callArray), getIoTDeviceParameter(4, callArray), getIoTDeviceParameter(5, callArray),
        getIoTDeviceParameter(6, callArray), getIoTDeviceParameter(7, callArray), getIoTDeviceParameter(8, callArray),
        getIoTDeviceParameter(9, callArray), getIoTDeviceParameter(10, callArray)))

    printDataBase(IoTDevice)


def getIoTDeviceParameter(IoTDevice, callArray):

    for i in callArray:
        if i[2] == str(IoTDevice):
            return int(i[5])


def printDataBase(IoT_Device):

    print '***IoT table {}***'.format(IoT_Device)
    c.execute("SELECT * FROM IoT{}".format(IoT_Device))
    print c.fetchall()
    print '***IoT {} Call table***'.format(IoT_Device)
    c.execute("SELECT * FROM IoT{}_Calls".format(IoT_Device))
    print c.fetchall()


def getOutput(IoT, output):

    print "IoT device " + str(IoT)
    print "Command output: "
    print output
    print "********"
    splitOutput = output.split()

    inputArray = getIoTInputs(splitOutput)
    callArray = getDeviceArray(splitOutput)
    outputArray = getIoTOutputs(splitOutput)

    storeIoT(IoT, inputArray, outputArray, callArray)


def createDataBase():

    # Looping through to create all tables at once
    for i in range(1, 11):
        string = "IoT" + str(i)
        stringCall = "IoT" + str(i) + "_Calls"
        c.execute("""CREATE TABLE {} (
                Num_Inputs integer,
                Inputs text,
                Num_Calls integer,
                Highest_Input integer,
                Output integer,
                IoT1 bool,
                IoT2 bool,
                IoT3 bool,
                IoT4 bool,
                IoT5 bool,
                IoT6 bool,
                IoT7 bool,
                IoT8 bool,
                IoT9 bool,
                IoT10 bool)""".format(string))
        c.execute("""CREATE TABLE {} (
                Input_vs_Parameters integer,
                Parameter_vs_Output integer,
                IoT1 integer,
                IoT2 integer,
                IoT3 integer,
                IoT4 integer,
                IoT5 integer,
                IoT6 integer,
                IoT7 integer,
                IoT8 integer,
                IoT9 integer,
                IoT10 integer)""".format(stringCall))


conn = sqlite3.connect(database)
c = conn.cursor()
# createDataBase()

# Auto fill table
a = 0
fillEach = 0

while 1:

    conn.commit()
    # answer = raw_input('Enter IoT: ')
    print "a: " + str(a)
    print "Fill each: " + str(fillEach)
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
    a += 1
    if a == 11:
        fillEach += 1
        a = 0
    if fillEach == 200:
        print "200 table entries executed!"
        break



