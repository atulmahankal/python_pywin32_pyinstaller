import PyInstaller.__main__

PyInstaller.__main__.run([
    'service.py',
    '--onefile',
		'--hidden-import=win32timezone',
		'--hidden-import=servicemanager',
		'--icon=application.ico',
		'--add-data=application.ico:application.ico',
		# '--splash=splash.png',
		# '--add-data=splash.png:splash.png',
		'--version-file=version.txt',
])