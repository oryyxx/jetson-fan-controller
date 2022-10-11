import os
import time

#------------------ Configuration ------------------ 
tempTable = []
tempTable.append((20, 50)) #(temp, pwm (0-255)) 
tempTable.append((30, 100))
tempTable.append((40, 150))
tempTable.append((50, 200))
tempTable.append((60, 255))

#how long should the program check temp and set fan speed (in seconds)
period = 5
#----------------------------------------------------

tempfile = "/sys/class/thermal/thermal_zone0/temp"
pwmfile = "/sys/devices/pwm-fan/target_pwm"

if not os.path.exists(tempfile):
    raise Exception(f"Could not find: {tempfile}")

if not os.path.exists(pwmfile):
    raise Exception(f"Could not find: {pwmfile}")

def setPWM(pwm):

    if pwm < 0 or pwm > 255:
        print('pwm value should be between 0-255')

    pwm = round(pwm)
    with open("/sys/devices/pwm-fan/target_pwm","w") as targetfile:
        targetfile.write(str(pwm))

def readTemp():

    with open("/sys/class/thermal/thermal_zone0/temp","r") as tempfile:
        temp = int(tempfile.read(10)) / 1000

    return temp

def main():

    while True:

        temp = readTemp()

        for t in tempTable:

            if temp > t[0]:
                setPWM(t[1])

        with open("/sys/devices/pwm-fan/target_pwm","r") as pwmfile:
            pwm = pwmfile.read()

        print(f"temp: {temp}c ,pwm: {pwm}")
        time.sleep(period)

if __name__ == '__main__':
    main()
