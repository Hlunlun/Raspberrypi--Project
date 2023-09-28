import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_SSD1306

def display_text(text, *args):    

    disp = Adafruit_SSD1306.SSD1306_128_64(rst = 0)

    disp.begin()
    disp.clear()
    disp.display()

    width = disp.width
    height = disp.height

    # 1 bit pixel
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    #ARIALUNI.TTF : font-family file
    font = ImageFont.truetype("./ARIALUNI.TTF", FONT_SIZE)

    try:
        # debug
        print('Display answer on OLED')

        # display answer
        FONT_SIZE = 20
        FILL_BACKGROUND=0
        FILL_TEXT=255
        if text=='CORRECT!':
            FILL_BACKGROUND=255
            FILL_TEXT=0

        draw.rectangle((0, 0, 128,64), outline = 0, fill = FILL_BACKGROUND) 
        draw.text((0, 0), text, font = font, fill = FILL_TEXT)

        disp.image(image)
        disp.display()
        time.sleep(15)

    except KeyboardInterrupt:
        print('terminated')

    finally:
        disp.clear()
        disp.display()
