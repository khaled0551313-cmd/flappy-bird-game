[app]

# (str) Title of your application
title = Bird Kind 3D

# (str) Package name
package.name = birdkind3d

# (str) Package domain (needed for android packaging)
package.domain = org.birdkind

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# تم إزالة numpy واستبدالها بمكتبة الـ 3D لضمان نجاح البناء على أندرويد
requirements = python3, pygame, pygame-3d-engine

# (str) Supported orientations (landscape, portrait or all)
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 24
android.ndk_api = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True

# (list) Accept SDK License
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
