from Libraries.computer_lists import build_computer_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt


CHARS_IN_SERIAL_NUM = 7
LEN_INIT_TEXT = len('SerialNumber    ')


if __name__ == "__main__":
    username, password = user_pass_prompt()
    
    output_file = open('serial_numbers_stores.txt', 'w+')
    for comp in build_computer_list():
        serial_num, err = Popen_background('wmic /user:"crossroads\\' + username + '" /password:' + password + ' /node:"' + comp + '" bios get serialnumber')
        output_file.write(comp + ' =' + serial_num[LEN_INIT_TEXT : LEN_INIT_TEXT + CHARS_IN_SERIAL_NUM] + '\n\n')
        print comp + ' =' + serial_num[LEN_INIT_TEXT : LEN_INIT_TEXT + CHARS_IN_SERIAL_NUM] + '\n\n'

    output_file.close()
