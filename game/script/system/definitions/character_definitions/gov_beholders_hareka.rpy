define hareka = Character("Hareka", image="hareka", who_prefix="Beholder - ", who_color="#4f6597")
### STILL IMAGES ####
# Beholder Uniform
#image hareka beholder_uniform blush_eyes_closed_happy:
    #"images/characters/gov/beholders/hareka/beholder_uniform/blush_eyes_closed_happy.png"
    #zoom 1.75
#image hareka beholder_uniform blush_eyes_closed_sad:
    #"images/characters/gov/beholders/hareka/beholder_uniform/blush_eyes_closed_sad.png"
    #zoom 1.75
#image hareka beholder_uniform blush_happy:
    #"images/characters/gov/beholders/hareka/beholder_uniform/blush_happy.png"
    #zoom 1.75
#image hareka beholder_uniform blush_sad:
    #"images/characters/gov/beholders/hareka/beholder_uniform/blush_sad.png"
    #zoom 1.75
#image hareka beholder_uniform eyes_closed_happy:
    #"images/characters/gov/beholders/hareka/beholder_uniform/eyes_closed_happy.png"
    #zoom 1.75
#image hareka beholder_uniform eyes_closed_neutral:
    #"images/characters/gov/beholders/hareka/beholder_uniform/eyes_closed_neutral.png"
    #zoom 1.75
#image hareka beholder_uniform eyes_closed_sad:
    #"images/characters/gov/beholders/hareka/beholder_uniform/eyes_closed_sad.png"
    #zoom 1.75
#image hareka beholder_uniform happy:
    #"images/characters/gov/beholders/hareka/beholder_uniform/happy.png"
    #zoom 1.75
#image hareka beholder_uniform neutral:
    #"images/characters/gov/beholders/hareka/beholder_uniform/neutral.png"
    #zoom 1.75
#image hareka beholder_uniform sad:
    #"images/characters/gov/beholders/hareka/beholder_uniform/sad.png"
    #zoom 1.75

### LAYERED IMAGES ###
image blinking_hareka:
    "images/characters/gov/beholders/hareka/layeredimage/assets/opened_eyes_hareka.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/gov/beholders/hareka/layeredimage/assets/closed_eyes_hareka.png"
    .15
    repeat

image sad_blinking_hareka:
    "images/characters/gov/beholders/hareka/layeredimage/assets/sad_opened_eyes_hareka.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/gov/beholders/hareka/layeredimage/assets/sad_closed_eyes_hareka.png"
    .15
    repeat

layeredimage hareka:
    zoom 1.75
    always:
        "images/characters/gov/beholders/hareka/layeredimage/base/hareka_base.png"

    group pants:
        attribute socks default:
            "images/characters/gov/beholders/hareka/layeredimage/base/pants/socks_hareka.png"
                
    group shirts:
        attribute dress default:
            "images/characters/gov/beholders/hareka/layeredimage/base/shirts/dress_hareka.png"
    
    group eyes:
        attribute blinking default:
            "blinking_hareka"
        
        attribute sad_blinking:
            "sad_blinking_hareka"
        
        attribute opened_eyes:
            "images/characters/gov/beholders/hareka/layeredimage/assets/opened_eyes_hareka.png"
        
        attribute closed_eyes:
            "images/characters/gov/beholders/hareka/layeredimage/assets/closed_eyes_hareka.png"
        
        attribute sad_opened_eyes:
            "images/characters/gov/beholders/hareka/layeredimage/assets/sad_opened_eyes_hareka.png"
        
        attribute sad_closed_eyes:
            "images/characters/gov/beholders/hareka/layeredimage/assets/sad_closed_eyes_hareka.png"
    
    group mouth:
        attribute neutral_mouth default:
            "images/characters/gov/beholders/hareka/layeredimage/assets/neutral_hareka.png"
        
        attribute smile_mouth:
            "images/characters/gov/beholders/hareka/layeredimage/assets/smile_closed_hareka.png"
        
        attribute sad_mouth:
            "images/characters/gov/beholders/hareka/layeredimage/assets/sad_closed_hareka.png"
        
        attribute talking:
            "images/characters/gov/beholders/hareka/layeredimage/assets/talking_hareka.png"
    
    group facial_feature:
        attribute blush:
            "images/characters/gov/beholders/hareka/layeredimage/assets/blush_hareka.png"
    
    group inside_hair_decoration:
        attribute hair_band:
            "images/characters/gov/beholders/hareka/layeredimage/assets/hair_band_hareka.png"
    
    
    group hair_decoration:
        attribute ribbon:
            "images/characters/gov/beholders/hareka/layeredimage/assets/ribbon_hareka.png"

image side hareka = "images/characters/gov/beholders/hareka/side.png"
# Paths: images/characters/gov/beholders/hareka/layeredimage/assets/ & images/characters/gov/beholders/hareka/layeredimage/base