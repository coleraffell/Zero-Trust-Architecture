import subprocess
import sqlite3

IoT1 = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT1.exe'
IoT1Anom = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\COMP321720212022CW2B\\IoT1_anomaly.exe'

def getIoT1Anom(file):
    p = subprocess.Popen(file, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print "IoT 1 Anomaly:"
    print "Command output : ", output
    storeOutput(1, output)
    #print "Command exit status/return code : ", p_status

def getIoT1(file):
    p = subprocess.Popen(file, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print "IoT 1:"
    print "Command output : ", output
    #print "Command exit status/return code : ", p_status

def createDataBase():
    c.execute("""CREATE TABLE IoT1 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT2 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT3 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT4 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT5 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT6 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT7 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT8 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT9 (
            Input integer,
            Call IoT integer,
            Output integer)""")
    c.execute("""CREATE TABLE IoT10 (
            Input integer,
            Call IoT integer,
            Output integer)""")

def storeOutput(IoT, output):
    print "Storing output for IoT device: " + IoT



database = 'C:\\Users\\cole_\\OneDrive\\Desktop\\Uni of Southampton\\Semester 6\\Security of Cyber Physical Systems\\CW2 - B\\IoT.db'
print "Connecting to DB"
conn = sqlite3.connect(database)
c = conn.cursor()
print "Connected!"
#createDataBase()
conn.commit()
conn.close()

while 1:
    print "1 for IoT 1"
    print "2 for IoT 1 anomaly"
    answer = raw_input("Enter: ")
    print ""
    if answer == '1':
        getIoT1(IoT1)
        # Add fields into database
    if answer == '2':
        getIoT1Anom(IoT1Anom)

