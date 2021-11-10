angle = 0
servos.P0.set_range(10, 170)

def on_forever():
    global angle
    for index in range(17):
        angle = index * 10 + 10
        servos.P0.set_angle(angle)
        basic.pause(100)
    angle = 170
    for index2 in range(17):
        angle = index2 - 5
        servos.P0.set_angle(angle)
        basic.pause(100)
basic.forever(on_forever)
