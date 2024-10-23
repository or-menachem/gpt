IR_V15.onPressEvent(RemoteButton.CH_MINUS, function () {
    Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
})
IR_V15.onPressEvent(RemoteButton.CH, function () {
    Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
})
IR_V15.onPressEvent(RemoteButton.CH_Add, function () {
    Tinybit.RGB_Car_Big(Tinybit.enColor.Blue)
})
IR_V15.init(Pins.P8)
