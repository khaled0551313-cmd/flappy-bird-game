[app]

# (str) Title of your application
title = Bird Sanctuary

# (str) Package name
package.name = birdsanctuary

# (str) Package domain (needed for android/ios packaging)
package.domain = org.cozy

# (str) Source code where the main.py live
source.dir = .

# (str) Source files to include (let empty to include all the files)
source.include_exts = py

# (list) Application requirements
requirements = python3,pygame

# (str) Version of your application (هذا هو السطر الذي كان ناقصاً وتمت إضافته)
version = 0.1

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (list) Supported architectures
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
