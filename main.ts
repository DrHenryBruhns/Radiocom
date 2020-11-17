input.onButtonPressed(Button.A, function () {
    sendQueue.push("TIM:")
})
input.onButtonPressed(Button.B, function () {
    sendQueue.push("DAT:")
})
let msgData = ""
let msgType = ""
let serialInput = ""
let display_Queue: string[] = []
let sendQueue: string[] = []
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate19200
)
basic.forever(function () {
    while (sendQueue.length > 0) {
        serial.writeLine("" + (sendQueue.shift()))
    }
})
basic.forever(function () {
    while (display_Queue.length > 0) {
        basic.showString("" + (display_Queue.shift()))
    }
})
basic.forever(function () {
    serialInput = serial.readUntil(serial.delimiters(Delimiters.NewLine))
    if (serialInput.length >= 4 && serialInput.charAt(3) == ":") {
        msgType = serialInput.substr(0, 3)
        msgData = serialInput.substr(4, serialInput.length - 4)
        if (msgType == "TIM") {
            display_Queue.push(msgData)
        } else if (msgType == "DAT") {
            display_Queue.push(msgData)
        } else if (msgType == "CMP") {
            sendQueue.push("CMP:" + input.compassHeading())
        }
    }
})
