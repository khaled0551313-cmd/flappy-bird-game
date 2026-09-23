import pygame
import random
import sys
import math
import array

# ==========================================
# 1. تهيئة Pygame (تعمل على OpenGL 1.1)
# ==========================================
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

WIDTH, HEIGHT = 450, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("لعبة باركور العصفور العربي 3D")
clock = pygame.time.Clock()

# الألوان
SKY_BLUE = (135, 206, 235)
GREEN = (50, 205, 50)
RED = (220, 20, 60)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
OBSTACLE_COLOR = (230, 100, 30)
TEXT_COLOR = (20, 20, 20)

# ==========================================
# 2. توليد الأصوات برمجياً (تغريد + واق وق)
# ==========================================
def generate_chirp():
    """توليد صوت تغريد العصفور عند القفز"""
    sample_rate = 22050
    duration = 0.12
    n_samples = int(sample_rate * duration)
    buf = array.array('h')
    for i in range(n_samples):
        t = float(i) / sample_rate
        freq = 800 + 1200 * (t / duration)
        value = int(16000 * math.sin(2 * math.pi * freq * t))
        buf.append(value)
        buf.append(value)
        
    sound = pygame.mixer.Sound(buffer=buf)
    sound.set_volume(0.3)
    return sound

def generate_fail_sound():
    """توليد صوت الخسارة المضحك (واق وق وااااق)"""
    sample_rate = 22050
    duration = 0.6
    n_samples = int(sample_rate * duration)
    buf = array.array('h')
    for i in range(n_samples):
        t = float(i) / sample_rate
        freq = 300 - 180 * (t / duration)
        value = int(20000 * math.sin(2 * math.pi * freq * t) * (1 - t/duration))
        buf.append(value)
        buf.append(value)
        
    sound = pygame.mixer.Sound(buffer=buf)
    sound.set_volume(0.6)
    return sound

chirp_sound = generate_chirp()
fail_sound = generate_fail_sound()

# ==========================================
# 3. متغيرات اللعبة والمستويات (1 إلى 1000)
# ==========================================
state = "MENU" # MENU, GAMEPLAY, GAMEOVER
current_level = 1

bird_x = 100
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.55
jump_strength = -10.5

obstacle_x = WIDTH + 50
obstacle_width = 70
gap_size = 190
obstacle_height = random.randint(100, HEIGHT - 300)

font_large = pygame.font.SysFont("Arial", 36, bold=True)
font_medium = pygame.font.SysFont("Arial", 24, bold=True)

# ==========================================
# 4. دالة رسم العصفور (أخضر / أحمر / أبيض)
# ==========================================
def draw_bird(x, y):
    # الجسم الأخضر
    pygame.draw.circle(screen, GREEN, (int(x), int(y)), 25)
    # البطن الأحمر
    pygame.draw.ellipse(screen, RED, (int(x - 10), int(y - 5), 20, 25))
    # الرقبة البيضاء
    pygame.draw.ellipse(screen, WHITE, (int(x - 15), int(y - 20), 25, 12))
    # المنقار الأصفر
    pygame.draw.polygon(screen, YELLOW, [(int(x + 20), int(y - 5)), (int(x + 35), int(y)), (int(x + 20), int(y + 5))])

def reset_game():
    global bird_y, bird_velocity, obstacle_x, obstacle_height
    bird_y = HEIGHT // 2
    bird_velocity = 0
    obstacle_x = WIDTH + 50
    obstacle_height = random.randint(100, HEIGHT - 300)

# ==========================================
# 5. حلقة اللعبة الرئيسية (Game Loop)
# ==========================================
running = True
while running:
    clock.tick(60) # 60 إطار في الثانية
    screen.fill(SKY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # دعم اللمس على شاشة الجوال أوالماوس/المسافة
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            if state == "MENU":
                state = "GAMEPLAY"
                reset_game()
            elif state == "GAMEPLAY":
                bird_velocity = jump_strength
                chirp_sound.play()
            elif state == "GAMEOVER":
                state = "GAMEPLAY"
                reset_game()

    # --------------------------------------
    # حالة القائمة الرئيسية
    # --------------------------------------
    if state == "MENU":
        draw_bird(WIDTH // 2, HEIGHT // 3)
        title_txt = font_large.render("Parkour Bird 3D", True, TEXT_COLOR)
        level_txt = font_medium.render(f"Level: {current_level} / 1000", True, TEXT_COLOR)
        start_txt = font_medium.render("Tap to Start!", True, RED)

        screen.blit(title_txt, (WIDTH//2 - title_txt.get_width()//2, HEIGHT//2))
        screen.blit(level_txt, (WIDTH//2 - level_txt.get_width()//2, HEIGHT//2 + 50))
        screen.blit(start_txt, (WIDTH//2 - start_txt.get_width()//2, HEIGHT//2 + 120))

    # --------------------------------------
    # حالة اللعب المباشر
    # --------------------------------------
    elif state == "GAMEPLAY":
        # تطبيق الفيزياء
        bird_velocity += gravity
        bird_y += bird_velocity

        # تحريك عقبات الباركور
        speed = 4 + (current_level * 0.02)
        obstacle_x -= speed

        if obstacle_x < -obstacle_width:
            obstacle_x = WIDTH
            obstacle_height = random.randint(100, HEIGHT - 300)
            if current_level < 1000:
                current_level += 1

        # رسم عقبات الباركور
        pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, 0, obstacle_width, obstacle_height))
        pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, obstacle_height + gap_size, obstacle_width, HEIGHT))

        # رسم العصفور
        draw_bird(bird_x, bird_y)

        # رسم رقم المستوى
        lvl_lbl = font_medium.render(f"Level: {current_level} / 1000", True, TEXT_COLOR)
        screen.blit(lvl_lbl, (20, 20))

        # فحص الاصطدام والخسارة
        bird_rect = pygame.Rect(bird_x - 20, bird_y - 20, 40, 40)
        top_obs = pygame.Rect(obstacle_x, 0, obstacle_width, obstacle_height)
        bottom_obs = pygame.Rect(obstacle_x, obstacle_height + gap_size, obstacle_width, HEIGHT)

        if bird_y < 0 or bird_y > HEIGHT or bird_rect.colliderect(top_obs) or bird_rect.colliderect(bottom_obs):
            fail_sound.play()
            state = "GAMEOVER"

    # --------------------------------------
    # حالة الخسارة (Game Over)
    # --------------------------------------
    elif state == "GAMEOVER":
        go_txt = font_large.render("GAME OVER!", True, RED)
        squawk_txt = font_medium.render("Waaq Waq Waaaq!", True, TEXT_COLOR)
        retry_txt = font_medium.render("Tap to Retry", True, GREEN)

        screen.blit(go_txt, (WIDTH//2 - go_txt.get_width()//2, HEIGHT//3))
        screen.blit(squawk_txt, (WIDTH//2 - squawk_txt.get_width()//2, HEIGHT//3 + 60))
        screen.blit(retry_txt, (WIDTH//2 - retry_txt.get_width()//2, HEIGHT//3 + 130))

    pygame.display.flip()

pygame.quit()
sys.exit()