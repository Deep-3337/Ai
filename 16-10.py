sensor1=dict()
sensor2=dict()
outputcom1=dict()
outputcom2=dict()
outputun=dict()
outputin=dict()
unionop=dict()
interop=dict()

sensor1={"0":0,"20":0.5,"40":0.65,"60":0.85,"80":1,"100":1}
sensor2={"0":0,"20":0.35,"40":0.5,"60":0.75,"80":0.90,"100":1}
# Union set
for sensor1_key,sensor2_key in zip(sensor1,sensor2):
    sensor1_value=sensor1[sensor1_key]
    sensor2_value=sensor2[sensor2_key]
    
    if sensor1_value>sensor2_value:
        outputun[sensor1_key]=sensor1_value
    else:
       outputun[sensor2_key]=sensor2_value
print("Fuzzy Set Union is : ",outputun)

# Intersection set
for sensor1_key,sensor2_key in zip(sensor1,sensor2):
    sensor1_value=sensor1[sensor1_key]
    sensor2_value=sensor2[sensor2_key]
    
    if sensor1_value<sensor2_value:
        outputin[sensor1_key]=sensor1_value
    else:
       outputin[sensor2_key]=sensor2_value
print("Fuzzy Set Intersection is : ",outputin)

# # Compliment of sensor1
for sensor1_key in sensor1:
    outputcom1[sensor1_key]=1-sensor1[sensor1_key]
print("Fuzzy Set Compliment of sensor1 is : ",outputcom1)

# # Compliment of sensor2
for sensor2_key in sensor2:
    outputcom2[sensor2_key]=1-sensor2[sensor2_key]
print("Fuzzy Set Compliment of sensor2 is : ",outputcom2)

# De Morgan Law
# Compliment of Union senor1 and sensor2
for outputun_key in outputun:
    unionop[outputun_key]=1-outputun[outputun_key]
print ("Compliment of Union senor1 and sensor2 is : ",unionop)

# Compliment of intersection senor1 and sensor2

for outputcom1_key,outputcom2_key in zip(outputcom1,outputcom2):
    outputcom1_value=outputcom1[outputcom1_key]
    outputcom2_value=outputcom2[outputcom2_key]
    
    if outputcom1_value<outputcom2_value:
        interop[outputcom1_key]=outputcom1_value
    else:
       interop[outputcom2_key]=outputcom2_value
print("Compliment of intersection senor1 and sensor2 is : ",interop)

# o/p
# Fuzzy Set Union is :  {'0': 0, '20': 0.5, '40': 0.65, '60': 0.85, '80': 1, '100': 1}
# Fuzzy Set Intersection is :  {'0': 0, '20': 0.35, '40': 0.5, '60': 0.75, '80': 0.9, '100': 1}
# Fuzzy Set Compliment of sensor1 is :  {'0': 1, '20': 0.5, '40': 0.35, '60': 0.15000000000000002, '80': 0, '100': 0}
# Fuzzy Set Compliment of sensor2 is :  {'0': 1, '20': 0.65, '40': 0.5, '60': 0.25, '80': 0.09999999999999998, '100': 0}
# Compliment of Union senor1 and sensor2 is :  {'0': 1, '20': 0.5, '40': 0.35, '60': 0.15000000000000002, '80': 0, '100': 0}
# Compliment of intersection senor1 and sensor2 is :  {'0': 1, '20': 0.5, '40': 0.35, '60': 0.15000000000000002, '80': 0, '100': 0}