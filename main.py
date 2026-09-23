import pygame
import sys
import math

# تهيئة بايثون والصوت
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1) # تهيئة قناة الصوت للأندرويد

WIDTH, HEIGHT = 1024, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Engine with Sound - Pygame")
clock = pygame.time.Clock()

# --- دالة لتوليد صوت ريترو برمجياً (يعمل 100% بدون ملفات خارجية) ---
def generate_retro_sound():
    sr = 44100
    dur = 0.1  # مدة الصوت قصيرة وسريعة
    buf = bytearray()
    for i in range(int(sr * dur)):
        t = i / sr
        # موجة جيبية بتردد يتغير ليعطي نغمة تفاعل ممتازة
        val = int(32767 * 0.5 * math.sin(2 * math.pi * (440 + t * 500) * t))
        buf += val.to_bytes(2, byteorder='little', signed=True)
    return pygame.mixer.Sound(buffer=bytes(buf))

click_sound = generate_retro_sound()

# بقية كود المكعب الثلاثي الأبعاد...
vertices = [
    [-100, -100, -100], [100, -100, -100], [100, 100, -100], [-100, 100, -100],
    [-100, -100, 100], [100, -100, 100], [100, 100, 100], [-100, 100, 100]
]

faces = [
    (0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 7, 3),
    (1, 5, 6, 2), (0, 1, 5, 4), (3, 2, 6, 7)
]

face_colors = [
    (200, 50, 50), (50, 200, 50), (50, 50, 200),
    (200, 200, 50), (200, 50, 200), (50, 200, 200)
]

angle_x, angle_y = 0, 0

running = True
while running:
    screen.fill((20, 20, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        # تشغيل الصوت عند الضغط على أي زر في الكيبورد أو اللمس على الشاشة
        elif event.type == pygame.KEYDOWN or event.type == pygame.FINGERDOWN:
            try:
                click_sound.play()
            except:
                pass

    angle_y += 0.02
    angle_x += 0.015

    sin_x, cos_x = math.sin(angle_x), math.cos(angle_x)
    sin_y, cos_y = math.sin(angle_y), math.cos(angle_y)

    projected_vertices = []
    transformed_vertices = []

    for vertex in vertices:
        x, y, z = vertex
        x1 = x * cos_y - z * sin_y
        z1 = z * cos_y + x * sin_y
        y2 = y * cos_x - z1 * sin_x
        z2 = z1 * cos_x + y * sin_x

        z_final = z2 + 500
        transformed_vertices.append((x1, y2, z_final))

        fov = 400
        factor = fov / max(z_final, 1)
        sx = int(WIDTH / 2 + x1 * factor)
        sy = int(HEIGHT / 2 + y2 * factor)
        projected_vertices.append((sx, sy))

    face_depths = []
    for i, face in enumerate(faces):
        avg_z = sum(transformed_vertices[v_idx][2] for v_idx in face) / 4
        face_depths.append((avg_z, [projected_vertices[v] for v in face], face_colors[i]))

    face_depths.sort(key=lambda x: x[0], reverse=True)

    for avg_z, points, color in face_depths:
        pygame.draw.polygon(screen, color, points)
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)

    # نص توضيحي على الشاشة
    font = pygame.font.SysFont(None, 32)
    txt = font.render("Press any key or tap screen to play sound", True, (255, 255, 255))
    screen.blit(txt, (20, 20))

    pygame.display.flip()
    clock.tick(60)
