let Messege1 = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Messege1 += -1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendString("" + ("" + Messege1))
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Messege1 += 1
})
basic.forever(function on_forever() {
    basic.showNumber(Messege1)
})
