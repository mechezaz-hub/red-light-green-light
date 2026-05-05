def on_button_pressed_a():
    global State
    State = GREENLIGHT
    basic.show_icon(IconNames.YES)
    music.ring_tone(185)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global State
    State = REDLIGHT
    basic.show_icon(IconNames.NO)
    music.ring_tone(622)
input.on_button_pressed(Button.B, on_button_pressed_b)

GREENLIGHT = 0
REDLIGHT = 0
State = 0
State = 0
REDLIGHT = 1
GREENLIGHT = 2
radio.set_group(1)

def on_forever():
    radio.send_number(State)
basic.forever(on_forever)
