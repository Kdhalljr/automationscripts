from Libraries.computer_lists import build_computer_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt

LEN_EXTRA_SPACE = 8
LEN_INIT_TEXT = len('Name          ')


if __name__ == "__main__":
    username, password = user_pass_prompt()
    output_file = open('comp_models_stores.txt', 'w+')
    
    for comp in build_computer_list():
        serial_num, err = Popen_background('wmic /user:"crossroads\\' + username + '" /password:' + password + ' /node:"' + comp + '" csproduct get name')
        output_file.write(comp + ' =' + serial_num[LEN_INIT_TEXT : -LEN_EXTRA_SPACE] + '\n\n')
        print comp + ' =' + serial_num[LEN_INIT_TEXT : -LEN_EXTRA_SPACE] + '\n\n'
        
    output_file.close()

