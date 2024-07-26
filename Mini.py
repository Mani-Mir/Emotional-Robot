from machine import Pin,I2C
import ssd1306
from time import sleep


i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


re1 =88
re2 =0
re3 =40
re4 =32

rh1 =101
rh2 =16
rh3 =5
rh4 =5

################

le1 =0
le2 =0
le3 =40
le4 =32

lh1 =21
lh2 =16
lh3 =5
lh4 =5

##############

m1 =30
m2 =55
m3 =96
m4 =55

def happy():
    x=2
    y=1
    c=1
    
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x+=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)    
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x+=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x+=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x+=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    oled.show()
    
def unhappy():
    x=6
    y=6
    c=0
    
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x-=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)    
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x-=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x-=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x-=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    oled.show()
    
def sad ():
    x=2
    y=-1
    c=1
    
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x+=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)    
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x+=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x+=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x+=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y-=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    oled.show()
    
def unsad():
    x=6
    y=-6
    c=0
    
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x-=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)    
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x-=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x-=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    x-=1
    oled.show()
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    y+=1
    oled.pixel(m1-x,m2-y,c)
    oled.pixel(m3+x,m4-y,c)
    sleep(.2)
    oled.show()
    
def glitch():
    oled.fill(0)
    
    for i in range(40):
        oled.invert(1)
        oled.invert(0)
        oled.show()
        sleep(.05)
        
def logo():
    oled.fill(0)
    
    for i in range(25):
        oled.text('__',30,5)
        oled.scroll(1,1)
        
    for i in range(25):
        oled.text('__',55,30)
        oled.scroll(-1,1)
        
    oled.scroll(25,-25)
    oled.fill_rect(0,37,80,64,0)
    oled.fill_rect(55,37,16,8,1)
    
    for i in range(50):
        oled.line(55-i,38,62,45,0)
    for i in range(50):
        oled.line(70+i,38,63,45,0)
        
    oled.fill_rect(85,15,10,50,1)
    oled.fill_rect(30,45,10,20,1)
    
    oled.show()
    sleep(4)
    oled.fill(0)
    for i in range(18):
        oled.invert(1)
        oled.invert(0)
        oled.show()
        sleep(.0001)
    for x in range(216):
        oled.fill(0)    
        oled.text('Hello',0,64 - x)
        oled.text('I am',0,84 - x)
        oled.text('Mani Mirhosseini',0,104-x)
        oled.text('I write this code',0,124-x)
        oled.text('With Micropython',0,144-x)
        oled.text('On ESP8266 nMCU',0,164-x)
        oled.text('Thanks for your',0,194-x)
        oled.text('Attention <3',18,210-x)
        
        oled.show()
        sleep(.01)
    
    
       
glitch()

while True:
    oled.fill(0)
    
    oled.rect(le1,le2,le3,le4,1)
    oled.rect(re1,re2,re3,re4,1)
    oled.fill_rect(lh1,lh2,lh3,lh4,1)
    oled.fill_rect(rh1,rh2,rh3,rh4,1)
    oled.line(m1,m2,m3,m4,1)
    
    oled.show()
    sleep(2)
    happy()
    sleep(4)
    unhappy()
    sleep(3)
    sad()
    sleep(4)
    unsad()
    sleep(2)
    glitch()
    logo()
    oled.poweroff()
    
    break