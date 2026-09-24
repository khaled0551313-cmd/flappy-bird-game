[app]

title = Flappy Bird Game
package.name = flappybird
package.domain = org.flappy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,wav

# استخدام pygame-ce بدلاً من pygame العادية
requirements = python3,pygame-ce

version = 0.1
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.private_storage = True

[buildozer]
log_level = 2
