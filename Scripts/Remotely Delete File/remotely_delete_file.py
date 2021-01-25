from Libraries.computer_lists import build_pos_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os import system
from os.path import exists

if __name__ == "__main__":

    username, password = user_pass_prompt()
    
    output_file = open('delete_results.txt', 'w+')
    file_name_to_delete = '"POS Manual.pdf.lnk"'
    for comp in build_pos_list():
        create_key_results, err = Popen_background('cmdkey /add:' + comp + ' /user:' + username + ' /password:' +  password)
        if (exists('\\\\' + comp + '\\c$\\Users\\Public\\Desktop\\POS Manual.pdf.lnk')):
            print 'file found'
            delete_result, err = Popen_background('del \\\\' + comp + '\\c$\\Users\\Public\\Desktop\\"POS Manual.pdf.lnk"')
            delete_result = 'deleted'
        else:
            delete_result = ''

        output_file.write(comp + ' = ' + delete_result + '\n')
        
        print comp + ' = ' + delete_result

    output_file.close()

    system('pause')
