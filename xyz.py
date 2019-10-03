from sense_hat import SenseHat
import time 
s = SenseHat() 
s.clear()
X = (255, 255, 0)
O = (0,0,0)
grid0 = [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O]
i = 0 
pos0 = 0 
while i<7:
 del grid0[pos0]
 grid0.insert(pos0,X)
 pos0 = pos0 + 8
 i=i+1
 s.set_pixels(grid0)
 time.sleep(.25)
q = 0
while q<7:
 del grid0[pos0]
 grid0.insert(pos0,X)
 pos0 =  pos0 + 1
 q=q+1
 s.set_pixels(grid0)
 time.sleep(.25)
r = 0
while r<7:
 del grid0[pos0]
 grid0.insert(pos0,X)
 pos0 = pos0 -8
 r=r+1
 s.set_pixels(grid0)
 time.sleep(.25)
t = 0
while t<7:
 del grid0[pos0]
 grid0.insert(pos0,X)
 pos0 = pos0 - 1
 t=t+1
 s.set_pixels(grid0)
 time.sleep(.25)
