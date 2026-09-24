[app]

# (str) Title of your application
title = Flappy Bird Game

# (str) Package name
package.name = flappybird

# (str) Package domain (needed for android packaging)
package.domain = org.flappy

# (list) Source files to include (let it include your python script and assets)
source.include_exts = py,png,jpg,kv,atlas,ttf,wav

# (list) Application requirements
# استخدام إصدار مستقر ومباشر لضمان عدم حدوث مشاكل التطابق
requirements = python3,pygame

# (str) Supported orientations (landscape or portrait)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 27.3.13750724

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2
