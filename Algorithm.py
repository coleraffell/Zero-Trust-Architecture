import subprocess
import sqlite3

database = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\DataCollect.db'
IoT1 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT1.exe'
IoT1_anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT1_anomaly.exe'


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


def getIoTDeviceArray(splitOutput):

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


def getSpecifics(IoTDevice, inputArray, outputArray, callArray):

    bools = []

    numInputs = len(inputArray)
    numInputsSafe = compareNumInputs(IoTDevice, numInputs)
    print numInputsSafe
    bools.append(numInputsSafe)
    print ''

    inputs = str(inputArray)
    print "Inputs: " + inputs
    print ''

    numCalls = len(callArray)
    numCallsSafe = compareNumCalls(IoTDevice, numCalls)
    print numCallsSafe
    bools.append(numCallsSafe)
    print ''

    highestInput = max(inputArray)
    inputSizeSafe = compareHighestInput(IoTDevice, highestInput)
    print inputSizeSafe
    bools.append(inputSizeSafe)
    print ''

    output = outputArray[1]
    outputSizeIsSafe = compareOutputs(IoTDevice, output)
    print outputSizeIsSafe
    bools.append(outputSizeIsSafe)
    print ''

    deviceCalls = getDeviceCalls(callArray)
    deviceCallsAreSafe = compareDeviceCalls(IoTDevice, deviceCalls)
    print deviceCallsAreSafe
    bools.append(deviceCallsAreSafe)
    print ''

    deviceParametersSafe = compareDeviceParameters(IoTDevice, deviceCalls, callArray)
    print deviceParametersSafe
    bools.append(deviceParametersSafe)
    print ''

    input_vs_parameter = max(getInputVsParameter(inputArray, getDeviceParameters(callArray)))
    isInputVsParameterSafe = compareInputsParameters(IoTDevice, input_vs_parameter)
    print isInputVsParameterSafe
    bools.append(isInputVsParameterSafe)
    print ''

    parameter_vs_output = max(getParameterVsOutput(getDeviceParameters(callArray), output))
    isParameterVsOutputSafe = compareParametersOutputs(IoTDevice, parameter_vs_output)
    print isParameterVsOutputSafe
    bools.append(isParameterVsOutputSafe)
    print ''

    if bools.__contains__(False):
        print "Anomaly dataset!"
    else:
        print "Safe!"

    print ""


def compareNumInputs(IoTDevice, numInputs):

    print "Num_Inputs: " + str(numInputs)
    c.execute("SELECT * FROM IoT{} WHERE Num_Inputs={}".format(IoTDevice, numInputs))
    results = c.fetchall()
    lengthResults = len(results)

    if lengthResults >= 1:
        return True
    else:
        return False


def compareNumCalls(IoTDevice, numCalls):

    print "Num_Calls: " + str(numCalls)

    c.execute("SELECT * FROM IoT{} WHERE Num_Calls={}".format(IoTDevice, numCalls))
    results = c.fetchall()
    lengthResults = len(results)
    print "Results database array size: " + str(lengthResults)

    if lengthResults >= 1:
        return True
    else:
        return False


def compareHighestInput(IoTDevice, highestInput):

    print "Highest_Input: " + str(highestInput)

    c.execute("SELECT Highest_Input FROM IoT{} WHERE Highest_Input=(SELECT MAX(Highest_Input) FROM IoT{})".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]
    print value

    if int(highestInput) < int(value):
        return True
    else:
        return False


def compareOutputs(IoTDevice, output):

    print "Output: " + str(output)

    c.execute("SELECT Output FROM IoT{} WHERE Output=(SELECT MAX(Output) FROM IoT{})".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]
    print value

    if int(output) < int(value):
        return True
    else:
        return False


def compareDeviceCalls(IoTDevice, deviceCalls):

    print "Device calls: " + str(deviceCalls)
    bools = []

    for i in deviceCalls:
        c.execute("SELECT IoT{} FROM IoT{} WHERE IoT{}='1'".format(int(i), IoTDevice, int(i)))
        results = c.fetchall()
        lengthResults = len(results)

        if lengthResults == 0:
            print "This call has not been made before"
            bools.append(False)

    if bools.__contains__(False):
        return False
    else:
        return True


def compareDeviceParameters(IoTDevice, deviceCalls, callArray):

    print "Device calls: " + str(deviceCalls)
    bools = []

    for i in deviceCalls:
        param = getIoTDeviceParameter(int(i), callArray)
        c.execute("SELECT IoT{} FROM IoT{}_Calls WHERE IoT{}=(SELECT MAX(IoT{}) FROM IoT{}_Calls)".format(int(i), IoTDevice, int(i), int(i), IoTDevice))
        results = c.fetchall()
        tup = results[0]
        value = tup[0]

        if param < value:
            bools.append(True)
        else:
            print "Parameter hasn't been this high before"
            bools.append(False)

    if bools.__contains__(False):
        return False
    else:
        return True


def compareInputsParameters(IoTDevice, inputsVsParameters):

    print "Highest difference between Input and parameter: " + str(inputsVsParameters)

    c.execute("SELECT Input_vs_Parameters FROM IoT{}_Calls WHERE Input_vs_Parameters=(SELECT MAX(Input_vs_Parameters) FROM IoT{}_Calls)".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]
    print value

    if int(inputsVsParameters) < int(value):
        return True
    else:
        return False


def compareParametersOutputs(IoTDevice, parametersVsOutputs):

    print "Highest difference between Parameter and Output: " + str(parametersVsOutputs)

    c.execute("SELECT Parameter_vs_Output FROM IoT{}_Calls WHERE Parameter_vs_Output=(SELECT MAX(Parameter_vs_Output) FROM IoT{}_Calls)".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]
    print value

    if int(parametersVsOutputs) < int(value):
        return True
    else:
        return False


def getIoTDeviceParameter(IoTDevice, callArray):

    for i in callArray:
        if i[2] == str(IoTDevice):
            return int(i[5])


def getOutput(IoT, output):

    print "IoT device " + str(IoT)
    print "Command output: "
    print output
    print "********"
    splitOutput = output.split()

    inputArray = getIoTInputs(splitOutput)
    callArray = getIoTDeviceArray(splitOutput)
    outputArray = getIoTOutputs(splitOutput)

    getSpecifics(IoT, inputArray, outputArray, callArray)


def printDataBase(IoT_Device):

    print '***IoT table {}***'.format(IoT_Device)
    c.execute("SELECT * FROM IoT{}".format(IoT_Device))
    print c.fetchall()
    print '***IoT {} Call table***'.format(IoT_Device)
    c.execute("SELECT * FROM IoT{}_Calls".format(IoT_Device))
    print c.fetchall()


conn = sqlite3.connect(database)
c = conn.cursor()

while 1:

    print "1: run IoT1"
    print "2: run IoT1 anomaly"
    print "3: print IoT1 tables"
    answer = raw_input('Enter IoT: ')
    if answer == '1':
        getIoT(IoT1, 1)
    if answer == '2':
        getIoT(IoT1_anom, 1)
    if answer == '3':
        printDataBase(1)
