import pygame , asyncio
import random

pygame.init()

# ekran ozgaruvchilari #################################
W , H = 50 , 30
TILE = 20
FPS  = 100
GAME_RES = W * TILE , H * TILE 
clock = pygame.time.Clock()
# ekran yaratish #################################
Border = [pygame.Rect(0,0,1000,600)]
grid = [pygame.Rect(x * TILE , y * TILE , TILE , TILE) for x in range(W) for y in range(H)]
GalavaEkran = pygame.display.set_mode((1300,600))
screen = pygame.Surface((GAME_RES))  
kubike = pygame.Surface((20,20))
limit =pygame.Surface((20,20))
limit.fill('red')
async def main():
    # ozgaruvchilar yaratish #################################
    x , y = 0 , 20
    x1 , y1 = 20 , 0
    mass = [kubike]
    masLen = [[0,0]]
    count = 0
    truar = 0
    asd = True
    konstanta = 0
    masLengaQoshish = []
    l ,k = random.randint(0,1000),random.randint(0,600)

    if l % 20 >0:
            l = l-(l%20) 
    if k % 20 >0:
            k = k-(k%20)

    # oynaga text yaratish #################################   
    scoreCount = 0
    recordCount = 0
    pygame.display.set_caption('Ilon o`yini')
    font = pygame.font.Font('freesansbold.ttf', 32)
    font2 = pygame.font.Font('freesansbold.ttf', 26)
    Title = font.render('ILON  O`YINI', True, pygame.Color('white'))
    font3 = pygame.font.Font('freesansbold.ttf', 100)
    delete = font3.render('GAME  OVER',True,pygame.Color('white'))

            
    def gameSound():
                pygame.mixer.music.load('kubike/gameSound.wav')
                pygame.mixer.music.play(0) 
                
    def Deleted():
        screen.fill('black')
        kubike = 0
        limit = 0
        GalavaEkran.blit(delete , (170,220))
        
    while True:
            # asosiy oyin boshlanishi #################################
                recordStr = str(recordCount)
                scoreStr = str(scoreCount)
                Record = font2.render('RECORD :   '+recordStr,True,pygame.Color('white'))
                Score = font2.render('SCORE :   '+scoreStr,True,pygame.Color('white'))
                
                # oynalar yaratish #################################
                GalavaEkran.fill('#585858')
                GalavaEkran.blit(Title,(1050,20))
                GalavaEkran.blit(Record,(1030,500))
                GalavaEkran.blit(Score,(1030,550))
                GalavaEkran.blit(screen , (0,0))
                            
                screen.fill('black')

                kubike.fill('white')
                    
                # ilon devolga tegsa chiqib ketish #################################
                            
                # ilon yaratish #################################
                x += x1
                y += y1
                screen.blit(limit,(x,y))
                let = x,y
                    
                # ilon oziga tegsa chiqib ketish #################################
                for i in range(len(masLen)):
                    if let == masLen[i]:
                        exit()
                    
                # har 15 qadamda gosh chiqazish kordinatalari #################################
                if asd == False:
                    konstanta += 1
                if konstanta == 15:
                    konstanta = 0
                    l ,k = random.randint(0,1000),random.randint(0,600)
                    if l % 20 >0:
                        l = l-(l%20) 
                    if k % 20 >0:
                        k = k-(k%20) 
                    asd = True
                        
                # gosh ilonga urilganda massivga qoshish #################################   
                qwe = l,k
                if qwe == let : 
                    scoreCount += 100
                    asd = False
                    mass.append(kubike)
                    qwe = masLengaQoshish
                    masLen.append(qwe)
                    qwe = 0,0  
                            
                # gosh chiqazish #################################      
                if asd == True:
                    screen.blit(kubike , (qwe)) 
                        
                # ilon massiviga goshni kardinatalarini qoshish funksiyasi #################################    
                def chiz(x,y):
                    screen.blit(mass[truar],(x,y))
                        
                # ilon ketidan massivni yurgazish #################################    
                if count > 1:
                    for i in range(len(mass)):
                        masLengaQoshish = masLen[i]
                        chiz(masLen[i][0],masLen[i][1])           
                    truar += 1     
                if truar >= len(mass):
                    truar = 0               
                masLen[truar]=x,y    
                count += 1
                
                # pygamedan chiqish va ilon orqaga yurmasligini bajarish #################################            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            exit()   
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if x1 != 20:
                                x1 = -20 
                                y1 = 0
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if x1 != -20:
                                x1 = 20
                                y1 = 0
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            if y1 != 20:
                                y1 = -20  
                                x1 = 0
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            if y1 != -20:
                                y1 = 20 
                                x1 = 0 
                                
                # oynani ishlatish #################################                 
                [pygame.draw.rect(screen,(40,40,40),i_rect,1) for i_rect in grid]  
                [pygame.draw.rect(screen,(pygame.Color('red')),border,2) for border in Border]   
                if x < 0 or x > 1000:
                    Deleted()
                if y < 0 or y > 600:
                    Deleted()              
                pygame.display.update()
                clock.tick(FPS)
                pygame.time.delay(200)
                
                await asyncio.sleep(0)
asyncio.run(main())
            
