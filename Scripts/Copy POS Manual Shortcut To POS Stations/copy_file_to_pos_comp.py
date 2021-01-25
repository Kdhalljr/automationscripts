from Libraries.computer_lists import build_pos_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os import system

if __name__ == "__main__":

    username, password = user_pass_prompt()
    
    output_file = open('copy_results.txt', 'w+')

    for comp in build_pos_list():
        create_key_results, err = Popen_background('cmdkey /add:' + comp + ' /user:' + username + ' /password:' +  password)
        copy_result, err = Popen_background('xcopy /k /i /y "Pay Out & Pay-In Categories.pdf.lnk" \\\\' + comp + '\c$\Users\Public\Desktop')
        output_file.write(comp + ' = ' + copy_result + '\n')

        print comp + ' = ' + copy_result

    output_file.close()

    system('pause')
