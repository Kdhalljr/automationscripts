from Libraries.computer_lists import build_stores_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os import system

def chunks(list, n):
    #Yield successive n-sized chunks from l.
    for i in range(0, len(list), n):
        yield list[i:i + n]


if __name__ == '__main__':
    KB_ID = 'xxxxxx'
    OS_ARCH_DATA_INDEX = 1
    
    username, password = user_pass_prompt()
    output_file = open('check_for_certain_update.txt', 'w+')
    leftovers_file = open('leftovers_file.txt', 'w+')
    
    for comp in build_stores_list():
        arch_results, err = Popen_background('wmic /node:' + comp + ' /user:' + username + ' /password:' + password + ' os get osarchitecture')
        os_results, err = Popen_background('wmic /node:' + comp + ' /user:' + username + ' /password:' + password + ' os get name')
        wuauclt_results, err = Popen_background('wmic /node:' + comp + ' /user:' + username + ' /password: ' + password + ' qfe where "HotfixID = \'' + KB_ID + '\'" get HotfixID,InstalledOn')

        output_file.write(comp + '\n' + '--------------------------' + '\n')
        print comp + '\n' + '--------------------------' + '\n'
        
        if arch_results.strip() != '':
            arch_results = str(filter(None, arch_results.splitlines())[OS_ARCH_DATA_INDEX]).strip()
            output_file.write(arch_results + '\n')
            print arch_results
        else:
            print 'Could not gather arch number' + '\n'
        if os_results.strip() != '':
            os_results = str(filter(None, os_results.splitlines())[OS_ARCH_DATA_INDEX][:len('Microsoft Windows ##')].strip())
            output_file.write(os_results + '\n')
            print os_results + '\n'
        else:
            print 'Could not gather os version' + '\n'
        
        if wuauclt_results != []:
            output_file.write(str(wuauclt_results) + '\n\n')
            print str(wuauclt_results) + '\n\n'
        elif (wuauclt_results == []) and (os_results == 'Microsoft Windows 7'):
            leftovers_file.write(comp + '\n')
            leftovers_file.write(arch_results + '\n')
            leftovers_file.write(os_results + '\n\n')
                
    output_file.close()
    leftovers_file.close()
    
    system('pause')
