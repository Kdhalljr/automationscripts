from Libraries.computer_lists import build_stores_list
from Libraries.Popen_background import Popen_background
from os import system

if __name__ == '__main__':
    output_file = open('check_enabled_winrm.txt', 'w+')

    for comp in build_stores_list():
        check_enabled_winrm, err = Popen_background('winrs -r:' + comp + ' hostname')
        if check_enabled_winrm.strip() == comp:
            output_file.write(comp + '\tenabled\n')
            print comp + '\tenabled'
        else:
            output_file.write(comp + '\tdisabled\n')
            print comp + '\tdisabled\n'

    output_file.close()
    system('pause')
