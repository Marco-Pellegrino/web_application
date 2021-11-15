import os
from collections import defaultdict
import random

from airium import Airium


def rec_split(s):
    rest, tail = os.path.split(s)
    if rest in ('', os.path.sep):
        return tail,
    return rec_split(rest) + (tail,)


IMAGE_TYPES = ('jpg','.png','.JPEG','.JPG','.PNG')
GRASSHOPPER_TYPE = ('.gh')
TEXT_TYPES = ('txt','.md')
COLORS = ['#F5F5DC','#A52A2A','#8A2BE2','#0000FF','#008B8B']
ROOT_FOLDER = os.getcwd()

#/Users/mpmac/Documents/GitHub/web_application
print(ROOT_FOLDER) 

os.chdir('assets/Example_Files')
print(os.getcwd())


example_image_collection = defaultdict(list)
example_grasshopper = defaultdict(str)


for root, dirs, files in os.walk(os.getcwd()):

    if files:
        for file_names in files:
            
            file_name = os.path.join(root,file_names)
            file_name = os.path.relpath(file_name, ROOT_FOLDER)

            if file_name.endswith(IMAGE_TYPES):
                example_name = rec_split(file_name)[-3]
                example_image_collection[example_name].append(file_name)
            
            if file_name.endswith(GRASSHOPPER_TYPE):
                example_name = rec_split(file_name)[-2]
                example_grasshopper[example_name] = file_name
            


a = Airium()

a('<!DOCTYPE html>')
with a.html(lang="en"):
    with a.head():
        a.title(_t="Alpaca4d")
        a.meta(charset="utf-8")
        a.meta(name="author",content="Marco Pellegrino")
        a.meta(name="viewport", content= "width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0")
        a.link(rel="icon", href= "assets/icons/logo_200_200.png")

        a.link(rel="stylesheet", href="./style.css")
        a.link(href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400;600&display=swap",rel="stylesheet")


    with a.body():
        with a.h1(id="id23409231", klass='main_header', style="color:Black"):
            a("Alpaca4d")
        with a.div():
            a.img(src="assets/icons/logo_200_200.png")

        with a.p():
            a("Case had never seen him wear the same suit twice, although his wardrobe seemed to consist entirely of meticulous reconstruction’s of garments of the console in faded pinks and yellows. They floated in the coffin for Armitage’s call. Then he’d taken a long and pointless walk along the black induction strip, fine grit sifting from cracks in the Japanese night like live wire voodoo and he’d cry for it, cry in his jacket pocket. Strata of cigarette smoke rose from the tiers, drifting until it struck currents set up by the blowers and the drifting shoals of waste. Sexless and inhumanly patient, his primary gratification seemed to he in his capsule in some coffin hotel, his hands clawed into the nearest door and watched the other passengers as he rode.")
        with a.p():
            a("Therefore the LORD God formed man from the man he made into a woman and brought them to the man he made into a woman and brought her to the woman, Did God say, 'You shall not eat from any tree in the garden'? And to the man said, This at last is bone of my flesh; this one shall be called Woman, for out of the ground of every kind, and everything that creeps on the earth. By the sweat of your face you shall eat all the days of your face you shall eat of it all the earth, and every tree of the waters, and let it separate the waters from the waters. So God made the wild animals of the knowledge of good and evil you shall not eat of it you were taken; you are dust, and to dust you shall eat all the days of your face you shall eat the plants of the sky to separate the light from the darknes.")
    
    with a.main():
        for key,v in example_image_collection.items():
            with a.div(klass='examples', style="background-color: #ffffff"):
                a.h3(style = "color:#000000",_t= key)
                with a.p():
                    for item in v:
                        a.img(src=item, width=300)
                
                a.p(_t="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Offendit eleifend moderatius ex vix, quem odio mazim et qui, purto expetendis cotidieque quo cu, veri persius vituperata ei nec. Ne assum fierent his, cibo eruditi necessitatibus id vix, cum tantas audiam reprehendunt in.")

                a.a(klass="download_link",href=example_grasshopper[key], _t= "DOWNLOAD")
                






html = str(a)  # casting to string extracts the value
# or directly to UTF-8 encoded bytes:
html_bytes = bytes(a)  # casting to bytes is a shortcut to str(a).encode('utf-8')


os.chdir(ROOT_FOLDER)

with open('index.html', 'wb') as f:
    f.write(bytes(html_bytes))