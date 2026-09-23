[app]

# (str) Title of your application
title = Bird 3d py

# (str) Package name
package.name = birdkind3d

# (str) Package domain (needed for android packaging)
package.domain = org.bird3d

# (list) Source files to include (let it include python and assets)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion & exclusion patterns
source.include_patterns = assets/*,images/*.png

# (str) Application versioning
version = 1.0

# (list) Application requirements
# ملاحظة: أزلنا أي مكتبات معقدة لضمان نجاح التجميع
requirements = python3,pygame

# (list) Custom source folders for python modules
# source.dirs = ''

# (list) Permissions
# (e.g. INTERNET, ACCESS_FINE_LOCATION, etc.)
# android.permissions = INTERNET

# (str) Supported orientations (landscape is best for 3D/games)
orientation = landscape

# (list) List of services to declare
# android.services = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = .buildozer

# (str) Path to build output (bin)
# bin_dir = ./bin

# --- إعدادات أندرويد المتوافقة والمستقرة لمنع الأخطاء ---
[android]

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
# android.sdk = 24

# (str) ANT version to use
# android.ant = 1.9.4

# (bool) Use --private data storage (True) or --public (False)
android.private_storage = True

# (list) The Android archs to build for,, 
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.androidx = True
