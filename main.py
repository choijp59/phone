def on_button_pressed_a():
    if input.magnetic_force(Dimension.STRENGTH) >= 150:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . # . #
            # # # # #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    led.plot_bar_graph(input.magnetic_force(Dimension.STRENGTH), 200)
basic.forever(on_forever)
