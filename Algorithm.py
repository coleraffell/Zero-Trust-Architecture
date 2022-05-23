import subprocess
import sqlite3
import math

database = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\DataCollect.db'
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


def getIoT(inputFile, IoT):
    print "IOT: " + str(IoT)
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
    if not numInputsSafe:
        print "Number of inputs: anomaly"
    bools.append(numInputsSafe)

    numCalls = len(callArray)
    numCallsSafe = compareNumCalls(IoTDevice, numCalls)
    if not numCallsSafe:
        print "Number of calls: anomaly"
    bools.append(numCallsSafe)

    highestInput = max(inputArray)
    inputSizeSafe = compareHighestInput(IoTDevice, highestInput)
    if not inputSizeSafe:
        print "Input size: anomaly"
    bools.append(inputSizeSafe)

    output = outputArray[1]
    outputSizeIsSafe = compareOutputs(IoTDevice, output)
    if not outputSizeIsSafe:
        print "Irregular output size: anomaly"
    bools.append(outputSizeIsSafe)

    deviceCalls = getDeviceCalls(callArray)
    deviceCallsAreSafe = compareDeviceCalls(IoTDevice, deviceCalls)
    if not deviceCallsAreSafe:
        print "Device calls: anomaly"
    bools.append(deviceCallsAreSafe)

    deviceParametersSafe = compareDeviceParameters(IoTDevice, deviceCalls, callArray)
    if not deviceParametersSafe:
        print "Device parameters: anomaly"
    bools.append(deviceParametersSafe)

    input_vs_parameter = max(getInputVsParameter(inputArray, getDeviceParameters(callArray)))
    isInputVsParameterSafe = compareInputsParameters(IoTDevice, input_vs_parameter)
    if not isInputVsParameterSafe:
        print "Input vs parameter: anomaly"
    bools.append(isInputVsParameterSafe)

    parameter_vs_output = max(getParameterVsOutput(getDeviceParameters(callArray), output))
    isParameterVsOutputSafe = compareParametersOutputs(IoTDevice, parameter_vs_output)
    if not isParameterVsOutputSafe:
        print "Parameter vs output: anomaly"
    bools.append(isParameterVsOutputSafe)

    inputStandardDeviationSafe = inputStandardDeviation(IoTDevice, inputArray)
    if not inputStandardDeviationSafe:
        print "Input more than 1.5x standard deviation"
    bools.append(inputStandardDeviationSafe)

    if bools.__contains__(False):
        print "Anomaly dataset!"
    else:
        print ""
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


def inputStandardDeviation(IoTDevice, inputs):

    print ""
    print "Input Standard deviation test! "
    print inputs

    maxValuesArray = []
    sumMaxValues = 0

    c.execute("SELECT Highest_Input FROM IoT{}".format(IoTDevice))
    results = c.fetchall()

    for i in results:
        tup = i
        value = tup[0]
        sumMaxValues += value
        maxValuesArray.append(value)

    mean = sumMaxValues/len(maxValuesArray)
    iSubMeanSquaredArray = []

    for i in results:
        tup = i
        value = tup[0]
        iSubtractMean = value - mean
        iSubMeanSquared = iSubtractMean*iSubtractMean
        iSubMeanSquaredArray.append(iSubMeanSquared)

    iSubMeanSquaredTotal = 0
    for i in iSubMeanSquaredArray:
        iSubMeanSquaredTotal += i

    standardDeviation = math.sqrt(iSubMeanSquaredTotal / len(iSubMeanSquaredArray))
    isSafe = []
    for i in inputs:
        if int(i) < mean:
            diff = int(mean) - int(i)
        else:
            diff = int(i) - int(mean)
        diffFromStandardDeviation = diff-standardDeviation
        if diffFromStandardDeviation < 0:
            diffFromStandardDeviation *= -1
        if diffFromStandardDeviation > 1.5*standardDeviation:
            isSafe.append(False)

    if isSafe.__contains__(False):
        return False
    else:
        return True


def getIoTDeviceParameter(IoTDevice, callArray):

    for i in callArray:
        if i[2] == str(IoTDevice):
            return int(i[5])


def getOutput(IoT, output):

    print ""
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
    print "3: run IoT2"
    print "4: run IoT2 anomaly"
    print "5: run IoT3"
    print "6: run IoT3 anomaly"
    print ""

    answer = raw_input('Enter IoT: ')
    if answer == '1':
        getIoT(IoT1, 1)
    if answer == '2':
        getIoT(IoT1Anom, 1)
    if answer == '3':
        getIoT(IoT2, 2)
    if answer == '4':
        getIoT(IoT2Anom, 2)
    if answer == '5':
        getIoT(IoT3, 3)
    if answer == '6':
        getIoT(IoT3Anom, 3)
    if answer == '7':
        getIoT(IoT4, 4)
    if answer == '8':
        getIoT(IoT4Anom, 4)
    if answer == '9':
        getIoT(IoT5, 5)
    if answer == '10':
        getIoT(IoT5Anom, 5)
    if answer == '11':
        getIoT(IoT6, 6)
    if answer == '12':
        getIoT(IoT6Anom, 6)
    if answer == '13':
        getIoT(IoT7, 7)
    if answer == '14':
        getIoT(IoT7Anom, 7)
    if answer == '15':
        getIoT(IoT8, 8)
    if answer == '16':
        getIoT(IoT8Anom, 8)
    if answer == '17':
        getIoT(IoT9, 9)
    if answer == '18':
        getIoT(IoT9Anom, 9)
    if answer == '19':
        getIoT(IoT10, 10)
    if answer == '20':
        getIoT(IoT10Anom, 10)

