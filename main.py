Messege1 = 0

def on_button_pressed_a():
    global Messege1
    Messege1 += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("" + str(Messege1))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global Messege1
    Messege1 += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_number(Messege1)
basic.forever(on_forever)
