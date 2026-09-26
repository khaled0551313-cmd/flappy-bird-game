[app]

# (str) Title of your application
title = Flappy Bird

# (str) Package name
package.name = flappybird

# (str) Package domain (needed for android packaging)
package.domain = org.game

# (str) Source directory where the application files are located
source.dir = .

# (list) Source files to include (let it match your python files and assets)
source.include_exts = py,png,jpg,kv,atlas,json,mp3,wav

# (str) Application versioning (مهم جداً: تم إضافته لمنع الخطأ)
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 34

# (int) Minimum API your APK will support (ليتوافق مع One UI 6.1)
android.min_api = 24

# (list) Supported architectures (معمارية 64-bit لهواتف سامسونج الحديثة)
android.archs = arm64-v8a

# (bool) Indicate whether the application should be fullscreen or not
android.fullscreen = 1

# (str) Log cat TAG prefix
android.logcat_tag = game

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
