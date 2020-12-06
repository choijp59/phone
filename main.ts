input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (input.magneticForce(Dimension.Strength) >= 150) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . # . #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
    
})
basic.forever(function on_forever() {
    led.plotBarGraph(input.magneticForce(Dimension.Strength), 200)
})
