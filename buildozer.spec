[app]

title = Flappy Bird Game
package.name = flappybird
package.domain = org.flappy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,wav

# استخدام pygame-ce بدلاً من pygame العادية
requirements = python3==3.10.12,pygame-ce

version = 0.1
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 27.3.13750724
android.private_storage = True

[buildozer]
log_level = 2
