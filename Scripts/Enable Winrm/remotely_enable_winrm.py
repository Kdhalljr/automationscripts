from Libraries.computer_lists import build_stores_list
from Libraries.Popen_background import Popen_background

if __name__ == '__main__':
    for comp in build_stores_list():
        install_winrm_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec \\\\' + comp + ' -s "C:\\Windows\\System32\\winrm.cmd quickconfig -q"')
        print comp
        print '-------------------'
        print install_winrm_results
