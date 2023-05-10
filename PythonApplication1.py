import pygame   #Libreria necessarria per lo sviluppo di videogiochi su python
import time
import random

pygame.font.init() #Funzione del modulo pygame che si occuppa di inizializzare il sottosistema di rendering
pygame.init() #Funzione del modulo pygame che si occupa di inizializzare vari sottosistemi(grafica,input,audio)
infoObject = pygame.display.Info()

WIDTH =  infoObject.current_w  #Prelevo le informazioni relative alla larghezza e altezza del monitor dell'utente
HEIGHT =  infoObject.current_h- 100  #E' necessario ridurre l'altezza della finestra per mostrare a schermo anche le scorciatoie di finestra(chiusura,ridimensionamento,minimizzazione)
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Asseggno alla variabile WIN la finestra di gioco con i parametri di altezza e larghezza del monitor 
pygame.display.set_caption("Mission Environment")

elapsed_time=0 #Inizializzo la variabile tempo trascorso
punteggio_tot=0 #Inizializzo il punteggio inziale

SKY_BLUE = (135, 206, 235) #Assegno a diverse variabili i preset(RGB) per avere determinati colori
WHITE = (255, 255, 255)    
GREEN = (0, 255, 0)    
RED = (255, 0, 0)    
BLACK= (0,0,0) 
FONT = pygame.font.SysFont("comicsans", 30)  #Assegno il font alla variabile FONT


PLAYER_WIDTH = 160   #Variabili dimensioni del player e dei lampi
PLAYER_HEIGHT = 180
PLAYER_VEL = 7
STAR_WIDTH = 100
STAR_HEIGHT = 90
STAR_VEL = 3


sfondo_no_omino = pygame.transform.scale(pygame.image.load("no_omino.jpg"), (WIDTH+100, HEIGHT+100))    #Variabili contenenti gli elementi grafici
sfbianco = pygame.transform.scale(pygame.image.load("sfondo_bianco.jpeg"), (WIDTH, HEIGHT))
fulmine = pygame.transform.scale(pygame.image.load("fulmine.jpeg"), (STAR_WIDTH+100, STAR_HEIGHT+100))
pannello = pygame.transform.scale(pygame.image.load("pannello.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
start = pygame.transform.scale(pygame.image.load("schermata_iniziale.jpg"), (WIDTH, HEIGHT))
sfondo_omino= pygame.transform.scale(pygame.image.load("con_omino.jpg"), (WIDTH, HEIGHT))
game_over= pygame.transform.scale(pygame.image.load("gameover.png"), (WIDTH, HEIGHT))
schermata_finale= pygame.transform.scale(pygame.image.load("fine_gioco.png"), (WIDTH, HEIGHT))



def draw(player, elapsed_time, stars ,point,stop, gamestarter):   #Funzione esterna che si occupa di stampare a schermo il primo gioco
    if gamestarter == True :  #Se il giocatore preme spacebar il gioco parte e vengono mostrati a schermo il pannello mobile e i fulmini cadenti
        WIN.blit(sfondo_no_omino, (0, 0)) #Stampo il background
        WIN.blit(pannello,(player.x,player.y)) #Stampo il pannello mosso dal giocatore
        time_text = FONT.render(f"Tempo: {round(elapsed_time)}s", 1, "white") 
        WIN.blit(time_text, (10, 10)) #Stampo il tempo passato a schermo
        point_text = FONT.render(f"Punti: {round(point)}", 1, "white")
        WIN.blit(point_text, (WIDTH-150,10)) #Stampo il punteggio a schermo
        for star in stars:   #Stampo i fulmini nella lista
            WIN.blit(fulmine,(star.x,star.y))

    
        
            
    if elapsed_time > stop : #Se il tempo di gioco finisce si passa ad un'altra schermata
        WIN.blit(sfondo_omino, (0, 0)) 
        finish_text = FONT.render(f"Ottimo lavoro hai fatto  {round(point)} punti !", 1, "white")#
        WIN.blit(finish_text, (20 , HEIGHT/2+150)) #Stampo lo sfondo e il punteggio
        
        
    if gamestarter == False : #Schermata iniziale
        WIN.blit(start, (0,0)) 
        
       
    pygame.display.flip() #Aggiorno lo schermo
     

def draw2(questions, current_question,gover,false_button,true_button,score,fine_gioco,punteggio_tot):
    WIN.fill(SKY_BLUE)
    

    
    if gover == False and current_question<11:
        pygame.draw.rect(WIN, RED, false_button)
        pygame.draw.rect(WIN, GREEN, true_button)
        true_text = FONT.render("Vero", True, BLACK)
        true_rect = true_text.get_rect(center=true_button.center)
        WIN.blit(true_text, true_rect)
        false_text = FONT.render("Falso", True, BLACK)
        false_rect = false_text.get_rect(center=false_button.center)
        WIN.blit(false_text, false_rect)
        pygame.draw.rect(WIN, SKY_BLUE, (0, 0, WIDTH, 150))  # Copre la domanda precedente con il colore dello sfondo
        question_text = FONT.render(questions[current_question], True, BLACK)
        question_rect = question_text.get_rect(center=(WIDTH//2, 100))    
        WIN.blit(question_text, question_rect)
        score_text = FONT.render(f"Punteggio {round(score)}  ", 1, "black")
        WIN.blit(score_text,(0,0))

    if gover == True :
        
        WIN.blit(game_over,(0,0))
        
        
    if fine_gioco:
        punteggio_tot=punteggio_tot+score
        punteggio = FONT.render(f"Punteggio totale : {round(punteggio_tot)}  ", 1, "black")
        WIN.blit(schermata_finale,(0,0))
        WIN.blit(punteggio,(WIDTH/2-75,HEIGHT/2))
    
    pygame.display.update()
   
    
def gioco_1(puntegggio_tot): #Funzione che si occupa del primo minigioco
   
    elapsed_time=0
    gamestarter = False
    run = True
    vab = True
    stop = 40
    star_count=0
    point = 0
    start_time=0
    stars = []
    clock = new_func1() 
    player = new_func()
    star_add_increment= 2000
    start_time=0
    a=True
    
    
    

    while run:
        
        
        keys = new_func2()
        
        #Chiusura Gioco#
        for event in pygame.event.get():    
           if event.type == pygame.QUIT :
              run = False
              
              pygame.quit()
              
              
           
           
        
        
        #Controllo del tempo
        if gamestarter == True and a==True :   
            start_time=time.time() 
            a=False
        elapsed_time = time.time() - start_time
        

        if (elapsed_time>stop+15 and gamestarter == True) or keys[pygame.K_ESCAPE]:
            pygame.time.delay(10)
            run= False
            return   


        #Stampa Stelle
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        if star_count > star_add_increment:
                for _ in range(3):
                    star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)                   
                

                star_add_increment = max(1200, star_add_increment - 50)
                star_count = 0
        
                
                
        #Tasto d'inizio         
            
        if keys[pygame.K_SPACE] and vab == True :             
           gamestarter = True
           vab = False  
        
        
        
        
        

        #Gioco numero 1
        if  gamestarter == True and elapsed_time < stop:    
            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > HEIGHT-50:
                    stars.remove(star)
                elif  star.colliderect(player) : 
                    stars.remove(star)
                    point=point+1
                    punteggio_tot=point
            keys = new_func2()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL
        
















        
        draw(player, elapsed_time, stars, point,stop, gamestarter)
    

def gioco_2(WIDTH,HEIGTH,punteggio_tot) : 

    






    fine_gioco= False
    running = True
    gover = False
    score = 0
    current_question = 0
    questions = ["Esistono pannelli fotovoltaici che funzionano anche di notte?", "Pannello fotovoltaico e solare sono la stessa cosa.", "Un pannello fotovoltaico dura in media 25 anni.","Il sole emette 5,2 x 10^24 Kilocalorie/Minuto?","L energia solare ci giunge sotto forma di onde acustiche","L energia solare ci giunge sotto forma di onde corte","Radiazione globale e sinonimo di radiazione effettiva","L albedo e il rapporto tra l energia riflessa e l energia totale in arrivo","L effetto serra non ce sempre stato","La cella di Hudley e in espansione?","L equatore termico corrisponde all equatore geografico"]
    correct_answers = [True, False, True,True,False,True,False,True,False,True,False]
    false_button = pygame.Rect(WIDTH*(2/3), 200, 100, 50)
    true_button = pygame.Rect(WIDTH*(1/3), 200, 100, 50)
    
    
    
    
    
    

    
    


    while running:
        if not fine_gioco:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if true_button.collidepoint(event.pos):
                        if correct_answers[current_question]:
                            score+=1
                            current_question+=1
                        else:
                            score-=1
                            current_question+=1
                    if false_button.collidepoint(event.pos):
                        if not correct_answers[current_question]:
                            score+=1
                            current_question+=1
                        else:
                            score-=1
                            current_question+=1
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False       
        if score<-3 :
            gover = True
        if current_question>10:
           fine_gioco = True 
            
        draw2(questions,current_question,gover,false_button,true_button,score,fine_gioco,punteggio_tot)
        
        
        
            
            
    pygame.quit() 





    



    
        
        
   

        
  
    













def new_func5(star_x):
    star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
    return star

def new_func4():
    star_x = random.randint(0, WIDTH - STAR_WIDTH)
    return star_x

def new_func2():
    keys = pygame.key.get_pressed()
    return keys

def new_func1():
    clock = pygame.time.Clock()
    return clock

def new_func():
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH, PLAYER_HEIGHT)
    return player

def main(WIDTH,HEIGHT,punteggio_tot):
    
    gioco_1(punteggio_tot)
    gioco_2(WIDTH,HEIGHT,punteggio_tot)

if __name__ == "__main__":
    main(WIDTH,HEIGHT,punteggio_tot)   



    
    

    
   
   
       


































 






    

