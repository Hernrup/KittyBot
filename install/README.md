http://raspberrypi-aa.github.io/session2/pwm-servo.html

Installing Servoblaster:
1. git clone /github.com/richardghirst/PiBits.git or use included ziped sourcecode
2. cd PiBits/ServoBlaster/user 
3. make 
4. sudo make install 
5. Verify that servoblaster is installed: ls /dev/servoblaster 

Servoblaster is controlled by writing into the /dev/servoblaster file. The content is written as <servo-number>=<servo-position>. The first field written is the servo number. The following table shows which output pin each servo channel is connected to.

Servo number	GPIO number	Pin in P1 header
0	4	P1-7
1	17	P1-11
2	18	P1-12
3	21/27	P1-13
4	22	P1-15
5	23	P1-16
6	24	P1-18
7	25	P1-22
The allowable position values depend on your servo, for mine values between 80 and 249 were accepted. The servo specification often provides the number of steps the servo supports.
Source Code
#!/usr/bin/env python
#
#
# Drives Servoblaster controlled servo
# https://github.com/richardghirst/PiBits/tree/master/ServoBlaster
#


import time

# From /dev/servoblaster.cfg:
# Servo Channel 0 => GPIO 4
servoChannel = 2

def setServo(servoChannel, position):
    
    servoStr ="%u=%u\n" % (servoChannel, position)

    
    with open("/dev/servoblaster", "wb") as f:
        f.write(servoStr)
                
    

if __name__ == '__main__':
    val = 50
    direction = 1
    while True:
        #print val
        setServo(servoChannel, val)
        time.sleep(.01)
    
        if val == 249:
            direction -= 1
        elif val == 50:
            direction = 1

        val += direction