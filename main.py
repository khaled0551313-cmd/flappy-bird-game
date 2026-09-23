import pygame
import random
import sys
import math
import numpy as np

# 1. تهيئة اللعبة ونظام الصوت
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1)

# أبعاد الشاشة لجهاز الجوال (وضع أفقي)
WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bird Kind 2.5D Adventure")
clock = pygame.time.Clock()

# 2. دالة توليد الأصوات برمجياً مع حماية الـ Audio Buffer للأندرويد
def generate_sound(sound_type):
    sample_rate = 44100
    if sound_type == "jump":
        # صوت قفز ينزلق للأعلى (Pitch Slide Up)
        duration = 0.12
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        freq = np.linspace(350, 700, len(t))
        wave = np.sin(2 * np.pi * freq * t)
    elif sound_type == "score":
        # صوت نقطة ناعم بـ Sine Wave
        duration = 0.15
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        freq = np.where(t < duration/2, 880, 1174.66)
        wave = np.sin(2 * np.pi * freq * t)
    elif sound_type == "hit":
        # صوت اصطدام برمجياً بواسطة White Noise وتلاشي سريع
        duration = 0.25
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        noise = np.random.uniform(-1, 1, len(t))
        envelope = np.exp(-8 * t)
        wave = noise * envelope
    else:
        return None

    # تحويل الموجة إلى صيغة 16-bit PCM وتطبيق الفوليوم
    audio = (wave * 32767 * 0.4).astype(np.int16)
    return pygame.sarray.make_sound(audio)

# إنشاء المؤثرات الصوتية في الذاكرة
snd_jump = generate_sound("jump")
snd_score = generate_sound("score")
snd_hit = generate_sound("hit")

# 3. الألوان الأساسية للبيئة
SKY_TOP = (120, 190, 235)
SKY_BOTTOM = (210, 240, 255)
MOUNTAIN_COLOR = (140, 175, 200)
FOREST_COLOR = (45, 95, 60)
GROUND_GREEN = (110, 185, 75)
PATH_BROWN = (185, 145, 95)

# 4. متغيرات اللعبة والفيزياء
bird_x = 180
bird_y = HEIGHT // 2 - 30
bird_velocity = 0
gravity = 0.55
jump_strength = -9.0

# طبقات التمرير خلف اللعبة (Parallax Background)
bg_mountains_x = 0
bg_trees_x = 0

# قائمة العوائق ثلاثية الأبعاد (تأتي من العمق z=0 نحو الشاشة z=1)
obstacles = []
spawn_timer = 0
score = 0
game_over = False

def spawn_obstacle():
    obs_type = random.choice(["log", "rock"])
    # تحديد مسار عشوائي يخرج منه العائق في عمق الغابة
    start_x = random.randint(WIDTH // 2 - 50, WIDTH // 2 + 150)
    obstacles.append({
        "z": 0.0,          # Depth: 0.0 (بعيد جداً) -> 1.0 (عند اللاعب)
        "x": start_x, 
        "type": obs_type
    })

# 5. الحلقة البرمجية الرئيسية
running = True
while running:
    clock.tick(60)

    # التفاعل مع اللمس والجوال
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
            if game_over:
                # إعادة التشغيل عند الخسارة
                bird_y = HEIGHT // 2 - 30
                bird_velocity = 0
                obstacles.clear()
                score = 0
                game_over = False
            else:
                bird_velocity = jump_strength
                if snd_jump: snd_jump.play()

    if not game_over:
        # حركة الجاذبية للطائر
        bird_velocity += gravity
        bird_y += bird_velocity

        # حدود الشاشة للطائر
        if bird_y < 25:
            bird_y = 25
            bird_velocity = 0
        if bird_y > HEIGHT - 70:
            if snd_hit: snd_hit.play()
            game_over = True

        # تحريك الخلفيات بأبعاد مختلفة (Parallax Depth)
        bg_mountains_x = (bg_mountains_x - 0.4) % WIDTH
        bg_trees_x = (bg_trees_x - 1.2) % WIDTH

        # إنشاء العوائق المتقاربة بالعمق
        spawn_timer += 1
        if spawn_timer > 85:
            spawn_obstacle()
            spawn_timer = 0

        # تحديث مواضع العوائق والعمق البصري
        for obs in obstacles[:]:
            obs["z"] += 0.012  # زيادة نسبة القرب نحو الشاشة

            # حساب الموقع المائل البصري والحجم المتزايد (Scaling)
            scale = obs["z"]
            current_x = obs["x"] - (scale * (obs["x"] - 50))
            current_y = (HEIGHT // 2 + 30) + (scale * 170)

            # اجتياز العائق بنجاح
            if obs["z"] >= 1.0:
                obstacles.remove(obs)
                score += 1
                if snd_score: snd_score.play()
                continue

            # حساب التصادم ثلاثي الأبعاد مع الطائر عند وصول العائق للموقع الصحيح (z > 0.8)
            if 0.78 < obs["z"] < 0.96:
                if abs(current_x - bird_x) < 55 and abs(current_y - bird_y) < 65:
                    if snd_hit: snd_hit.play()
                    game_over = True

    # 6. رسم عناصر اللعبة بالمنظور البصري (من الخلف إلى الأمام)
    # رسم تدرج السماء
    for y in range(HEIGHT // 2 + 50):
        ratio = y / (HEIGHT // 2 + 50)
        r = int(SKY_TOP[0] * (1 - ratio) + SKY_BOTTOM[0] * ratio)
        g = int(SKY_TOP[1] * (1 - ratio) + SKY_BOTTOM[1] * ratio)
        b = int(SKY_TOP[2] * (1 - ratio) + SKY_BOTTOM[2] * ratio)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

    # الجبال البعيدة (Parallax 1)
    for i in range(2):
        pygame.draw.polygon(screen, MOUNTAIN_COLOR, [
            (bg_mountains_x + i*WIDTH - 60, HEIGHT // 2 + 50),
            (bg_mountains_x + i*WIDTH + 140, HEIGHT // 2 - 80),
            (bg_mountains_x + i*WIDTH + 380, HEIGHT // 2 + 50)
        ])

    # الغابة في المنتصف (Parallax 2)
    for i in range(4):
        x_pos = bg_trees_x + i*(WIDTH//3)
        pygame.draw.rect(screen, FOREST_COLOR, (x_pos, HEIGHT // 2 - 10, 80, 80))
        pygame.draw.circle(screen, FOREST_COLOR, (x_pos + 40, HEIGHT // 2 - 20), 55)

    # رسم الأرضية والممر المائل المنظوري (Isometric Path 2.5D)
    pygame.draw.polygon(screen, GROUND_GREEN, [
        (0, HEIGHT), (WIDTH, HEIGHT), 
        (WIDTH, HEIGHT // 2 + 40), (0, HEIGHT // 2 + 70)
    ])
    pygame.draw.polygon(screen, PATH_BROWN, [
        (120, HEIGHT), (420, HEIGHT), 
        (WIDTH // 2 + 60, HEIGHT // 2 + 45), (WIDTH // 2 - 10, HEIGHT // 2 + 48)
    ])

    # رسم العوائق في الممر المائل القادمة من العمق
    for obs in obstacles:
        z = obs["z"]
        w = int(18 + z * 105)
        h = int(12 + z * 85)
        curr_x = int(obs["x"] - (z * (obs["x"] - 50)))
        curr_y = int((HEIGHT // 2 + 45) + (z * 170))

        if obs["type"] == "log":
            # جذع شجرة ثنائي الطبقات ليعطي مظهراً مجسماً
            pygame.draw.rect(screen, (120, 60, 20), (curr_x, curr_y - h, w, h), border_radius=4)
            pygame.draw.rect(screen, (80, 40, 10), (curr_x, curr_y - h, w, int(h * 0.3)))
        else:
            # صخرة ثلاثية الأبعاد بظلال متدرجة
            pygame.draw.ellipse(screen, (100, 100, 100), (curr_x, curr_y - h, w, h))
            pygame.draw.ellipse(screen, (150, 150, 150), (curr_x + 4, curr_y - h + 2, w - 8, h - 5))

    # رسم ظل الطائر التفاعلي على الأرض (يتصاغر ويتلاشى مع الارتفاع)
    ground_plane_y = HEIGHT - 85
    height_diff = max(0, ground_plane_y - bird_y)
    shadow_size = max(6, int(38 - height_diff * 0.12))
    shadow_surface = pygame.Surface((shadow_size * 2, shadow_size), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow_surface, (20, 50, 20, 90), (0, 0, shadow_size * 2, shadow_size))
    screen.blit(shadow_surface, (bird_x - shadow_size, ground_plane_y))

    # رسم الطائر اللطيف
    # الجسم
    pygame.draw.circle(screen, (255, 185, 15), (bird_x, int(bird_y)), 22)
    # العين والضوء
    pygame.draw.circle(screen, (0, 0, 0), (bird_x + 10, int(bird_y) - 5), 4)
    pygame.draw.circle(screen, (255, 255, 255), (bird_x + 12, int(bird_y) - 7), 2)
    # المنقار
    pygame.draw.polygon(screen, (255, 80, 0), [(bird_x + 18, int(bird_y) - 4), (bird_x + 28, int(bird_y)), (bird_x + 18, int(bird_y) + 4)])
    # الجناح المتفاعل مع السرعة
    wing_y = int(bird_y + math.sin(pygame.time.get_ticks() * 0.015) * 6)
    pygame.draw.polygon(screen, (230, 140, 0), [(bird_x - 10, int(bird_y)), (bird_x - 22, wing_y), (bird_x - 4, int(bird_y) + 6)])

    # واجهة النقاط والعدادات
    font = pygame.font.SysFont(None, 40)
    score_txt = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_txt, (20, 20))

    # شاشة الخسارة
    if game_over:
        font_large = pygame.font.SysFont(None, 60)
        go_txt = font_large.render("Game Over!", True, (220, 30, 30))
        retry_txt = font.render("Tap Screen to Play Again", True, (255, 255, 255))
        screen.blit(go_txt, (WIDTH // 2 - 120, HEIGHT // 2 - 40))
        screen.blit(retry_txt, (WIDTH // 2 - 150, HEIGHT // 2 + 30))

    pygame.display.flip()

pygame.quit()
sys.exit()
