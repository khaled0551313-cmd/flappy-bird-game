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
# ركز هنا: بايثون وبايجيم فقط لضمان الاستقرار التام
requirements = python3,pygame

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (list) Supported architectures
android.archs = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = False)
warn_on_root = 1
