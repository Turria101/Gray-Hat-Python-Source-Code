# Backdoor builder
from distutils.core import setup
import py2.exe

setup(console=['backdoor.py'],
      options = {'py2exe':{'bundle_files':1}},
      zipfile = None,                
      )
