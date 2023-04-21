import pygame
from Button import *
from TriangleButton import *
from RectangleButton import *
from CircleButton import *
from single_linked_list import *
import time
singlell = SingleLinkedList()


pygame.init()
screen = pygame.display.set_mode((1000,600))

width = screen.get_width()
height = screen.get_height()

color_dark = (100,100,100)
font = pygame.font.SysFont("Helvetica",40)
labelValue = font.render("Value Selection",False,(255,255,255))

lista_botones = []
boton_sll = Button("SingleLL", 30,10,40)
boton_dll = Button("DoubleLL", 220, 10,40)
boton_pyl = Button("Pilas y Colas", 420, 10,40)
boton_arb = Button("Arboles", 670, 10,40)
boton_grf = Button("Grafos", 850, 10,40)
boton_sel = Button("Selección de acciones", 350, 250,40)
lista_botones.extend([boton_sll,boton_dll,boton_pyl,boton_arb,boton_grf,boton_sel])

lista_acciones = []
boton_a1 = Button("Agregar elemento al inicio", 35,10,25)
boton_a2 = Button("Agregar elemento al final", 35, 70,25)
boton_a3 = Button("Eliminar elemento al inicio", 35, 130,25)
boton_a4 = Button("Eliminar elemento al final", 35, 190,25)
boton_a5 = Button("Invertir la lista enlazada", 35, 250,25)
boton_a6 = Button("Eliminar todos los elementos", 35, 310,25)
boton_a7 = Button("Eliminar elemento en la posicion", 35, 370,25)
boton_a8 = Button("Agregar elemento a la posicion", 35, 430,25)
boton_a9 = Button("Editar elemento a la posicion", 35, 490,25)
boton_a10 = Button("Comprobar si esta vacia", 35, 550,25)
lista_acciones.extend([boton_a1,boton_a2,boton_a3,boton_a4,boton_a5,boton_a6,boton_a7,boton_a8,boton_a9,boton_a10]) 

boton_triangle = TriangleButton(490,150)
boton_rectangle = RectangleButton(340, 150)
boton_circle = CircleButton(640, 150)

usertext = ""
text_place1 = font.render(usertext,False,(255,255,255))

node_selected = None
user_number = 0

def actionWindow(screen):
    run = True
    user_numberd = font.render("0",False,(255,255,255))
    user_number = 0
    while (run):
        
        screen.fill((0,0,0))
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen,(0,0,255), pygame.Rect(0, 0, 500, height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN: 
                if event.unicode.isnumeric():
                    user_numberd = font.render(event.unicode,False,(255,255,255)) 
                    user_number = int(event.unicode)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click")
                if boton_a1.checkHover(mouse_pos):
                    singlell.create_node_sll_unshift(node_selected)  
                    print("awa")
                if boton_a2.checkHover(mouse_pos): 
                    singlell.create_node_sll_ends(node_selected)  
                if boton_a3.checkHover(mouse_pos): 
                    singlell.shift_node_sll()
                if boton_a4.checkHover(mouse_pos): 
                    singlell.delete_node_sll_pop()
                if boton_a5.checkHover(mouse_pos): 
                    singlell.reverse_sll()
                if boton_a6.checkHover(mouse_pos): 
                    singlell.remove_all_nodes()
                if boton_a7.checkHover(mouse_pos): 
                    singlell.remove_node(user_number)
                if boton_a8.checkHover(mouse_pos): 
                    singlell.insert_value_at_index( node_selected,user_number)
                if boton_a9.checkHover(mouse_pos): 
                    singlell.update_node_value(user_number,node_selected)
                if boton_a10.checkHover(mouse_pos): 
                   
                    a = font.render(str(singlell.is_sll_empty()),False,(255,255,255))
                    screen.blit(a,(475,250))
                    pygame.display.update()
                    time.sleep(1)
                run = False
                break              
        for button in lista_acciones:
            button.draw(screen, mouse_pos)
        screen.blit(user_numberd,(700,270))
        pygame.display.update()
    return

print(lista_botones)

pygame.display.flip()
run = True
while run:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in lista_botones:
                if button.checkHover(mouse_pos):
                    print("click")
            
            
            if boton_triangle.checkHover(mouse_pos):          
                boton_triangle.setClick()
                boton_circle.setFalse()
                boton_rectangle.setFalse()
                if boton_triangle.selected:
                    node_selected = 0  
                else:
                    node_selected = None
            if boton_rectangle.checkHover(mouse_pos):
                boton_rectangle.setClick()
                boton_circle.setFalse()
                boton_triangle.setFalse()
                if boton_rectangle.selected:
                    node_selected = 1 
                else:
                    node_selected = None
            if boton_circle.checkHover(mouse_pos):
                boton_circle.setClick()
                boton_triangle.setFalse()
                boton_rectangle.setFalse()
                if boton_circle.selected:
                    node_selected = 2
                else:
                    node_selected = None
            if boton_sel.checkHover(mouse_pos):
                if node_selected == None:
                    break
                actionWindow(screen)
                print("HOHEFOHDOEHFOE")
            
            

    for button in lista_botones:
        button.draw(screen, mouse_pos)
    boton_triangle.draw(screen, mouse_pos)
    boton_rectangle.draw(screen, mouse_pos)
    boton_circle.draw(screen,mouse_pos)
    boton_sel.draw(screen, mouse_pos)

    cantidad_nodos =singlell.get_list_lenght()
    contador = 0
    print(singlell.show_list())
    print(singlell.get_list_lenght())
    for nodo in singlell.show_list():
        posicion = (width/2)+ 60*contador - 27*cantidad_nodos
        if nodo == 0:
            pygame.draw.rect(screen,(255,0,0), pygame.Rect(posicion , 400, 50, 50), 3)
            pygame.draw.polygon(screen, (255, 0, 0), ((posicion+5,400+40),(posicion+45,400+40),(posicion+10+((35)/2),400+5)),3)
        if nodo == 1:
            pygame.draw.rect(screen,(0,255,0), pygame.Rect(posicion , 400, 50, 50),3)
            pygame.draw.rect(screen, (0,255, 0),  pygame.Rect(posicion+10 , 400+10, 65-35, 65-35), 3)
        if nodo == 2:
            pygame.draw.rect(screen,(0,0,255), pygame.Rect(posicion , 400, 50, 50),3)
            pygame.draw.circle(screen, (0, 0, 255),(((posicion+(posicion+50))/2),((400+(400+50))/2)), 20, 3)
        contador+=1

    screen.blit(labelValue,(400,100))
    pygame.display.update()
pygame.quit()

