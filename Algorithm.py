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
        resultString = "     Anomaly!"
        with open("output2.txt", "a") as myFile:
            myFile.write(resultString+"\n")
        print resultString
    else:
        resultString = "     Safe!"
        with open("output2.txt", "a") as myFile:
            myFile.write(resultString+"\n")
        print resultString


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
# inputFile = sys.argv[1]

files = []


for i in range(1, 11):
    files.append("IoT1.exe")
for i in range(1, 11):
    files.append("IoT1_anomaly.exe")
for i in range(1, 11):
    files.append("IoT2.exe")
for i in range(1, 11):
    files.append("IoT2_anomaly.exe")
for i in range(1, 11):
    files.append("IoT3.exe")
for i in range(1, 11):
    files.append("IoT3_anomaly.exe")
for i in range(1, 11):
    files.append("IoT4.exe")
for i in range(1, 11):
    files.append("IoT4_anomaly.exe")
for i in range(1, 11):
    files.append("IoT5.exe")
for i in range(1, 11):
    files.append("IoT5_anomaly.exe")
for i in range(1, 11):
    files.append("IoT6.exe")
for i in range(1, 11):
    files.append("IoT6_anomaly.exe")
for i in range(1, 11):
    files.append("IoT7.exe")
for i in range(1, 11):
    files.append("IoT7_anomaly.exe")
for i in range(1, 11):
    files.append("IoT8.exe")
for i in range(1, 11):
    files.append("IoT8_anomaly.exe")
for i in range(1, 11):
    files.append("IoT9.exe")
for i in range(1, 11):
    files.append("IoT9_anomaly.exe")
for i in range(1, 11):
    files.append("IoT10.exe")
for i in range(1, 11):
    files.append("IoT10_anomaly.exe")


print str(files)

with open("output2.txt", "a") as myFile:

    for i in files:
        myFile.write(i)
        if i == 'IoT1.exe':
            string = "IoT1: "
            print string
            getIoT(i, 1)

        if i == 'IoT1_anomaly.exe':
            string = "IoT1_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 1)

        if i == 'IoT2.exe':
            string = "IoT2: "
            myFile.write(string+"\n")
            print string
            getIoT(i, 2)

        if i == 'IoT2_anomaly.exe':
            string = "IoT2_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 2)

        if i == 'IoT3.exe':
            string = "IoT3: "
            myFile.write(string+"\n")
            print string
            getIoT(i, 3)

        if i == 'IoT3_anomaly.exe':
            string = "IoT3_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 3)

        if i == 'IoT4.exe':
            string = "IoT4: "
            myFile.write(string+"\n")
            print string
            getIoT(i, 4)

        if i == 'IoT4_anomaly.exe':
            string = "IoT4_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 4)

        if i == 'IoT5.exe':
            string = "IoT5: "
            print string
            getIoT(i, 5)

        if i == 'IoT5_anomaly.exe':
            string = "IoT5_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 5)

        if i == 'IoT6.exe':
            string = "IoT6: "
            myFile.write(string+"\n")
            print string
            getIoT(i, 6)

        if i == 'IoT6_anomaly.exe':
            string = "IoT6_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 6)

        if i == 'IoT7.exe':
            string = "IoT7: "
            myFile.write(string+"\n")
            print string
            getIoT(i, 7)

        if i == 'IoT7_anomaly.exe':
            string = "IoT7_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 7)

        if i == 'IoT8.exe':
            string = "IoT8: "
            myFile.write(string+"\n")
            print string
            getIoT(i, 8)

        if i == 'IoT8_anomaly.exe':
            string = "IoT8_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 8)

        if i == 'IoT9.exe':
            string = "IoT9: "
            myFile.write(string+"\n")
            print string
            getIoT(i, 9)

        if i == 'IoT9_anomaly.exe':
            string = "IoT9_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 9)

        if i == 'IoT10.exe':
            string = "IoT10: "
            myFile.write(string+"\n")
            print string
            getIoT(i, 10)

        if i == 'IoT10_anomaly.exe':
            string = "IoT10_anomaly:  "
            myFile.write(string+"\n")
            print string
            getIoT(i, 10)






