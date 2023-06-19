label start:
    "Welcome to {b}Crimson Love - Redux{/b}!"
    "Please keep in mind that this game is in very early beta. There will be bugs, errors, and incomplete story."
    "Thank you for playing, and enjoy!"
    jump volumeselect
menu volumeselect:
    "Select a volume."
    "Volume 1 (Chapters 1-5)":
        jump volume1select
menu volume1select:
    "{b}Currently selected: Volume 1{/b}\n Select a chapter."
    "Chapter 1":
        jump chapter1select
menu chapter1select:
    "{b}Current selected: Volume 1 - Chapter 1{/b}\n Select a day."
    "Day 1 (Monday 1st January)":
        jump vol1ch1d1_start
    "Day 2 (Tuesday 2nd January)":
        jump vol1ch1d2_start