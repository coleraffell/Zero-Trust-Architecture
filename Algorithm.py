import subprocess
import sqlite3
import math
import sys

database = 'DataCollect.db'
string = ''


# This method takes the command line file and runs it, sending the output to getOutput

def getIoT(inputFile, IoT):

    p = subprocess.Popen(inputFile, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    getOutput(IoT, output)
    # print "Command exit status/return code : ", p_status


# Method is given device output and uses booleans to iterate through string array to find device inputs

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


# Method is given device output and uses booleans to iterate through string array to find device calls

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


# Method is given device output and uses booleans to iterate through string array to find device outputs

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


# Method establishes which IoT devices have been called from current IoT device

def getDeviceCalls(callArray):

    # i[2] is always IoT device number
    deviceCalls = []
    for i in callArray:
        deviceCalls.append(i[2])

    return deviceCalls


# Method establishes parameters used for IoT device calls

def getDeviceParameters(callArray):

    # i[5] is always parameter
    deviceCalls = []
    for i in callArray:
        deviceCalls.append(i[5])

    return deviceCalls


# Method iterates through each element of each int list and finds the biggest difference between any two numbers

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


# Method iterates through each element of each int list and finds the biggest difference between any two numbers

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


# The main method. Ensuring there are no anomalies bit by bit

def getSpecifics(IoTDevice, inputArray, outputArray, callArray):

    bools = []

    # Ensure the number of inputs isn't irregular
    numInputs = len(inputArray)
    numInputsSafe = compareNumInputs(IoTDevice, numInputs)
    bools.append(numInputsSafe)

    # Ensure number of calls isn't irregular
    numCalls = len(callArray)
    numCallsSafe = compareNumCalls(IoTDevice, numCalls)
    bools.append(numCallsSafe)

    # Ensure highest input in current IoT device isn't irregular
    highestInput = max(inputArray)
    inputSizeSafe = compareHighestInput(IoTDevice, highestInput)
    bools.append(inputSizeSafe)

    # Ensure output size isn't irregular
    output = outputArray[1]
    outputSizeIsSafe = compareOutputs(IoTDevice, output)
    bools.append(outputSizeIsSafe)

    # Ensure IoT device calls have been made before. I.e., device 1 doesn't call device 8
    deviceCalls = getDeviceCalls(callArray)
    deviceCallsAreSafe = compareDeviceCalls(IoTDevice, deviceCalls)
    bools.append(deviceCallsAreSafe)

    # Ensure device parameters aren't irregular
    deviceParametersSafe = compareDeviceParameters(IoTDevice, deviceCalls, callArray)
    bools.append(deviceParametersSafe)

    # Ensure not too much of a difference between input & parameter
    input_vs_parameter = max(getInputVsParameter(inputArray, getDeviceParameters(callArray)))
    isInputVsParameterSafe = compareInputsParameters(IoTDevice, input_vs_parameter)
    bools.append(isInputVsParameterSafe)

    # Ensure not too much of a difference between parameter & output
    parameter_vs_output = max(getParameterVsOutput(getDeviceParameters(callArray), output))
    isParameterVsOutputSafe = compareParametersOutputs(IoTDevice, parameter_vs_output)
    bools.append(isParameterVsOutputSafe)

    # Ensure the inputs are within 2 standard deviations of data set
    inputStandardDeviationSafe = inputStandardDeviation(IoTDevice, inputArray)
    bools.append(inputStandardDeviationSafe)

    outputStandardDeviationSafe = outputStandardDeviation(IoTDevice, int(output))
    bools.append(outputStandardDeviationSafe)

    parameterStandardDeviationSafe = parameterStandardDeviation(IoTDevice, deviceCalls, callArray)
    bools.append(parameterStandardDeviationSafe)

    # Check if any of the above checks returned False
    if bools.__contains__(False):
        print "Anomaly!"
    else:
        print "Safe!"


# Query device database to check if device has received that many inputs before

def compareNumInputs(IoTDevice, numInputs):

    c.execute("SELECT * FROM IoT{} WHERE Num_Inputs={}".format(IoTDevice, numInputs))
    results = c.fetchall()
    lengthResults = len(results)

    if lengthResults >= 1:
        return True
    else:
        return False


# Query device database to check if device has sent that many calls before

def compareNumCalls(IoTDevice, numCalls):

    c.execute("SELECT * FROM IoT{} WHERE Num_Calls={}".format(IoTDevice, numCalls))
    results = c.fetchall()
    lengthResults = len(results)

    if lengthResults >= 1:
        return True
    else:
        return False


# Query device database to compare the highest input with database highest recorded input

def compareHighestInput(IoTDevice, highestInput):

    c.execute("SELECT Highest_Input FROM IoT{} WHERE Highest_Input=(SELECT MAX(Highest_Input) FROM IoT{})".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]

    if int(highestInput) < int(value):
        return True
    else:
        return False


# Query device database to compare the highest output with database highest recorded output

def compareOutputs(IoTDevice, output):

    c.execute("SELECT Output FROM IoT{} WHERE Output=(SELECT MAX(Output) FROM IoT{})".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]

    if int(output) < int(value):
        return True
    else:
        return False


# Query database to check if device calls have been made before

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


# Query device database to check if device call parameters have previously been this high

def compareDeviceParameters(IoTDevice, deviceCalls, callArray):

    bools = []

    for i in deviceCalls:
        param = getIoTDeviceParameter(int(i), callArray)
        c.execute("SELECT IoT{} FROM IoT{}_Calls WHERE IoT{}=(SELECT MAX(IoT{}) FROM IoT{}_Calls)".format(int(i), IoTDevice, int(i), int(i), IoTDevice))
        results = c.fetchall()

        if len(results) > 0:
            tup = results[0]
            value = tup[0]

            if param < value:
                bools.append(True)
            else:
                bools.append(False)
        else:
            "print ''"

    if bools.__contains__(False):
        return False
    else:
        return True


# Query database to ensure the difference between input and device parameters isn't too high

def compareInputsParameters(IoTDevice, inputsVsParameters):

    c.execute("SELECT Input_vs_Parameters FROM IoT{}_Calls WHERE Input_vs_Parameters=(SELECT MAX(Input_vs_Parameters) FROM IoT{}_Calls)".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]

    if int(inputsVsParameters) < int(value):
        return True
    else:
        return False


# Query database to ensure the difference between call parameters and the output isn't too high

def compareParametersOutputs(IoTDevice, parametersVsOutputs):

    c.execute("SELECT Parameter_vs_Output FROM IoT{}_Calls WHERE Parameter_vs_Output=(SELECT MAX(Parameter_vs_Output) FROM IoT{}_Calls)".format(IoTDevice, IoTDevice))
    results = c.fetchall()
    tup = results[0]
    value = tup[0]

    if int(parametersVsOutputs) < int(value):
        return True
    else:
        return False


# Method to calculate if the current inputs are outside of 2 standard deviations

def inputStandardDeviation(IoTDevice, inputs):

    maxValuesArray = []
    sumMaxValues = 0

    # This needs to be average of all inputs
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
        if diff > 1.8*standardDeviation:
            isSafe.append(False)

    if isSafe.__contains__(False):
        return False
    else:
        return True


def outputStandardDeviation(IoTDevice, output):

    maxValuesArray = []
    sumMaxValues = 0

    # This needs to be average of all inputs
    c.execute("SELECT Output FROM IoT{}".format(IoTDevice))
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

    if output < mean:
        diff = int(mean) - output
    else:
        diff = output - int(mean)
    if diff > 1.8*standardDeviation:
        isSafe.append(False)

    if isSafe.__contains__(False):
        return False
    else:
        return True


def parameterStandardDeviation(IoTDevice, deviceCalls, callArray):

    isSafe = []
    valuesArray = []
    sumValues = 0

    for i in deviceCalls:
        for a in callArray:
            if a[2] == i:
                # This is where standard deviation needs to happen
                # Select column from device
                c.execute("SELECT IoT{} FROM IoT{}_Calls".format(a[2], IoTDevice))
                results = c.fetchall()
                # Take the sum of the values
                for b in results:
                    tup = b
                    value = tup[0]
                    if value is None:
                        "print 'None type'"
                    else:
                        sumValues += value
                        valuesArray.append(value)

                # Calculate the mean
                if len(valuesArray) > 0:
                    mean = sumValues/len(valuesArray)
                else:
                    break
                iSubMeanSquaredArray = []
                for b in results:
                    tup = b
                    value = tup[0]
                    if value is None:
                        "print 'None type'"
                    else:
                        iSubtractMean = value - mean
                        iSubMeanSquared = iSubtractMean*iSubtractMean
                        iSubMeanSquaredArray.append(iSubMeanSquared)

                iSubMeanSquaredTotal = 0
                for b in iSubMeanSquaredArray:
                    iSubMeanSquaredTotal += b

                standardDeviation = math.sqrt(iSubMeanSquaredTotal / len(iSubMeanSquaredArray))
                parameter = a[5]

                if int(parameter) < mean:
                    diff = int(mean) - int(parameter)
                else:
                    diff = int(parameter) - int(mean)
                if diff > 1.8*standardDeviation:
                    isSafe.append(False)

    if isSafe.__contains__(False):
        return False
    else:
        return True


def getIoTDeviceParameter(IoTDevice, callArray):

    for i in callArray:
        if i[2] == str(IoTDevice):
            return int(i[5])


# method is given device output, makes use of get methods to pull specific parts

def getOutput(IoT, output):

    splitOutput = output.split()
    inputArray = getIoTInputs(splitOutput)
    callArray = getIoTDeviceArray(splitOutput)
    outputArray = getIoTOutputs(splitOutput)
    getSpecifics(IoT, inputArray, outputArray, callArray)


# Testing method to ensure database works

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
inputFile = sys.argv[1]

if inputFile.__contains__('T1'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 1)
    else:
        string = "Normal: "
        getIoT(inputFile, 1)

if inputFile.__contains__('2'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 2)
    else:
        string = "Normal: "
        getIoT(inputFile, 2)

if inputFile.__contains__('3'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 3)
    else:
        string = "Normal: "
        getIoT(inputFile, 3)

if inputFile.__contains__('4'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 4)
    else:
        string = "Normal: "
        getIoT(inputFile, 4)

if inputFile.__contains__('5'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 5)
    else:
        string = "Normal: "
        getIoT(inputFile, 5)

if inputFile.__contains__('6'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 6)
    else:
        string = "Normal: "
        getIoT(inputFile, 6)

if inputFile.__contains__('7'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 7)
    else:
        string = "Normal: "
        getIoT(inputFile, 7)

if inputFile.__contains__('8'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 8)
    else:
        string = "Normal: "
        getIoT(inputFile, 8)

if inputFile.__contains__('9'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 9)
    else:
        string = "Normal: "
        getIoT(inputFile, 9)

elif inputFile.__contains__('10'):
    if inputFile.__contains__('anomaly'):
        string = "Anomaly: "
        getIoT(inputFile, 10)
    else:
        string = "Normal: "
        getIoT(inputFile, 10)


"""
while 1:

    # inputFile = raw_input('Enter IoT file: ')

    if inputFile.__contains__('T1'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 1)
        else:
            string = "Normal: "
            getIoT(inputFile, 1)

    if inputFile.__contains__('2'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 2)
        else:
            string = "Normal: "
            getIoT(inputFile, 2)

    if inputFile.__contains__('3'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 3)
        else:
            string = "Normal: "
            getIoT(inputFile, 3)

    if inputFile.__contains__('4'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 4)
        else:
            string = "Normal: "
            getIoT(inputFile, 4)

    if inputFile.__contains__('5'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 5)
        else:
            string = "Normal: "
            getIoT(inputFile, 5)

    if inputFile.__contains__('6'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 6)
        else:
            string = "Normal: "
            getIoT(inputFile, 6)

    if inputFile.__contains__('7'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 7)
        else:
            string = "Normal: "
            getIoT(inputFile, 7)

    if inputFile.__contains__('8'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 8)
        else:
            string = "Normal: "
            getIoT(inputFile, 8)

    if inputFile.__contains__('9'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 9)
        else:
            string = "Normal: "
            getIoT(inputFile, 9)

    elif inputFile.__contains__('10'):
        if inputFile.__contains__('anomaly'):
            string = "Anomaly: "
            getIoT(inputFile, 10)
        else:
            string = "Normal: "
            getIoT(inputFile, 10)

    print "  - " + string
"""

