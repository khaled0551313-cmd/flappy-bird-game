[app]

# (str) Title of your application
title = Bird Kind 2.5D

# (str) Package name
package.name = birdkind25d

# (str) Package domain (needed for android packaging)
package.domain = org.birdkind

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# تمت إضافة numpy لتوليد الأصوات برمجياً بدون ملفات خارجية
requirements = python3, pygame, numpy

# (str) Supported orientations (landscape, portrait or all)
# تم ضبطها على landscape لتناسب الرؤية البصرية ثلاثية الأبعاد
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) List of Java .jar files to add to the libs so that Pygame can build properly
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = error, 1 = warning)
warn_on_root = 1
