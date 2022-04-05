/*Ex 1 de la MakeCode;

basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")
basic.pause(5000)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")


//Ex2 

basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
if input.button_is_pressed(Button.A):
    basic.show_leds("""
        # . . . .
                . # . . .
                . . # . .
                . . . # .
                . . . . #
    """)
else:
    if input.button_is_pressed(Button.B):
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)


        Ex 3.
        for Compteur in range(10):
    if input.button_is_pressed(Button.A):
        basic.show_number(Compteur - 1)
    else:
        if input.button_is_pressed(Button.B):
            basic.show_number(Compteur + 1)