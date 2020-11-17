def on_button_pressed_a():
    sendQueue.append("TIM:")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sendQueue.append("DAT:")
input.on_button_pressed(Button.B, on_button_pressed_b)

msgData = ""
msgType = ""
serialInput = ""
display_Queue: List[str] = []
sendQueue: List[str] = []
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE19200)

def on_forever():
    while len(sendQueue) > 0:
        serial.write_line("" + (sendQueue.shift()))
basic.forever(on_forever)

def on_forever2():
    while len(display_Queue) > 0:
        basic.show_string("" + (display_Queue.shift()))
basic.forever(on_forever2)

def on_forever3():
    global serialInput, msgType, msgData
    serialInput = serial.read_until(serial.delimiters(Delimiters.NEW_LINE))
    if len(serialInput) >= 4 and serialInput.char_at(3) == ":":
        msgType = serialInput.substr(0, 3)
        msgData = serialInput.substr(4, len(serialInput) - 4)
        if msgType == "TIM":
            display_Queue.append(msgData)
        elif msgType == "DAT":
            display_Queue.append(msgData)
        elif msgType == "CMP":
            sendQueue.append("CMP:" + str(input.compass_heading()))
basic.forever(on_forever3)
