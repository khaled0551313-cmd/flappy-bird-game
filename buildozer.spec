[app]

title = Bird Sanctuary
package.name = birdsanctuary
package.domain = org.cozy
source.dir = .
source.include_exts = py
requirements = python3==3.10,pygame
version = 0.1
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.archs = arm64-v8a

# أضف هذه الأسطر الجديدة لضمان استقرار التحميل
p4a.branch = master
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
