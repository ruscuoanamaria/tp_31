for (let Compteur = 0; Compteur < 10; Compteur++) {
    if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(Compteur - 1)
    } else if (input.buttonIsPressed(Button.B)) {
        basic.showNumber(Compteur - 1)
    }
    
}
