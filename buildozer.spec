[app]

# (str) Title of your application
title = FlappyBirdGame

# (str) Package name
package.name = mygame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (add extensions of your images/sounds if any)
source.include_exts = py,png,jpg,jpeg,ttf,wav,mp3

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,pygame

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API required
android.minapi = 24

# (str) Android NDK architecture to build for
android.archs = arm64-v8a

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 0
