import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable('emailandnumberscrapper.py', base=base, icon='scrapper.ico')]

cx_Freeze.setup(

    name="Email and Phone Numbers Scrapper",
    options={"build_exe": {"packages": ['tkinter', 're'], "include_files": ['scrapper.ico']}},
    version='1.0.0',
    description='Email and Phone Numbers Scrapper \n Created By: Jerrol Montemayor',
    executables=executables
)
