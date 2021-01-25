from Libraries.computer_lists import build_mgr_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os import system
import csv
import sys

if __name__ == "__main__":
    username, password = user_pass_prompt()

    output_file = open('adobe_standard_installed.txt', 'w+')
    for comp in build_mgr_list():
        software_list, err = Popen_background('wmic /user: "' + comp + '\\' + username + '" /password:"' + password + '" /node:"' + comp + '" product get name')
        adobe_reader_index = software_list.find('Adobe Acrobat')

        if adobe_reader_index != -1:
            reader_installed = software_list[adobe_reader_index:adobe_reader_index + len('Adobe Acrobat XX XXXXXXXX')]
        else:
            reader_installed = None

        output_file.write(comp + ' = ' + str(reader_installed) + '\n') 
        print comp + ' = ' + str(reader_installed)

    output_file.close()
    system('pause')
