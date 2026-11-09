import pygame
import pgzrun
import random
 
vidas = 3 
estado_jogo = "JOGANDO"
WIDTH = 800
HEIGHT = 600
TITLE = "Meu primeiro pygame zero"
luffy = Actor("luffy", (100,100))
moeda = Actor("moeda",(400,300))
inimigo = Actor("luffy",(700,500))
pontos = 0
PONTOS_VITORIA = 100
RAIO_DE_VISAO_QD = 230
VELOCIDADE_inimigo_PERSEGUICAO = 2

def draw():
   global pontos, vidas
   screen.fill((0,0,0))
  
   if estado_jogo == "JOGANDO":
      if estado_inimigo == "PERSEGUICAO":
         cor_visao = (255 ,50,50)
      else:
         cor_visao = (100,100,255)
      screen.draw.circle(inimigo.pos,100,cor_visao)
      if estado_inimigo == "PERSEGUICAO":
         status_alerta = "ALERTA: OPPS,O inimigo TE VIU!"
      else:
         status_alerta = "Status: Oculto"
         
      screen.draw.text(status_alerta, midbottom=(WIDTH// 2,HEIGHT - 15),fontsize=22, color="crinmson"if estado_inimigo == "PERSEGUICAO" else "lime")
   
   elif estado_jogo == "VITORIA":
      screen.draw.text("E ISSO AI! ESCAPOU COM SUCESSO", center=(WIDTH // 2,250), fontsize=50,color="lightgreen",shadow=(2,2),scolor= "black")
      screen.draw.text("presione [R] para jogar novamente",center=(WIDTH // 2,350),fontsize= 26, color= "yellow")
      
      luffy.draw()
      moeda.draw()
      screen.draw.text(f"Pontos: {pontos}/{PONTOS_VITORIA}",topleft=(20,20), fontsize=32, color="gold",shadow=(1,1),scolor="blue")
      inimigo.draw()
      screen.draw.text(f"VIDAS: {vidas}/3",topleft=(20,40), fontsize=32, color="gold",shadow=(1,1),scolor="blue")
   elif estado_jogo == "GAMEOVER":
      screen.draw.text("SE FUDEU", center=(WIDTH // 2,220),fontsize=64,color="crimson",shadow=(2,2),scolor="black")

def update():
   global pontos, vidas, estado_jogo
   atualizar_ia_inimigo()
   if keyboard.right:
       luffy.x = luffy.x + 2
   if keyboard.left:
       luffy.x = luffy.x - 2
   if keyboard.up:
       luffy.y = luffy.y - 2
   if keyboard.down:
       luffy.y = luffy.y + 2
   if luffy.x > inimigo.x:
       inimigo.x = inimigo.x + 1
   if luffy.x < inimigo.x:
       inimigo.x = inimigo.x - 1
   if luffy.y > inimigo.y:
       inimigo.y = inimigo.y + 1
   if luffy.y < inimigo.y:
       inimigo.y = inimigo.y - 1
   if luffy.colliderect(moeda):
      pontos= pontos + 1
      moeda.x = random.randint(50,WIDTH - 50)
      moeda.y = random.randint(50,HEIGHT - 50)
   if luffy.colliderect(inimigo):
      vidas = vidas - 1
   if vidas<= 0:
      estado_jogo = "GAMEOVER"
   else:
      inimigo.x = random.choice([60,WIDTH - 60])
      inimigo.y = random.choice([60,WIDTH - 60])

   if estado_jogo in {"VITORIA", "GAMEOVER"}:
      if keyboard.r:
         reiniciar_jogo()
      return



def atualizar_ia_inimigo():
   global estado_inimigo,indice_rota,estado_jogo
   dx = luffy.x - inimigo.x
   dy = luffy.y - inimigo.y
   distancia_qd = dx**2 + dy**2
   if distancia_qd <= RAIO_DE_VISAO_QD:
      estado_inimigo = "PERSEGUICAO"
   else:
      estado_inimigo = "PATRULHA"
   if estado_inimigo == "PERSEGUICAO":
      if inimigo.x < luffy.x: inimigo.x += VELOCIDADE_inimigo_PERSEGUICAO
      elif inimigo.x > luffy.x: inimigo.x -= VELOCIDADE_inimigo_PERSEGUICAO
    
      if inimigo.y < luffy.y: inimigo.y += VELOCIDADE_inimigo_PERSEGUICAO
      elif inimigo.y > luffy.y: inimigo.y -= VELOCIDADE_inimigo_PERSEGUICAO

   if estado_inimigo == "PATULHA":
      alvo_x, alvo_y = rota_patrulha[indice_rota]
      
      if inimigo.x < alvo_x: inimigo.x += VELOCIDADE_inimigo_PATULHA
      elif inimigo.x > alvo_x: inimigo.x -= VELOCIDADE_inimigo_PATULHA
    
      if inimigo.y < alvo_y: inimigo.y += VELOCIDADE_inimigo_PERSEGUICAO
      elif inimigo.y > alvo_y: inimigo.y -= VELOCIDADE_inimigo_PERSEGUICAO

      if abs(inimigo.x - alvo_x) < 5 and abs(inimigo.y - alvo_y) < 5:
         indice_rota = (indice_rota + 1) % len(rota_patrulha)
   
def reiniciar_jogo():
   global estado_jogo,estado_guarda, indice_rota
   estado_jogo = "JOGANDO"
   estado_guarda = "PATULHA"
   indice_rota = 0
   heroi.pos = (100,500)
   guarda.pos = (400,100)
pgzrun.go() 

