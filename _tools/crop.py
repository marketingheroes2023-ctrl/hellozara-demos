from PIL import Image, ImageDraw
import os
S='/tmp/claude-chrome-screenshots-BSLpzc/screenshot-'
D='/home/claude/hellozara-demos/'
def f(n):
    import glob; return glob.glob(S+'*-%d.*'%n)[0]
def save(n,box,out,w=None,white_dot=None):
    im=Image.open(f(n)).convert('RGB')
    if white_dot:
        d=ImageDraw.Draw(im); d.ellipse(white_dot,fill=(255,255,255))
    if box: im=im.crop(box)
    if w and im.width>w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    os.makedirs(os.path.dirname(D+out),exist_ok=True)
    im.save(D+out,'JPEG',quality=85,progressive=True,optimize=True)
    print(out,im.size)
# Plaasdam
save(0,None,'plaasdam/img/logo.jpg',white_dot=(250,250,312,312))
save(1,(60,0,990,806),'plaasdam/img/windmill.jpg',1200)
save(7,(0,80,1238,929),'plaasdam/img/hall.jpg',1200)
save(11,None,'plaasdam/img/sweetheart.jpg')
save(12,None,'plaasdam/img/table.jpg')
# Wine Barrel
save(22,None,'winebarrel/img/hero.jpg',1400)
save(16,(0,0,410,615),'winebarrel/img/headtable.jpg')
save(20,(0,0,410,690),'winebarrel/img/barrel.jpg')
# Mountridge
save(23,(182,58,487,256),'mountridge/img/t1.jpg')
save(23,(182,262,487,460),'mountridge/img/t2.jpg')
save(23,(763,58,1062,256),'mountridge/img/t3.jpg')
save(23,(763,262,1062,460),'mountridge/img/t4.jpg')
save(27,(0,0,493,490),'mountridge/img/tea.jpg')
save(28,(150,170,493,612),'mountridge/img/chairs.jpg')
save(24,None,'mountridge/img/logo.jpg')
# Nelvida
save(30,None,'nelvida/img/logo.jpg',white_dot=(200,210,262,262))
save(31,None,'nelvida/img/flowers-wide.jpg')
save(34,(0,0,507,605),'nelvida/img/flowers.jpg')
save(38,(66,0,416,760),'nelvida/img/lanterns.jpg')
# OneOtwo
save(40,(230,60,930,697),'oneotwo/img/hall.jpg')
save(43,(60,60,930,697),'oneotwo/img/buffet.jpg')
save(44,(180,58,1275,461),'oneotwo/img/cover.jpg',1400)
save(44,(232,494,388,652),'oneotwo/img/logo.jpg')
