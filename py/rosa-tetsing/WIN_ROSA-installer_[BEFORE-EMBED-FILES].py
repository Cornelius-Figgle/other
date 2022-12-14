#!T:/projects/ROSA/rosa-env/Scripts/python.exe

'''
**purge time**

Ok so, originally this was intended to be cross-platofrm. It was hard and confusing and messy
I also realised, *nix users generally install stuf themselves, and my installer is probably incorrect for their specific system.

So. `git clone https://github.com/cornelius-figgle/ROSA.git` works still
I may also add ROSA to package managers en la futuro (especially the RPi one: `apt`, iirc)

So have fun on Windows,
	- Max, learning to be a dev
'''

import os
import pickle
import sys
from pathlib import Path
from threading import Thread

import PyQt5.QtWidgets as qt
from PyQt5.QtCore import Qt as QtCore
from PyQt5.QtGui import QPixmap
from requests import get
from win32com.client import Dispatch

#https://stackoverflow.com/a/11422350/19860022

if hasattr(sys, '_MEIPASS'): #https://stackoverflow.com/a/66581062/19860022
	file_base_path = sys._MEIPASS #https://stackoverflow.com/a/36343459/19860022
else:
	file_base_path = os.path.dirname(__file__)

#________________________________________________________________________________________________________________________________

class main(qt.QWizard):
	def __init__(self, parent=None) -> None:
		super(main, self).__init__(parent)

		if '_PYIBoot_SPLASH' in os.environ: #if compiled to exe
			from pyi_splash import close, update_text  # type: ignore
			update_text('UI Loaded...')
			close()

		self.setStyleSheet('QPushButton { background-color: lightgrey }') #set button style for all buttons
	
		self.addPage(licenseAgree())
		self.addPage(userConfig())
		self.addPage(installROSA())

		self.setWindowTitle('ROSA Installer (GUI)')

class licenseAgree(qt.QWizardPage): 
	def __init__(self, parent=None) -> None:
		super(licenseAgree, self).__init__(parent)

		licenseLayout = qt.QGridLayout()

		titleLabel = qt.QLabel('End User License Agreement')

		licenseText = qt.QLabel('\tMIT License\n\n\tCopyright (c) 2022 Max\n\n\tPermission is hereby granted, free of charge, to any person obtaining a copy\n\tof this software and associated documentation files (the "Software"), to deal\n\tin the Software without restriction, including without limitation the rights\n\tto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n\tcopies of the Software, and to permit persons to whom the Software is\n\tfurnished to do so, subject to the following conditions:\n\n\tThe above copyright notice and this permission notice shall be included in all\n\tcopies or substantial portions of the Software.\n\n\tTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n\tIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n\tFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n\tAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n\tLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n\tOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n\tSOFTWARE.')
		#lol long line
		licenseBox = qt.QScrollArea()

		licenseBox.setVerticalScrollBarPolicy(QtCore.ScrollBarAsNeeded)
		licenseBox.setHorizontalScrollBarPolicy(QtCore.ScrollBarAsNeeded)
		licenseBox.setWidgetResizable(True)
		licenseBox.setWidget(licenseText)

		agreeCb = qt.QLabel('By proceeding, you are agreeing to this license and its terms')

		licenseLayout.addWidget(titleLabel, 0, 0, 1, 2)

		licenseLayout.addWidget(licenseBox, 1, 0, 2, 2)

		licenseLayout.addWidget(qt.QLabel(''), 3, 0)

		licenseLayout.addWidget(agreeCb, 4, 0, 1, 2)

		self.setLayout(licenseLayout)

class userConfig(qt.QWizardPage):
	def __init__(self, parent=None) -> None:
		super(userConfig, self).__init__(parent)

		configLayout = qt.QGridLayout()
		shell = Dispatch('WScript.Shell')

		global installConfigs; installConfigs = {}
		
		installConfigs['filesToDownload'] = {
			'exe': 'https://raw.githubusercontent.com/Cornelius-Figgle/ROSA/main/bin/ROSA.exe',
			'UAC': 'https://raw.githubusercontent.com/Cornelius-Figgle/ROSA/main/bin/ROSA-installer_uac.exe',
			'bat': 'https://raw.githubusercontent.com/Cornelius-Figgle/ROSA/main/bin/create_shortcut.bat',
			'config': 'https://raw.githubusercontent.com/Cornelius-Figgle/ROSA/main/gpio.json', 
			'readme': 'https://raw.githubusercontent.com/Cornelius-Figgle/ROSA/main/bin/README.md', 
			'ico': 'https://raw.githubusercontent.com/Cornelius-Figgle/ROSA/main/ico/hotpot-ai.ico',
			'png': 'https://raw.githubusercontent.com/Cornelius-Figgle/ROSA/main/ico/hotpot-ai.png'
		}

		installConfigs['programPath'] = os.path.expandvars('%ProgramFiles%')
		installConfigs['dataPath'] = os.path.expandvars('%AppData%')
		installConfigs['startPath'] = shell.SpecialFolders('Programs') #os.path.expandvars('%AppData%\Microsoft\Windows\Start Menu'))
		installConfigs['deskPath'] = shell.SpecialFolders('Desktop') #os.path.expanduser('~\Desktop'))

		dirButton = qt.QPushButton('Program Files Path: ')
		dirButton.clicked.connect(lambda: self.chooseDir(dirLabel, dirButton, 'programPath', 'Program Files Path: '))
		dirLabel = qt.QLineEdit(installConfigs['programPath']) #https://docs.python.org/3/library/os.path.html#os.path.expandvars
		self.validateType(dirLabel, dirButton, 'programPath', 'Program Files Path: ')
		dirLabel.textChanged.connect(lambda: self.validateType(dirLabel, dirButton, 'programPath', 'Program Files Path: '))

		dataButton = qt.QPushButton('AppData Path: ')
		dataButton.clicked.connect(lambda: self.chooseDir(dataLabel, dataButton, 'dataPath', 'AppData Path: '))
		dataLabel = qt.QLineEdit(installConfigs['dataPath'])
		self.validateType(dataLabel, dataButton, 'dataPath', 'AppData Path: ')
		dataLabel.textChanged.connect(lambda: self.validateType(dataLabel, dataButton, 'dataPath', 'AppData Path: '))

		cb1 = qt.QCheckBox('Add shortcut to Start Menu')
		cb1.setChecked(True)
		cb1Button = qt.QPushButton('Start Menu Path: ')
		cb1Button.clicked.connect(lambda: self.chooseDir(cb1Label, cb1Button, 'startPath', 'Start Menu Path: '))
		cb1Label = qt.QLineEdit(installConfigs['startPath'])
		self.validateType(cb1Label, cb1Button, 'startPath', 'Start Menu Path: ')
		cb1Label.textChanged.connect(lambda: self.validateType( cb1Label, cb1Button, 'startPath', 'Start Menu Path: '))
		cb1.stateChanged.connect(lambda: self.saveCheckStatus(cb1, 'startShortcut'))

		cb2 = qt.QCheckBox('Add shortcut to Desktop')
		cb2.setChecked(False)
		cb2Button = qt.QPushButton('Desktop Path: ')
		cb2Button.clicked.connect(lambda: self.chooseDir(cb2Label, cb2Button, 'deskPath', 'Desktop Path: '))
		cb2Label = qt.QLineEdit(installConfigs['deskPath'])
		self.validateType(cb2Label, cb2Button, 'deskPath', 'Desktop Path: ')
		cb2Label.textChanged.connect(lambda: self.validateType(cb2Label, cb2Button, 'deskPath', 'Desktop Path: '))
		cb2.stateChanged.connect(lambda: self.saveCheckStatus(cb1, 'startShortcut'))

		configLayout.addWidget(dirButton, 0, 0)
		configLayout.addWidget(dirLabel, 0, 1)

		configLayout.addWidget(dataButton, 1, 0)
		configLayout.addWidget(dataLabel, 1, 1)


		configLayout.addWidget(qt.QLabel(''), 2, 0)

		configLayout.addWidget(cb1, 3, 0)
		configLayout.addWidget(cb1Button, 4, 0)
		configLayout.addWidget(cb1Label, 4, 1)

		configLayout.addWidget(qt.QLabel(''), 5, 0)

		configLayout.addWidget(cb2, 6, 0)
		configLayout.addWidget(cb2Button, 7, 0)
		configLayout.addWidget(cb2Label, 7, 1)

		self.setLayout(configLayout)

	def pathIsGood(self, path: str) -> str | None: return path if path and os.path.exists(path) and os.access(path, os.X_OK | os.W_OK) else None

	def validateType(self, label, display, config, revert) -> bool: 
		global installConfigs

		try:
			installConfigs['startShortcut'] = True if self.cb1.isChecked() else False
			installConfigs['deskShortcut'] = True if self.cb2.isChecked() else False
		except NameError: pass #intelligent cod3
		except AttributeError: pass #big bran m0ve

		path = label.text()
		path = self.pathIsGood(path)
		if not path:
			display.setText(f'Invalid \'{config}\'')

			display.setStyleSheet('background-color : red')
			#f = wizard.button(qt.QWizard.WizardButton.NextButton).font() ; f.setStrikeOut(True) ; wizard.button(qt.QWizard.WizardButton.NextButton).setFont(f)
			f = label.font() ; f.setStrikeOut(True) ; label.setFont(f)

			return False
		else:
			installConfigs[config] = path
			display.setText(revert)

			display.setStyleSheet('background-color : lightgrey')
			#f = wizard.button(qt.QWizard.WizardButton.NextButton).font() ; f.setStrikeOut(False) ; wizard.button(qt.QWizard.WizardButton.NextButton).setFont(f)
			f = label.font() ; f.setStrikeOut(False) ; label.setFont(f)

			return True        

	def chooseDir(self, label, display, config, revert) -> None: 
		path = qt.QFileDialog.getExistingDirectory('Select Dir')
		if self.pathIsGood(path): 
			label.setText(path) 
			self.validateType(label, display, config, revert)

	def saveCheckStatus(self, cb: qt.QCheckBox, config) -> None:
		global installConfigs
		installConfigs[config] = True if cb.isChecked() else False
		print(f'CheckBox \'{cb}\' Toggled')

class installROSA(qt.QWizardPage): 
	def __init__(self, parent=None) -> None:
		super(installROSA, self).__init__(parent)

		installLayout = qt.QGridLayout()

		label = qt.QLabel() #https://stackoverflow.com/a/40294286/19860022
		pixmap = QPixmap(os.path.join(file_base_path, '/ico/hotpot-ai.png'))
		label.setPixmap(pixmap)

		self.infoLabel = qt.QLabel(' ')
		self.infoLabel.setWordWrap(True)

		#display text to right of imag
		self.bar = qt.QProgressBar()

		installLayout.addWidget(label, 0, 0)
		installLayout.addWidget(self.infoLabel, 0, 1)
		installLayout.addWidget(self.bar, 1, 0, 1, 2)

		self.setLayout(installLayout)

		self.downloadedFiles = {}

	def initializePage(self) -> None:
		print(installConfigs)

		fred = Thread(target=self.threadProcesses) #so can dwld whilst display imag
		fred.start()

	def threadProcesses(self) -> None:
		self.downloadedFiles['bin'] = self.download_file(installConfigs['filesToDownload']['exe'])
		self.downloadedFiles['adm'] = self.download_file(installConfigs['filesToDownload']['UAC'])
		self.downloadedFiles['bat'] = self.download_file(installConfigs['filesToDownload']['bat'])
		self.downloadedFiles['config'] = self.download_file(installConfigs['filesToDownload']['config'])
		self.downloadedFiles['readme'] = self.download_file(installConfigs['filesToDownload']['readme'])
		self.downloadedFiles['ico'] = self.download_file(installConfigs['filesToDownload']['ico'])

		self.make_shortcut(self.downloadedFiles['bin'], os.path.join(installConfigs['startPath'], 'ROSA'))
		self.make_shortcut(self.downloadedFiles['config'], os.path.join(installConfigs['startPath'], 'ROSA'))
		self.make_shortcut(self.downloadedFiles['readme'], os.path.join(installConfigs['startPath'], 'ROSA'))
		self.make_shortcut(self.downloadedFiles['bin'], installConfigs['deskPath'])

		with open(os.path.join(file_base_path, 'installConfigs.pickle'), 'wb') as file:
			pk1 = pickle.dump(installConfigs, file)
		with open(os.path.join(file_base_path, 'downloadedFiles.pickle'), 'wb') as file:
			pk2 = pickle.dump(self.downloadedFiles, file)
		os.system(f'{self.downloadedFiles["adm"]} {pk1} {pk2}')	

		print('install complete!')
		self.infoLabel.setText('install complete!')

	def download_file(self, url) -> str:
		local_dirname = os.path.join(file_base_path, 'temp_dwld')
		local_filename = os.path.join(local_dirname, url.split('/')[-1])

		print(f'creating dirs "{local_dirname}"')
		self.infoLabel.setText(f'creating dirs "{local_dirname}"')

		os.makedirs(local_dirname, exist_ok=True)

		print(f'starting download for "{local_filename}"')
		self.infoLabel.setText(f'starting download for "{local_filename}"')

		with get(url, stream=True) as r:
			with open(local_filename, 'w', encoding="utf-8") as f:
				f.write(r.text)

		print(f'finished download for "{local_filename}"')
		self.infoLabel.setText(f'finished download for "{local_filename}"')

		return local_filename    

	def make_shortcut(self, source, dest_dir, dest_name=None) -> None:
		'''
		Make shortcut of `source` path to file in `dest_dir` target folder
		If `dest_name` is None, will use `source`'s filename
		'''

		# process user input
		if dest_name is None:
			dest_name = Path(source).name
		dest_path = str(Path(dest_dir, dest_name)) + '.lnk'

		if not os.path.exists(dest_dir):
			print(f'creating dirs "{dest_dir}"')
			self.infoLabel.setText(f'creating dirs "{dest_dir}"')

			os.makedirs(dest_dir, exist_ok=True)

		print(f'creating shortcut at "{dest_path}"')
		self.infoLabel.setText(f'creating shortcut at "{dest_path}"')

		os.system(f'{self.downloadedFiles["bat"]} {source} {dest_path} {source} "ROBOTICALLY OBNOXIOUS SERVING ASSISTANT - An emotional smart assistant that doesn\'t listen to you"')
		# print status
		print(f'{source}\n-->\n{dest_path}')
		self.infoLabel.setText(f'{source}\n-->\n{dest_path}')

		print(f'created shortcut at "{dest_path}"')
		self.infoLabel.setText(f'created shortcut at "{dest_path}"')

#________________________________________________________________________________________________________________________________

if __name__ == '__main__':
	app = qt.QApplication(sys.argv)
	wizard = main()
	wizard.show()
	sys.exit(app.exec_())
