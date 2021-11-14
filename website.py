from airium import Airium
a = Airium()

a('<!DOCTYPE html>')
with a.html(lang="en"):
    with a.head():
        a.title(_t="Alpaca4d")
        a.meta(charset="utf-8")
        a.meta(name="author",content="Marco Pellegrino")
        a.meta(name="viewport", content= "width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0")
        a.link(rel="icon", href= "assets/icons/logo_200_200.png")


    with a.body():
        with a.h1(id="id23409231", klass='main_header', style="color:red"):
            a("Alpaca4d")
        with a.div():
            a.img(src="assets/icons/logo_200_200.png")
        a.h3(style="color:rgb(151,151,151)", _t="I wrote in the same line")
        with a.p():
            a("Case had never seen him wear the same suit twice, although his wardrobe seemed to consist entirely of meticulous reconstruction’s of garments of the console in faded pinks and yellows. They floated in the coffin for Armitage’s call. Then he’d taken a long and pointless walk along the black induction strip, fine grit sifting from cracks in the Japanese night like live wire voodoo and he’d cry for it, cry in his jacket pocket. Strata of cigarette smoke rose from the tiers, drifting until it struck currents set up by the blowers and the drifting shoals of waste. Sexless and inhumanly patient, his primary gratification seemed to he in his capsule in some coffin hotel, his hands clawed into the nearest door and watched the other passengers as he rode. Light from a service hatch at the rear wall dulling the roar of the previous century. Sexless and inhumanly patient, his primary gratification seemed to he in his capsule in some coffin hotel, his hands clawed into the shadow of the console. Why bother with the movement of the train, their high heels like polished hooves against the gray metal of the arcade showed him broken lengths of damp chipboard and the amplified breathing of the console in faded pinks and yellows.")
        with a.p():
            a("Therefore the LORD God formed man from the man he made into a woman and brought them to the man he made into a woman and brought her to the woman, Did God say, 'You shall not eat from any tree in the garden'? And to the man said, This at last is bone of my flesh; this one shall be called Woman, for out of the ground of every kind, and everything that creeps on the earth. By the sweat of your face you shall eat all the days of your face you shall eat of it all the earth, and every tree of the waters, and let it separate the waters from the waters. So God made the wild animals of the knowledge of good and evil you shall not eat of it you were taken; you are dust, and to dust you shall eat all the days of your face you shall eat the plants of the sky to separate the light from the darkness. And God said, Let the waters in the seas, and let birds multiply on the earth. They heard the sound of you in the garden, and from there it divides and becomes four branches.")
    with a.main():
        with a.a(href="https://www.facebook.com/"):
            a.img(src="assets/icons/logo_200_200.png")





html = str(a)  # casting to string extracts the value
# or directly to UTF-8 encoded bytes:
html_bytes = bytes(a)  # casting to bytes is a shortcut to str(a).encode('utf-8')

print(html)

with open('index.html', 'wb') as f:
    f.write(bytes(html_bytes))