[app]

# (str) Title of your application
title = 3D Cube Engine

# (str) Package name
package.name = cubeengine3d

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav,obj

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data dir (True), or --dir public storage (False)
android.private_storage = True

# (bool) Accept SDK licences automatically
android.accept_sdk_licence = True

# (list) The Android architectures to build for
# We target arm64-v8a only to prevent NDK harfbuzz compilation failures on Github Actions
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

#
# Buildozer section
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn, 2 = error)
warn_on_root = 1
