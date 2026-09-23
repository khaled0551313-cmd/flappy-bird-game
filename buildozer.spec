[app]

# (str) Title of your application
title = Bird real 3D

# (str) Package name
package.name = birdkind3d

# (str) Package domain (needed for android packaging)
package.domain = org.bird3d

# (str) Source directory where the application files are located
source.dir = .

# (list) Source files to include (let it include python and assets)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion & exclusion patterns
source.include_patterns = assets/*,images/*.png

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,pygame

# (str) Supported orientations (portrait or landscape)
orientation = portrait

# (list) Permissions
# android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# --- إعدادات أندرويد المتوافقة والمستقرة لمنع الأخطاء ---
[android]

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.androidx = True
