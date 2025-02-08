import random
import pygame
from pygame.sprite import collide_rect

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1540, 800))#, flags=pygame.NOFRAME

pygame.display.set_caption("Fly")
icon = pygame.image.load('image/runr/r1.png').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('image/fon.png').convert_alpha()
bg = pygame.transform.scale(bg, (1540, 800))

bg_sound = pygame.mixer.Sound('sounds/fon.mp3')
bg_sound.play()

#анимация полета
walk_r = [
    pygame.image.load('image/runr/r1.png').convert_alpha(),
    pygame.image.load('image/runr/r2.png').convert_alpha(),
    pygame.image.load('image/runr/r3.png').convert_alpha(),
    pygame.image.load('image/runr/r4.png').convert_alpha(),
    pygame.image.load('image/runr/r5.png').convert_alpha(),
    pygame.image.load('image/runr/r6.png').convert_alpha(),
    pygame.image.load('image/runr/r7.png').convert_alpha(),
    pygame.image.load('image/runr/r8.png').convert_alpha(),
    pygame.image.load('image/runr/r9.png').convert_alpha(),
    pygame.image.load('image/runr/r10.png').convert_alpha(),
    pygame.image.load('image/runr/r11.png').convert_alpha(),
    pygame.image.load('image/runr/r12.png').convert_alpha(),
    pygame.image.load('image/runr/r13.png').convert_alpha(),
    pygame.image.load('image/runr/r14.png').convert_alpha(),


]
walk_l = [
    pygame.image.load('image/runl/l1.png').convert_alpha(),
    pygame.image.load('image/runl/l2.png').convert_alpha(),
    pygame.image.load('image/runl/l3.png').convert_alpha(),
    pygame.image.load('image/runl/l4.png').convert_alpha(),
    pygame.image.load('image/runl/l5.png').convert_alpha(),
    pygame.image.load('image/runl/l6.png').convert_alpha(),
    pygame.image.load('image/runl/l7.png').convert_alpha(),
    pygame.image.load('image/runl/l8.png').convert_alpha(),
    pygame.image.load('image/runl/l9.png').convert_alpha(),
    pygame.image.load('image/runl/l10.png').convert_alpha(),
    pygame.image.load('image/runl/l11.png').convert_alpha(),
    pygame.image.load('image/runl/l12.png').convert_alpha(),
    pygame.image.load('image/runl/l13.png').convert_alpha(),
    pygame.image.load('image/runl/l14.png').convert_alpha(),
]
walk_s = [
    pygame.image.load('image/runs/s1.png').convert_alpha(),
    pygame.image.load('image/runs/s2.png').convert_alpha(),
    pygame.image.load('image/runs/s3.png').convert_alpha(),
    pygame.image.load('image/runs/s2.png').convert_alpha(),
    pygame.image.load('image/runs/s1.png').convert_alpha(),
    pygame.image.load('image/runs/s7.png').convert_alpha(),
    pygame.image.load('image/runs/s8.png').convert_alpha(),
    pygame.image.load('image/runs/s7.png').convert_alpha(),
    pygame.image.load('image/runs/s1.png').convert_alpha(),
]
walk_w = [
    pygame.image.load('image/runw/w1.png').convert_alpha(),
    pygame.image.load('image/runw/w2.png').convert_alpha(),
    pygame.image.load('image/runw/w3.png').convert_alpha(),
    pygame.image.load('image/runw/w2.png').convert_alpha(),
    pygame.image.load('image/runw/w1.png').convert_alpha(),
    pygame.image.load('image/runw/w6.png').convert_alpha(),
    pygame.image.load('image/runw/w7.png').convert_alpha(),
    pygame.image.load('image/runw/w6.png').convert_alpha(),
    pygame.image.load('image/runw/w1.png').convert_alpha(),

]



wrag = pygame.image.load('image/wrag/wrag1.png').convert_alpha()
wrag_x = 1600
wrag_list = []

player_anim_count_rl = 0
player_anim_count_sw = 0
bgx = 0

player_speed = 20
player_x = 200
player_y = 170

wrag_timer = pygame.USEREVENT + 1
pygame.time.set_timer(wrag_timer, 6000)
bull_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bull_timer, 6000)
heel_timer = pygame.USEREVENT + 3
pygame.time.set_timer(heel_timer, 18000)


label = pygame.font.Font('fonts/CormorantSC-Light.ttf', 90)
loose_label = label.render('LOOSE', False, (12, 30, 76))
restart_label = label.render('RESTART', False, (48, 30, 19))
restart_label_rect = restart_label.get_rect(topleft=(900, 400))
exit_label = label.render('EXIT', False, (87, 36, 43))
exit_label_rect = restart_label.get_rect(topleft=(900, 500))

live_num = 3

write = pygame.font.Font('fonts/CormorantSC-Light.ttf', 40)
kills = write.render('Убито:', False, (221, 0, 255))

wrag_count = True
wrag_num = 0
spisok = [wrag_num]


bullet = pygame.image.load('image/items/bullet.png').convert_alpha()
bullet = pygame.transform.scale(bullet, (50, 50))
bullets = []

wrag_bullet = pygame.image.load('image/items/wrbull.png').convert_alpha()
wrag_bullet = pygame.transform.scale(wrag_bullet, (50, 50))
bullet_x = wrag_x
wrag_bullet_spis = []

heel = pygame.image.load('image/items/heel.png').convert_alpha()
heel = pygame.transform.scale(heel, (100, 100))
heel_spis = []

new_lvl = pygame.image.load('image/new_lvl.jpg').convert_alpha()

gameplay = True
running = True
new2_lvl = False
#сделать картинку нью лвл и кнопку контин. после нажатия игра продолжается с новой скоростью спавна врагов



while running:
    keys = pygame.key.get_pressed()
    wrag_y = random.random() * 500
    bullet_y = wrag_y
    screen.blit(bg, (bgx, 0))
    screen.blit(bg, (bgx + 1540, 0))
    heel_x = random.random() * 1300
    heel_y = random.random() * 500
  #  screen.blit(wrag, (-400, 200))

    if gameplay:
        screen.blit(kills, (100, 700))
        player_rect = walk_r[0].get_rect(topleft=(player_x, player_y))


        if wrag_list:
            for (i, el) in enumerate(wrag_list):
                screen.blit(wrag, el)
                el.x -= 10
                if el.x < -10:
                    wrag_list.pop(i)
                if player_rect.colliderect(el):
                    live_num -= 1
                    wrag_list.pop(i)
                    vzruv = pygame.image.load('image/items/vzruv.png').convert_alpha()
                    screen.blit(vzruv, (player_x, player_y))
                    vzr_sound = pygame.mixer.Sound('sounds/vzr.mp3')
                    vzr_sound.play()

                    if live_num == 0:
                        gameplay = False

        if heel_spis:
            for (i, el) in enumerate(heel_spis):
                screen.blit(heel, el)

#стрельба и звук лазера
        if keys[pygame.K_e]:
            bullets.append(bullet.get_rect(topleft=(player_x + 80, player_y + 80)))
            lazer_sound = pygame.mixer.Sound('sounds/lazer.mp3')
            lazer_sound.play()

        if wrag_bullet_spis:
            for (ind, ele) in enumerate(wrag_bullet_spis):
                screen.blit(wrag_bullet, ele)
                wrag_bullet_rect = wrag_bullet.get_rect(topleft=(ele.x, ele.y))
                ele.x -= 30
#счетчик жизней
                if wrag_bullet_rect.colliderect(player_rect):
                    wrag_bullet_spis.pop(ind)
                    live_num -= 1
                    vzruv = pygame.image.load('image/items/vzruv.png').convert_alpha()
                    screen.blit(vzruv, (player_x, player_y))
                    vzr_sound = pygame.mixer.Sound('sounds/vzr.mp3')
                    vzr_sound.play()
                    if live_num == 0:
                        gameplay = False
        if heel_spis:
            for (il, et) in enumerate(heel_spis):
                screen.blit(heel, et)
                heel_rect = heel.get_rect(topleft=(et.x, et.y))
                et.x -= 7
                if player_rect.colliderect(heel_rect):
                    #добавить звук
                    heel_spis.pop(il)
                    live_num += 1
                    isc = pygame.image.load('image/items/iscc.png').convert_alpha()
                    screen.blit(isc, (player_x + 20, player_y - 20))
                    iscc_sound = pygame.mixer.Sound('sounds/iscc.mp3')
                    iscc_sound.play()





#анимации
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            screen.blit(walk_l[player_anim_count_rl], (player_x, player_y))
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            screen.blit(walk_s[player_anim_count_sw], (player_x, player_y))
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            screen.blit(walk_w[player_anim_count_sw], (player_x, player_y))
        else:
            screen.blit(walk_r[player_anim_count_rl], (player_x, player_y))

#передвижение
        if keys[pygame.K_LEFT] and player_x > 30 or keys[pygame.K_a] and player_x > 30:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 1300 or keys[pygame.K_d] and player_x < 1300:
            player_x += player_speed
        elif keys[pygame.K_UP] and player_y > 5 or keys[pygame.K_w] and player_y > 5:
            player_y -= player_speed
        elif keys[pygame.K_DOWN] and player_y < 550 or keys[pygame.K_s] and player_y < 550:
            player_y += player_speed

#смена анимации
        if player_anim_count_rl == 13:
            player_anim_count_rl = 0
        else:
            player_anim_count_rl += 1

        if player_anim_count_sw == 8:
            player_anim_count_sw = 0
        else:
            player_anim_count_sw += 1

        bgx -= 6
        if bgx <= -1540:
            bgx = 0


        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 32

                if el.x > 1550:
                    bullets.pop(i)


#счетчик убийств, звук взрыва, сам взрыв
                if wrag_list:
                    for (index, wrag_el) in enumerate(wrag_list):
                        if el.colliderect(wrag_el):
                            wrag_list.pop(index)
                            bullets.pop(i)
                            wrag_num += 1
                            vzruv = pygame.image.load('image/items/vzruv.png').convert_alpha()
                            screen.blit(vzruv, wrag_el)
                            vzr_sound = pygame.mixer.Sound('sounds/vzr.mp3')
                            vzr_sound.play()
                        elif player_rect.colliderect(wrag_el):
                            vzruv = pygame.image.load('image/items/vzruv.png').convert_alpha()
                            screen.blit(vzruv, wrag_el)
                            vzr_sound = pygame.mixer.Sound('sounds/vzr.mp3')
                            vzr_sound.play()
                            live_num -= 1
                            if live_num == 0:
                                gameplay = False








        wrag_write1 = pygame.font.Font('fonts/CormorantSC-Light.ttf', 90)
        wrag_write1 = write.render(str(wrag_num), False, (221, 0, 255))
        screen.blit(wrag_write1, (230, 700))

        live_label = pygame.font.Font('fonts/CormorantSC-Light.ttf', 15)
        live_label = write.render('Жизней осталось: ' + str(live_num), False, (0, 0, 0))
        screen.blit(live_label, (40, 10))

        wrag_x -= 10
    else:
        screen.fill((0, 0, 0))
        screen.blit(loose_label, (900,300))
        screen.blit(restart_label, restart_label_rect)
        screen.blit(exit_label, exit_label_rect)
        bg_sound.stop()



        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            live_num = 3
            gameplay = True
            player_x = 200
            wrag_list.clear()
            bullets.clear()
            bg_sound.play()

        if exit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            running = False



    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == wrag_timer:
            wrag_list.append(wrag.get_rect(topleft=(1600,wrag_y)))
        if event.type == bull_timer:
            wrag_bullet_spis.append(wrag_bullet.get_rect(topleft=(1800,bullet_y)))
        if event.type == heel_timer:
            heel_spis.append(heel.get_rect(topleft=(heel_x, heel_y)))



    clock.tick(10)

