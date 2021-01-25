from Libraries.computer_lists import build_mgr_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
import csv
import sys

if __name__ == "__main__":
    username, password = user_pass_prompt()

    output_file = open('ms_office_versions.txt', 'w+')
    for comp in build_mgr_list():
        software_list, err = Popen_background('wmic /user: "' + comp + '\\' + username + '" /password:"' + password + '" /node:"' + comp + '" product get name')
        ms_ver_index = software_list.find('Microsoft Office Standard')
        if ms_ver_index != -1:
            office_version = software_list[ms_ver_index:ms_ver_index + len('Microsoft Office Standard xxxx')]
        else:
            office_version = None
        output_file.write(comp + ' = ' + str(office_version) + '\n') 
        print comp + ' = ' + str(office_version)

    output_file.close()
