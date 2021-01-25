from Libraries.computer_lists import build_stores_list
from Libraries.Popen_background import Popen_background
from os import system

if __name__ == '__main__':
    for comp in build_stores_list():
        remote_wuauclt_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec \\\\' + comp + ' -s reg query "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Detect" -v LastSuccessTime')
        print comp + '\n' + remote_wuauclt_results + '\n'
        system('pause')
