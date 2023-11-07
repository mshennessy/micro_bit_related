
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)



import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM4'

ser.open()
file = open("temperatures_from_microbit.csv",'a')
# use while True: for forever ...
# but it's easier to set a limit for testing
countData = 0
while (countData < 100):
    data = str(ser.readline())
    print (data)
    data = data.replace("b","")
    data = data.replace(" ","")
    data = data.replace("'","")
    #separating \r and \n seems to work better
    data = data.replace("\\r","")
    data = data.replace("\\n","")
    print (data)
    file.write(data+",")
    countData += 1
print ("Finished")
file.close()
    
