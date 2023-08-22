[app]

title = My Chatbot
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.7.6,hostpython3==3.7.6, kivy, pillow, chatbot.py
orientation = portrait

# osx settings

osx.python_version = 3.7.6
osx.kivy_version = 2.2.1

# android settings

fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# python-for-android settings

p4a.branch = develop

# ios settings

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]

log_level = 2
warn_on_root = 1
