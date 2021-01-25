from Libraries.computer_lists import build_hq01_comp_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os.path import exists
from os import makedirs
from os import system

if __name__ == "__main__":

    username, password = user_pass_prompt() 

    output_file = open('copy_results.txt', 'w+')
    for comp in build_hq01_comp_list():
        archive_path = '\\\\xxxxxxx' + comp + '\\'
        source_path = '\\\\' + comp + 'xxxxxx'
        comp_c_directory = '\\\\' + comp + '\\c$'
        
        create_key_results, err = Popen_background('cmdkey /add:' + comp + ' /user:' + username + ' /password:' +  password)  
        #if not exists(archive_path) and exists(comp_c_directory):
        #    makedirs(archive_path)

        if exists(source_path):
            copy_result, err = Popen_background('xcopy /s /y ' + source_path + '* ' + archive_path)
            output_file.write(comp + ' = ' + copy_result + '\n')
            print comp + ' = ' + copy_result
        else:
            output_file.write(comp + ' = computer off \n')
            print comp + ' = computer off'

    output_file.close()

    system('pause')
