[app]

# (str) Title of your application
title = My 3D Game

# (str) Package name
package.name = my3dgame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.game

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let it empty to include all)
source.include_exts = py,png,jpg,kv,atlas,ttf,obj

# (list) Application requirements
# تأكد هنا من إضافة pygame والمكتبات التي تعتمد عليها اللعبة
requirements = python3,pygame

# (str) Supported orientations (landscape أفضل للألعاب الثلاثية الأبعاد)
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (str) Supported archs (أفضل وأسرع توافق للأندرويد الحديث)
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
