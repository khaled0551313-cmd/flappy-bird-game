[app]

# (str) Title of your application
title = My 3D Game

# (str) Package name
package.name = my3dgame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.game

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf,obj

# (list) Application requirements
requirements = python3,pygame

# (str) Supported orientations
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (str) Supported archs
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
