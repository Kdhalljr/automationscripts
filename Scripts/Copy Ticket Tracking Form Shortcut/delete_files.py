from Libraries.computer_lists import build_computer_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os import system, remove
from os.path import exists

if __name__ == "__main__":

    username, password = user_pass_prompt()
    
    output_file = open('results.txt', 'w+')

    for comp in build_computer_list():
        create_key_results, err = Popen_background('cmdkey /add:' + comp + ' /user:' + username + ' /password:' +  password)
        file_path = '\\\\' + comp + '\\c$\\Users\\Public\\Desktop\\Support Ticket Form.url'
        if exists('\\\\' + comp + '\\c$'):
            if exists(file_path):
                print comp + ' File Exists, removed'
                remove(file_path)
                output_file.write(comp + ' File Exists, removed')
            else:
                print comp + ' No File Exists'
                output_file.write(comp + ' File Does Not Exist')
        else:
            print comp + ' Cant connect'
            output_file.write(comp + ' Cant connect')
            
    output_file.close()

    system('pause')
