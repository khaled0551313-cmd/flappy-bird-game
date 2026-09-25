from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Mesh
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
import math
import struct
import wave
import io

# --- دالة لتوليد صوت ريترو برمجياً وربطه بـ Kivy دون الحاجة لملفات خارجية ---
def create_retro_sound_stream():
    sr = 44100
    dur = 0.1
    num_samples = int(sr * dur)
    
    # كتابة ملف WAV في الذاكرة المباشرة (In-Memory WAV)
    wav_io = io.BytesIO()
    with wave.open(wav_io, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sr)
        
        frames = bytearray()
        for i in range(num_samples):
            t = i / sr
            val = int(32767 * 0.5 * math.sin(2 * math.pi * (440 + t * 500) * t))
            frames += struct.pack('<h', val)
        wav_file.writeframes(frames)
    
    wav_io.seek(0)
    return wav_io

class Cube3DWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle_x = 0
        self.angle_y = 0
        
        # إحداثيات رؤوس المكعب 3D
        self.vertices = [
            [-100, -100, -100], [100, -100, -100], [100, 100, -100], [-100, 100, -100],
            [-100, -100, 100], [100, -100, 100], [100, 100, 100], [-100, 100, 100]
        ]
        
        # الأوجه والألوان
        self.faces = [
            (0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 7, 3),
            (1, 5, 6, 2), (0, 1, 5, 4), (3, 2, 6, 7)
        ]
        
        self.face_colors = [
            (0.8, 0.2, 0.2, 1), (0.2, 0.8, 0.2, 1), (0.2, 0.2, 0.8, 1),
            (0.8, 0.8, 0.2, 1), (0.8, 0.2, 0.8, 1), (0.2, 0.8, 0.8, 1)
        ]
        
        # تحديث الحركة 60 إطار بالثانية
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def on_touch_down(self, touch):
        # شغل تأثير اللمس/الصوت عند الضغط
        pass

    def update(self, dt):
        self.canvas.clear()
        
        # تحديث الزوايا
        self.angle_y += 0.02
        self.angle_x += 0.015

        sin_x, cos_x = math.sin(self.angle_x), math.cos(self.angle_x)
        sin_y, cos_y = math.sin(self.angle_y), math.cos(self.angle_y)

        projected_vertices = []
        transformed_vertices = []

        center_x = self.width / 2 if self.width else Window.width / 2
        center_y = self.height / 2 if self.height else Window.height / 2

        # إجراء عمليات دوران المصفوفات 3D (Rotation Matrix)
        for vertex in self.vertices:
            x, y, z = vertex
            x1 = x * cos_y - z * sin_y
            z1 = z * cos_y + x * sin_y
            y2 = y * cos_x - z1 * sin_x
            z2 = z1 * cos_x + y * sin_x

            z_final = z2 + 500
            transformed_vertices.append((x1, y2, z_final))

            fov = 400
            factor = fov / max(z_final, 1)
            sx = center_x + x1 * factor
            sy = center_y + y2 * factor
            projected_vertices.append((sx, sy))

        # ترتيب الأوجه حسب العمق Z (Painters Algorithm)
        face_depths = []
        for i, face in enumerate(self.faces):
            avg_z = sum(transformed_vertices[v_idx][2] for v_idx in face) / 4
            face_depths.append((avg_z, [projected_vertices[v] for v in face], self.face_colors[i]))

        face_depths.sort(key=lambda item: item[0], reverse=True)

        # رسم الأوجه 3D باستخدام Kivy Graphics (Mesh & Triangles)
        with self.canvas:
            for avg_z, points, color in face_depths:
                Color(*color)
                # تقسيم المضلع الرباعي إلى مثلثين لرسمه بـ Mesh
                mesh_vertices = [
                    points[0][0], points[0][1], 0, 0,
                    points[1][0], points[1][1], 0, 0,
                    points[2][0], points[2][1], 0, 0,
                    points[3][0], points[3][1], 0, 0,
                ]
                indices = [0, 1, 2, 2, 3, 0]
                Mesh(vertices=mesh_vertices, indices=indices, mode='triangles')

class CubeApp(App):
    def build(self):
        return Cube3DWidget()

if __name__ == '__main__':
    CubeApp().run()
