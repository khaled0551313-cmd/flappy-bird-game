[app]

title = Bird Kind 2.5D
package.name = birdkind25d
package.domain = org.birdkind
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3, pygame, numpy

orientation = landscape
fullscreen = 1
android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk_api = 24
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
