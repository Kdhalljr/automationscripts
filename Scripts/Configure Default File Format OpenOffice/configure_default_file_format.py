from Libraries.computer_lists import build_pos_list, build_buy_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os import system
from os.path import exists


if __name__ == "__main__":

    username, password = user_pass_prompt()
    
    output_file = open('copy_results.txt', 'w+')

    remote_dest1 = 'xxxxxx'
    remote_dest2 = 'xxxxxx'
    remote_dest3 = 'xxxxxx'
    remote_dest4 = 'xxxxxx'
    
    for comp in build_pos_list() + build_buy_list():

        create_key_results, err = Popen_background('cmdkey /add:' + comp + ' /user:' + username + ' /password:' +  password)
        copy_result = ''
        
        if exists('\\\\' + comp + remote_dest1):
            copy_result, err = Popen_background('xcopy /k /i /y registrymodifications.xcu \\\\' + comp + remote_dest1)
        elif exists('\\\\' + comp + remote_dest2):
            copy_result, err = Popen_background('xcopy /k /i /y registrymodifications.xcu \\\\' + comp + remote_dest2)
        elif exists('\\\\' + comp + remote_dest3):
            copy_result, err = Popen_background('xcopy /k /i /y registrymodifications.xcu \\\\' + comp + remote_dest3)
        elif exists('\\\\' + comp + remote_dest4):
            copy_result, err = Popen_background('xcopy /k /i /y registrymodifications.xcu \\\\' + comp + remote_dest4)
            
        output_file.write(comp + ' = ' + copy_result + '\n')
        print comp + ' = ' + copy_result
        
    output_file.close()

    system('pause')
