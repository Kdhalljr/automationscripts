from Libraries.computer_lists import build_local_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os.path import getsize, join
from os import system, walk

if __name__ == "__main__":

    username, password = user_pass_prompt()
    
    output_file = open('copy_results_TEMP.txt', 'w+')
    for comp in build_local_list():
        create_key_results, err = Popen_background('cmdkey /add:' + comp + ' /user:' + username + ' /password:' +  password)
        size = 0
        try:
            for dirpath, dirnames, filenames in walk('\\\\' + comp + '\\c$\\TEMP'):
                for f in filenames:
                    fp = join(dirpath, f)
                    size += getsize(fp)
            print '\\\\' + comp + '\\c$\\TEMP = ' + str(size) + ' bytes'
            output_file.write('\\\\' + comp + '\\c$\\TEMP = ' + str(size) + ' bytes\n')
        except WindowsError:
            print '\\\\' + comp + '\\c$\\TEMP = Could Not Find File'
            output_file.write('\\\\' + comp + '\\c$\\TEMP = Could Not Find File\n')

    output_file.close()
    
    system('pause')
