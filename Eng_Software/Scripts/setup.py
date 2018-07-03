import sys
from cx_Freeze import setup, Executable
import PyQt5
import Janela_1
import Janela_3, janela_4, finish, warning
import

base = None
if sys.platform == "win32":
    base = "Win32GUI"
icon = 'AHP.ico'

executables = [Executable("Main.py", base=base, icon = icon)]

buildOptions = dict(
    packages = ["Qt5"],
    includes = ["PyQt5","Janela_1", "Janela_3", "janela_4", "finish", "finish"]
)


setup(
    name = "Calculadora AHP",
    options = dict(buid_exe = buildOptions),
    version = "0.9",
    description = 'Programa para disciplina de Engenharia de SOftware',
    executables = executables
)