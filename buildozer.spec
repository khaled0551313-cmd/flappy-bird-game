[app]

# (str) Title of your application
title = My Game App

# (str) Package name
package.name = mygameapp

# (str) Package domain (needed for android packaging)
package.domain = org.game

# (list) Source files to include (let it match your python files and assets)
source.include_exts = py,png,jpg,kv,atlas,json,mp3,wav

# (list) Application requirements
# (أضف هنا المكتبات التي تستخدمها لعبتك، مثل kivy أو pygame وغيرها)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support (مهم جداً ألا يقل عن 24 ليتوافق مع جهازك)
android.min_api = 24

# (list) Supported architectures (معمارية 64-bit الإلزامية لهواتف سامسونج الحديثة)
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
