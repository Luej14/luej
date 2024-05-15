
    pass
input.on_button_pressed(Button.A, on_button_pressed_button_pressed_a():
    music.play(music.string_playable("- - - - - - - - ", 120),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
music.string_playable("", 120)    pass
music.string_playable("", 120)basic.forever(on_forever)
music.string_playable("", 120)