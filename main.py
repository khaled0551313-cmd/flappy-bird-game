import pygame
import sys
import math
import random
import pygame_3d_engine  # المكتبة المطلوبة للـ 3D

# تهيئة بايثون والملفات الصوتية البسيطة
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1)

# إعداد الشاشة (أفقي للاندرويد)
WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bird Kind 3D Engine")
clock = pygame.time.Clock()

# توليد صوت القفزة برمجياً
def make_sound():
    sr = 44100
    dur = 0.1
    buf = bytearray()
    for i in range(int(sr * dur)):
        t = i / sr
        val = int(32767 * 0.5 * math.sin(2 * math.pi * (400 + t * 1000) * t))
        buf += val.to_bytes(2, byteorder='little', signed=True)
    return pygame.mixer.Sound(buffer=bytes(buf))

jump_sound = make_sound()

# متغيرات اللعبة
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.6
jump_force = -8
is_game_over = False
score = 0

# عقبات بنظام المنظور ثلاثي الأبعاد المبسط
obstacles = []

def spawn_pipe():
    obs_x = WIDTH
    obs_height = random.randint(120, 260)
    obstacles.append({"x": obs_x, "height": obs_height, "passed": False})

spawn_timer = 0

running = True
while running:
    screen.fill((135, 206, 235)) # خلفية سماوية

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.FINGERDOWN:
            if not is_game_over:
                bird_velocity = jump_force
                try:
                    jump_sound.play()
                except:
                    pass
            else:
                # إعادة تشغيل اللعبة
                is_game_over = False
                bird_y = HEIGHT // 2
                bird_velocity = 0
                obstacles.clear()
                score = 0

    if not is_game_over:
        # حركة العصفور والجاذبية
        bird_velocity += gravity
        bird_y += bird_velocity

        # إنشاء العقبات بانتظام
        spawn_timer += 1
        if spawn_timer > 100:
            spawn_pipe()
            spawn_timer = 0

        # تحريك العقبات للأمام
        for obs in obstacles:
            obs["x"] -= 4

        # إزالة العقبات الخارجة عن الشاشة وزيادة النتيجة
        for obs in obstacles:
            if not obs["passed"] and obs["x"] < 150:
                score += 1
                obs["passed"] = True

        obstacles = [obs for obs in obstacles if obs["x"] > -60]

        # فحص الاصطدام بالأرض أو السقف
        if bird_y > HEIGHT - 40 or bird_y < 0:
            is_game_over = True

        # فحص الاصطدام بالأنابيب
        for obs in obstacles:
            if 150 < obs["x"] < 210:
                if bird_y < obs["height"] or bird_y > obs["height"] + 130:
                    is_game_over = True

    # --- رسم مشهد الـ 2.5D / 3D ---
    pygame.draw.rect(screen, (34, 139, 34), (0, HEIGHT - 40, WIDTH, 40))
    pygame.draw.rect(screen, (0, 100, 0), (0, HEIGHT - 40, WIDTH, 6))

    # رسم الأنابيب بتأثير المنظور البصري
    for obs in obstacles:
        # العمود العلوي
        pygame.draw.rect(screen, (46, 139, 87), (obs["x"], 0, 50, obs["height"]))
        pygame.draw.rect(screen, (0, 80, 0), (obs["x"] - 4, obs["height"] - 15, 58, 15))
        
        # العمود السفلي
        bottom_y = obs["height"] + 130
        pygame.draw.rect(screen, (46, 139, 87), (obs["x"], bottom_y, 50, HEIGHT - bottom_y))
        pygame.draw.rect(screen, (0, 80, 0), (obs["x"] - 4, bottom_y, 58, 15))

    # رسم العصفور (Bird Kind)
    bird_rect = pygame.Rect(150, int(bird_y), 35, 25)
    pygame.draw.ellipse(screen, (255, 215, 0), bird_rect)
    pygame.draw.circle(screen, (255, 255, 255), (175, int(bird_y) + 8), 4)
    pygame.draw.circle(screen, (0, 0, 0), (177, int(bird_y) + 8), 2)
    pygame.draw.polygon(screen, (255, 140, 0), [
        (180, int(bird_y) + 10),
        (192, int(bird_y) + 12),
        (180, int(bird_y) + 15)
    ])

    # واجهة النتيجة
    font = pygame.font.SysFont(None, 40)
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (20, 20))

    if is_game_over:
        game_over_surface = font.render("Game Over! Tap/Key to Restart", True, (200, 0, 0))
        screen.blit(game_over_surface, (WIDTH // 2 - 200, HEIGHT // 2 - 20))

    pygame.display.flip()
    clock.tick(60)
