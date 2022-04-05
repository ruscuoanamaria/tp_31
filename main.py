for Compteur in range(10):
    if input.button_is_pressed(Button.A):
        basic.show_number(Compteur - 1)
    else:
        if input.button_is_pressed(Button.B):
            basic.show_number(Compteur - 1)