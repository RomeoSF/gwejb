import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

BACKGROUND = pygame.image.load("craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/background.png")
space_ship = pygame.image.load("craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/Fighter/Idle.png")
space_ship = pygame.transform.rotate(space_ship, 90)
boost_img = pygame.image.load("craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/Fighter/Boost.png")
bullet_img = pygame.image.load("craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/Fighter/Charge_1.png")
bullet_img = pygame.transform.rotate(bullet_img, 90)
attack_img = pygame.image.load("craftpix-net-757069-free-spaceship-pixel-art-sprite-sheets/Fighter/Attack_1.png")
asteroid_img = pygame.image.load("Foozle_2DS0015_Void_EnvironmentPack/Foozle_2DS0015_Void_EnvironmentPack/Asteroids/PNGs/Asteroid 01 - Base.png")
explosion_img = pygame.image.load("Foozle_2DS0015_Void_EnvironmentPack/Foozle_2DS0015_Void_EnvironmentPack/Asteroids/PNGs/Asteroid 01 - Explode.png")

font = pygame.font.SysFont("Arial", 36)

boost_frames = []
boost_frame_width = boost_img.get_width() // 5
boost_frame_height = boost_img.get_height()
for i in range(5):
    frame = pygame.Surface((boost_frame_width, boost_frame_height), pygame.SRCALPHA)
    frame.blit(boost_img, (0, 0), (i * boost_frame_width, 0, boost_frame_width, boost_frame_height))
    frame = pygame.transform.rotate(frame, 90)
    boost_frames.append(frame)

attack_frames = []
frame_width = attack_img.get_width() // 4
frame_height = attack_img.get_height()
for i in range(3):
    frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
    frame.blit(attack_img, (0, 0), (i * frame_width, 0, frame_width, frame_height))
    frame = pygame.transform.rotate(frame, 90)
    attack_frames.append(frame)

explosion_frames = []
explosion_frame_width = explosion_img.get_width() // 6
explosion_frame_height = explosion_img.get_height()
for i in range(6):
    frame = pygame.Surface((explosion_frame_width, explosion_frame_height), pygame.SRCALPHA)
    frame.blit(explosion_img, (0, 0), (i * explosion_frame_width, 0, explosion_frame_width, explosion_frame_height))
    explosion_frames.append(frame)

class Explosion:
    def __init__(self, x, y):
        self.frames = explosion_frames
        self.index = 0
        self.timer = 0
        self.delay = 5
        self.x = x
        self.y = y
        self.finished = False

    def update(self):
        self.timer += 1
        if self.timer >= self.delay:
            self.timer = 0
            self.index += 1
            if self.index >= len(self.frames):
                self.finished = True

    def draw(self, surface):
        if not self.finished:
            surface.blit(self.frames[self.index], (self.x, self.y))

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.image = asteroid_img
        w, h = self.image.get_size()
        self.rect = pygame.Rect(self.x + w * 0.25, self.y + h * 0.25, w * 0.5, h * 0.5)

    def move(self):
        self.y += self.speed
        w, h = self.image.get_size()
        self.rect.topleft = (self.x + w * 0.25, self.y + h * 0.25)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

def draw_health_bar(surface, x, y, health, max_health):
    pygame.draw.rect(surface, (50, 50, 50), (x, y, 200, 20))
    ratio = max(health / max_health, 0)
    pygame.draw.rect(surface, (0, 255, 0), (x, y, 200 * ratio, 20))
    pygame.draw.rect(surface, (255, 255, 255), (x, y, 200, 20), 2)

def draw_boost_bar(surface, x, y, boost, max_boost):
    pygame.draw.rect(surface, (50, 50, 50), (x, y, 200, 10))
    ratio = max(boost / max_boost, 0)
    pygame.draw.rect(surface, (0, 150, 255), (x, y, 200 * ratio, 10))
    pygame.draw.rect(surface, (255, 255, 255), (x, y, 200, 10), 1)

def draw_text(text, size, color, x, y, center=True):
    font_obj = pygame.font.SysFont("Arial", size)
    render = font_obj.render(text, True, color)
    rect = render.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(render, rect)

game_state = "start"
player_x = WIDTH // 2
player_y = HEIGHT - 150
player_speed = 3
player_normal_speed = 3
player_boost_speed = 6
player_health = 100
player_max_health = 100

boost_energy = 100
boost_max_energy = 100
boost_use_rate = 40
boost_regen_rate = 15

is_boosting = False
boost_frame = 0
boost_timer = 0
boost_cooldown = 1000
boost_duration = 1
last_boost_time = 0
boost_start_time = 0

is_attacking = False
attack_timer = 0
attack_frame = 0
attack_cooldown = 500
last_attack_time = 0
attack_speed = 5

bullets = []
bullet_speed = 7

asteroids = []
asteroid_timer = 0
asteroid_spawn_rate = 60

explosions = []
player_dead = False
player_explosion = None
background_y = 0

score = 0
high_score = 0
if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as f:
        try:
            high_score = int(f.read())
        except:
            high_score = 0

game_timer_start = 0
game_duration = 300000

running = True
while running:
    dt = clock.tick(60)
    screen.blit(BACKGROUND, (0, background_y))
    screen.blit(BACKGROUND, (0, background_y - BACKGROUND.get_height()))
    background_y = (background_y + 1) % BACKGROUND.get_height()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_state == "start":
        draw_text("SPACE SHOOTER", 60, (255, 255, 255), WIDTH // 2, HEIGHT // 3)
        draw_text("Press ENTER to Start", 32, (255, 255, 255), WIDTH // 2, HEIGHT // 2)
        if keys[pygame.K_RETURN]:
            game_timer_start = pygame.time.get_ticks()
            game_state = "playing"
    elif game_state == "paused":
        draw_text("PAUSED", 60, (255, 255, 255), WIDTH // 2, HEIGHT // 3)
        draw_text("Press R to Resume", 32, (255, 255, 255), WIDTH // 2, HEIGHT // 2)
        draw_text("Press Q to Quit", 32, (255, 255, 255), WIDTH // 2, HEIGHT // 2 + 40)
        if keys[pygame.K_r]:
            game_state = "playing"
        elif keys[pygame.K_q]:
            running = False
    elif game_state in ["gameover", "win", "lose"]:
        if game_state == "gameover":
            draw_text("GAME OVER", 60, (255, 0, 0), WIDTH // 2, HEIGHT // 2)
        elif game_state == "win":
            draw_text("YOU WIN!", 60, (0, 255, 0), WIDTH // 2, HEIGHT // 2)
        else:
            draw_text("YOU LOSE", 60, (255, 0, 0), WIDTH // 2, HEIGHT // 2)

        draw_text("Press ENTER to Restart", 32, (255, 255, 255), WIDTH // 2, HEIGHT // 2 + 50)
        draw_text(f"Score: {score}", 28, (255, 255, 255), WIDTH // 2, HEIGHT // 2 + 90)
        draw_text(f"High Score: {high_score}", 28, (255, 255, 0), WIDTH // 2, HEIGHT // 2 + 120)
        if keys[pygame.K_RETURN]:
            player_health = player_max_health
            boost_energy = boost_max_energy
            player_dead = False
            explosions.clear()
            asteroids.clear()
            bullets.clear()
            player_x = WIDTH // 2
            player_y = HEIGHT - 150
            if score > high_score:
                high_score = score
                with open("highscore.txt", "w") as f:
                    f.write(str(high_score))
            score = 0
            game_timer_start = pygame.time.get_ticks()
            game_state = "playing"
    elif game_state == "playing":
        if keys[pygame.K_ESCAPE]:
            game_state = "paused"

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - game_timer_start
        time_left = max(0, (game_duration - elapsed_time) // 1000)
        draw_text(f"Time Left: {time_left}s", 24, (255, 255, 255), WIDTH // 2, 20)

        if elapsed_time >= game_duration and not player_dead:
            game_state = "win"

        if keys[pygame.K_LSHIFT] and not is_boosting and boost_energy >= 20:
            is_boosting = True
            boost_start_time = pygame.time.get_ticks()
            last_boost_time = boost_start_time
            player_speed = player_boost_speed

        if is_boosting:
            used = boost_use_rate * dt / 1000
            boost_energy -= used
            if boost_energy <= 0 or pygame.time.get_ticks() - boost_start_time > boost_duration:
                is_boosting = False
                player_speed = player_normal_speed

        if not is_boosting and boost_energy < boost_max_energy:
            boost_energy += boost_regen_rate * dt / 1000
            boost_energy = min(boost_energy, boost_max_energy)

        if keys[pygame.K_a]: player_x -= player_speed
        if keys[pygame.K_d]: player_x += player_speed
        if keys[pygame.K_w]: player_y -= player_speed
        if keys[pygame.K_s]: player_y += player_speed

        player_x = max(0, min(WIDTH - space_ship.get_width(), player_x))
        player_y = max(0, min(HEIGHT - space_ship.get_height(), player_y))

        if keys[pygame.K_SPACE] and not is_attacking and pygame.time.get_ticks() - last_attack_time > attack_cooldown:
            is_attacking = True
            attack_frame = 0
            attack_timer = 0
            last_attack_time = pygame.time.get_ticks()

        if is_attacking:
            attack_timer += 1
            if attack_timer >= attack_speed:
                attack_timer = 0
                attack_frame += 1
                if attack_frame >= len(attack_frames):
                    bullets.append([player_x + space_ship.get_width() // 2 - bullet_img.get_width() // 2, player_y])
                    is_attacking = False

        if player_dead and player_explosion:
            player_explosion.update()
            player_explosion.draw(screen)
            if player_explosion.finished:
                if elapsed_time < game_duration:
                    game_state = "lose"
                else:
                    game_state = "gameover"
        else:
            if is_attacking:
                frame = attack_frames[min(attack_frame, len(attack_frames) - 1)]
                screen.blit(frame, (player_x, player_y))
            elif is_boosting:
                boost_timer += 1
                if boost_timer >= 3:
                    boost_timer = 0
                    boost_frame = (boost_frame + 1) % len(boost_frames)
                screen.blit(boost_frames[boost_frame], (player_x, player_y))
            else:
                screen.blit(space_ship, (player_x, player_y))

        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)
            else:
                bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_img.get_width(), bullet_img.get_height())
                screen.blit(bullet_img, (bullet[0], bullet[1]))
                for asteroid in asteroids[:]:
                    if bullet_rect.colliderect(asteroid.rect):
                        explosions.append(Explosion(asteroid.x, asteroid.y))
                        asteroids.remove(asteroid)
                        bullets.remove(bullet)
                        score += 10
                        break

        asteroid_timer += 1
        if asteroid_timer >= asteroid_spawn_rate:
            asteroids.append(Asteroid(random.randint(0, WIDTH - 60), -50))
            asteroid_timer = 0

        player_rect = pygame.Rect(player_x + 15, player_y + 15, 70, 100)
        for asteroid in asteroids[:]:
            asteroid.move()
            asteroid.draw(screen)
            if asteroid.y > HEIGHT:
                asteroids.remove(asteroid)
            elif not player_dead and asteroid.rect.colliderect(player_rect):
                explosions.append(Explosion(asteroid.x, asteroid.y))
                player_health -= 20
                asteroids.remove(asteroid)
                if player_health <= 0:
                    player_dead = True
                    player_explosion = Explosion(player_x, player_y)

        for explosion in explosions[:]:
            explosion.update()
            explosion.draw(screen)
            if explosion.finished:
                explosions.remove(explosion)

        draw_health_bar(screen, 20, 20, player_health, player_max_health)
        draw_boost_bar(screen, 20, 50, boost_energy, boost_max_energy)
        draw_text(f"Score: {score}", 24, (255, 255, 255), WIDTH - 150, 20, center=False)
        draw_text(f"High Score: {high_score}", 24, (255, 255, 0), WIDTH - 150, 45, center=False)

    pygame.display.update()
