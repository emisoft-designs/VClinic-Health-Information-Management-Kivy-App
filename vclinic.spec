# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2, glew
import os

# Adding the correct paths for files
add_files = [
    ('frontend\\interface\\*.kv', 'interface'),
    ('frontend\\interface\\auth\\*.kv', 'interface\\auth'), 
    ('frontend\\interface\\clinic\\gynae\\*.kv', 'interface\\clinic\\gynae'),
    ('frontend\\interface\\clinic\\obstetrics\\*.kv', 'interface\\clinic\\obstetrics'),
    ('frontend\\interface\\lab\\*.kv', 'interface\\lab'),
    ('frontend\\interface\\lab\\records\\*.kv', 'interface\\lab\\records'),
    ('frontend\\interface\\lab\\tests\\*.kv', 'interface\\lab\\tests'), 
    ('frontend\\interface\\register\\*.kv', 'interface\\register'), 
    ('frontend\\static\\images\\*.png', 'static\\images'), 
    ('frontend\\static\\images\\*.ico', 'static\\images'), 
    ('frontend\\static\\images\\*.jpg', 'static\\images'),
]

a = Analysis(
    ['frontend/main.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=add_files,
    hiddenimports=['kivymd.icon_definitions', 'kivymd.uix.datatables', 'kivymd.uix.dropdownitem'],
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
    Tree('frontend'),
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    name='vclinic',
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
    icon=['frontend/static/images/icon_sm.ico'],
    version='frontend/version.txt',
    author='Somtochukwu Owen Ikeanyi'
)

coll = COLLECT(
    exe,
    Tree('frontend'),
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    name='vclinic'
)