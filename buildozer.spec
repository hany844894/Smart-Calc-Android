[app]
title = MySmartCalc
package.name = smartcalc
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.skip_update = False
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1