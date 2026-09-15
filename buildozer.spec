[app]
title = Video1grab
package.name = video1grab
package.domain = org.video1grab

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,yt-dlp,requests,urllib3,charset-normalizer,idna,certifi

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
