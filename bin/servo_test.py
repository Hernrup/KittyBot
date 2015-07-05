import time

# From /dev/servoblaster.cfg:
# Servo Channel 0 => GPIO 4
servo_channel = 2


def set_servo(servo_channel_, position):

    servo_str = "%u=%u\n" % (servo_channel_, position)

    with open("/dev/servoblaster", "wb") as f:
        f.write(servo_str)


if __name__ == '__main__':
    val = 50
    direction = 1
    while True:
        # print val
        set_servo(servo_channel, val)
        time.sleep(.01)

        if val == 249:
            direction -= 1
        elif val == 50:
            direction = 1

        val += direction