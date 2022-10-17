# jetson-fan-controller
A simple script for changing fan PWM(speed) based on temperture.

| Jetson  | Tested |
| ------------- | ------------- |
|  Xavier  |    ✅ |
| Nano |     ✅ |

## Getting Started
Clone the repo
```
git clone https://github.com/oryyxx/jetson-fan-controller.git
```
run the following command in terminal:
```
python3 jetson-fan.py
```

## Configuration
There is no need to configure anything, but if you would like to configure the speed you can do so in the python script file.
```python
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
```
