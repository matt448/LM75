import LM75

sensor1 = LM75.LM75()
sensor1.i2c_address = 0x48

sensor2 = LM75.LM75()
sensor2.i2c_address = 0x49


print("temp_c:", sensor1.getCelsius())
print("temp_f:", sensor1.getFahrenheit())
print("----------------------------------")


#print("temp_c:", sensor2.getCelsius())
#print("----------------------------------")