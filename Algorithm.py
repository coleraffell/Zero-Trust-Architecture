import subprocess
import sqlite3
import math
import sys

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
    bools.append(numInputsSafe)

    numCalls = len(callArray)
    numCallsSafe = compareNumCalls(IoTDevice, numCalls)
    bools.append(numCallsSafe)

    highestInput = max(inputArray)
    inputSizeSafe = compareHighestInput(IoTDevice, highestInput)
    bools.append(inputSizeSafe)

    output = outputArray[1]
    outputSizeIsSafe = compareOutputs(IoTDevice, output)
    bools.append(outputSizeIsSafe)

    deviceCalls = getDeviceCalls(callArray)
    deviceCallsAreSafe = compareDeviceCalls(IoTDevice, deviceCalls)
    bools.append(deviceCallsAreSafe)

    deviceParametersSafe = compareDeviceParameters(IoTDevice, deviceCalls, callArray)
    bools.append(deviceParametersSafe)

    input_vs_parameter = max(getInputVsParameter(inputArray, getDeviceParameters(callArray)))
    isInputVsParameterSafe = compareInputsParameters(IoTDevice, input_vs_parameter)
    bools.append(isInputVsParameterSafe)

    parameter_vs_output = max(getParameterVsOutput(getDeviceParameters(callArray), output))
    isParameterVsOutputSafe = compareParametersOutputs(IoTDevice, parameter_vs_output)
    bools.append(isParameterVsOutputSafe)

    inputStandardDeviationSafe = inputStandardDeviation(IoTDevice, inputArray)
    bools.append(inputStandardDeviationSafe)

    if bools.__contains__(False):
        print "Anomaly!"
    else:
        print "Safe!"


def compareNumInputs(IoTDevice, numInputs):

    c.execute("SELECT * FROM IoT{} WHERE Num_Inputs={}".format(IoTDevice, numInputs))
    results = c.fetchall()
    lengthResults = len(results)

    if lengthResults >= 1:
        return True
    else:
        return False


def compareNumCalls(IoTDevice, numCalls):

    c.execute("SELECT * FROM IoT{} WHERE Num_Calls={}".format(IoTDevice, numCalls))
    results = c.fetchall()
    lengthResults = len(results)

    if lengthResults >= 1:
        return True
    else:
        return False


def compareHighestInput(IoTDevice, highestInput):

    c.execute("SELECT Highest_Input FROM IoT{} WHERE Highest_Input=(SELECT MAX(Highest_Input) FROM IoT{})".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]

    if int(highestInput) < int(value):
        return True
    else:
        return False


def compareOutputs(IoTDevice, output):

    c.execute("SELECT Output FROM IoT{} WHERE Output=(SELECT MAX(Output) FROM IoT{})".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]

    if int(output) < int(value):
        return True
    else:
        return False


def compareDeviceCalls(IoTDevice, deviceCalls):

    bools = []

    for i in deviceCalls:
        c.execute("SELECT IoT{} FROM IoT{} WHERE IoT{}='1'".format(int(i), IoTDevice, int(i)))
        results = c.fetchall()
        lengthResults = len(results)

        if lengthResults == 0:
            bools.append(False)

    if bools.__contains__(False):
        return False
    else:
        return True


def compareDeviceParameters(IoTDevice, deviceCalls, callArray):

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
            bools.append(False)

    if bools.__contains__(False):
        return False
    else:
        return True


def compareInputsParameters(IoTDevice, inputsVsParameters):

    c.execute("SELECT Input_vs_Parameters FROM IoT{}_Calls WHERE Input_vs_Parameters=(SELECT MAX(Input_vs_Parameters) FROM IoT{}_Calls)".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]

    if int(inputsVsParameters) < int(value):
        return True
    else:
        return False


def compareParametersOutputs(IoTDevice, parametersVsOutputs):

    c.execute("SELECT Parameter_vs_Output FROM IoT{}_Calls WHERE Parameter_vs_Output=(SELECT MAX(Parameter_vs_Output) FROM IoT{}_Calls)".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]

    if int(parametersVsOutputs) < int(value):
        return True
    else:
        return False


def inputStandardDeviation(IoTDevice, inputs):

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

# Sys.argv[1] wouldn't work for me. the commented inputFile does though if argv doesn't
inputFile = raw_input('Enter IoT file: ')
# inputFile = sys.argv[1]

if inputFile.__contains__('1'):
    getIoT(inputFile, 1)
if inputFile.__contains__('2'):
    getIoT(inputFile, 2)
if inputFile.__contains__('3'):
    getIoT(inputFile, 3)
if inputFile.__contains__('4'):
    getIoT(inputFile, 4)
if inputFile.__contains__('5'):
    getIoT(inputFile, 5)
if inputFile.__contains__('6'):
    getIoT(inputFile, 6)
if inputFile.__contains__('7'):
    getIoT(inputFile, 7)
if inputFile.__contains__('8'):
    getIoT(inputFile, 8)
if inputFile.__contains__('9'):
    getIoT(inputFile, 9)
if inputFile.__contains__('10'):
    getIoT(inputFile, 10)

