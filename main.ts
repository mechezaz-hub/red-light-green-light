input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    State = GREENLIGHT
    basic.showIcon(IconNames.Yes)
    music.ringTone(185)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    State = REDLIGHT
    basic.showIcon(IconNames.No)
    music.ringTone(622)
})
let GREENLIGHT = 0
let REDLIGHT = 0
let State = 0
State = 0
REDLIGHT = 1
GREENLIGHT = 2
radio.setGroup(1)
basic.forever(function on_forever() {
    radio.sendNumber(State)
})
