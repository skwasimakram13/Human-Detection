# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['human_detection.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/Sherni/Greet Bot/yolov3.cfg', '.'), ('D:/Sherni/Greet Bot/yolov3.weights', '.'), ('D:/Sherni/Greet Bot/haarcascade_frontalface_default.xml', '.'), ('D:/Sherni/Greet Bot/facevoice.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='human_detection',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['app.ico'],
)
