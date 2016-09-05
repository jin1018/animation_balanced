#from math import pi
import pygame
pygame.init()#initialzie pygame engine

#colors in RGB(red,green,blue) #red=(255,0,0), green=(0,255,0), blue=(0,0,255), black=(0,0,0), white=(0,0,0)
WHITE=(255,255,255)
bl_color = (20,43,190)#color for the characters "b", "l"
nced_color = (250,43,130)#color for the characters "n", "c", "e", "d"
 
#configure screen(window pops up)
ScreenSize = [500, 500]
screen = pygame.display.set_mode(ScreenSize)
 
pygame.display.set_caption("balance animation")
 
#Loop until the user clicks the close button.
close = False
clock = pygame.time.Clock()

#rotate line
x1=50
y1=180
x2=450
y2=270

a_x = 80
a_y = 240

b_x = 55
b_y = 130

l_x = 150
l_y = 138

n_x = 260
n_y = 170

c_x = 300
c_y = 184

e_x = 340
e_y = 190

d_x = 390
d_y = 208

switchDirection=1
switchFlag=0
purple_r, purple_g, purple_b = 100,43,190
while not close:
	#limit the while loop to run 10 times per second (Otherwise, it uses up too much space)
    #can also be used to control speed of motion
    clock.tick(10)

    # end program if the window(screen) is closed
    for event in pygame.event.get(): #an event happened
        if event.type == pygame.QUIT:
            close=True

    screen.fill(WHITE)#clear the screen each time

    #display text: "A"
    font_A = pygame.font.SysFont("helvetica", 80)
    text_A = font_A.render("A", True, (purple_r, purple_g, purple_b))

    font_B = pygame.font.SysFont("helvetica", 60)
    text_B = font_B.render("B", True, bl_color)

    font_L = pygame.font.SysFont("helvetica", 60)
    text_L = font_B.render("L", True, bl_color)

    font_N = pygame.font.SysFont("helvetica", 60)
    text_N = font_B.render("N", True, nced_color)

    font_C = pygame.font.SysFont("helvetica", 60)
    text_C = font_B.render("C", True, nced_color)

    font_E = pygame.font.SysFont("helvetica", 60)
    text_E = font_B.render("E", True, nced_color)

    font_D = pygame.font.SysFont("helvetica", 60)
    text_D = font_B.render("D", True, nced_color)
    
    screen.blit( text_A, (a_x,a_y) )

    screen.blit( text_B, (b_x,b_y) )
    screen.blit( text_L, (l_x,l_y) )
    screen.blit( text_N, (n_x,n_y) )
    screen.blit( text_C, (c_x,c_y) )
    screen.blit( text_E, (e_x,e_y) )
    screen.blit( text_D, (d_x,d_y) )
 
    #line function:
    #line(Surface, color, start_pos, end_pos, width=1)
    pygame.draw.line(screen, (purple_r, purple_g, purple_b), [x1, y1], [x2,y2], 10)
    if switchFlag==0:
		x1=x1+1
		y1=y1-1
		x2=x2-1
		y2=y2+1

		a_x = a_x + 8

		b_x = b_x+1.5
		b_y = b_y-1.5
		l_x = l_x+0.8
		l_y = l_y+0.8
		n_x = n_x+1.3
		n_y = n_y+1.3
		c_x = c_x+1.7
		c_y = c_y+1.7
		e_x = e_x+1.9
		e_y = e_y+1.9
		d_x = d_x+1.9
		d_y = d_y+1.9
		purple_r = purple_r + 8
		purple_b = purple_b - 3


    else:
    	x1=x1-1
    	y1=y1+1
    	x2=x2+1
    	y2=y2-1
    	
    	a_x = a_x - 8

    	b_x = b_x-1.5
    	b_y = b_y+1.5
    	l_x = l_x-0.8
    	l_y = l_y-0.8
    	n_x = n_x-1.3
    	n_y = n_y-1.3
    	c_x = c_x-1.7
    	c_y = c_y-1.7
    	e_x = e_x-1.9
    	e_y = e_y-1.9
    	d_x = d_x-1.9
    	d_y = d_y-1.9
    	purple_r = purple_r - 8
    	purple_b = purple_b + 3

    switchDirection=switchDirection+1

    if switchDirection%40<20:
    	switchFlag=0
    else:
    	switchFlag=1
 
    pygame.display.flip()#display updated screen after drawing functions

pygame.quit()