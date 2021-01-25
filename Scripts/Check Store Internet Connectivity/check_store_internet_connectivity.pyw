from Libraries.computer_lists import build_local_list
from Libraries.Popen_background import Popen_background
import ctypes


def get_num_pings(ping_result):
    num_pings = 0
    
    for line in ping_result.splitlines():
        if (line[line.find(': bytes'):line.find(':')+7] == ': bytes'):
            num_pings += 1

    return num_pings

def if_locals_up():
    UPPER_LIMIT = 6
    LOWER_LIMIT = 3
    if_up_list = []

    for comp in build_local_list():
        DOMAIN = 'xxxxxx'
        DOMAIN_CONTROLLER = 'xxxxxx'
        
        ping_result, err = Popen_background('ping -n 9 ' + comp)
        result = get_num_pings(ping_result)
    
        if result >= UPPER_LIMIT:
            if_up_list.append(comp + ' Up\n')

        elif result > LOWER_LIMIT and result < UPPER_LIMIT:
            if_up_list.append(comp + ' Shakey\n')

        elif result <= LOWER_LIMIT:
            if_up_list.append(comp + ' Down\n')
            
            nslookup_result, err = Popen_background('nslookup -type=A ' +
                                                    comp + DOMAIN + ' ' +
                                                    DOMAIN_CONTROLLER + DOMAIN)
            
            sonicwall_ip = nslookup_result[nslookup_result.find(comp + DOMAIN) +
                                           len(comp + DOMAIN + '\nAddress:   '):-6] + '1'
            
            sonicwall_ping_result, err = Popen_background('ping -n 9 ' + sonicwall_ip)

            sonicwall_result = get_num_pings(sonicwall_ping_result)

            storenum = ''
            if (comp[-3].isdigit()):
                storenum = comp[-3:]
            else:
                storenum = comp[-2:]
            
            if sonicwall_result >= UPPER_LIMIT:
                if_up_list.append('SonicWall @ ' + storenum + ' Up\n')

            elif sonicwall_result > LOWER_LIMIT and result < UPPER_LIMIT:
                if_up_list.append('SonicWall @ ' + storenum + ' Shakey\n')

            elif sonicwall_result <= LOWER_LIMIT:
                if_up_list.append('SonicWall @ ' + storenum + ' Down\n')
                
    return if_up_list


if __name__ == '__main__':
    ctypes.windll.user32.MessageBoxA(None, str(''.join(str(x) for x in if_locals_up())),
                                     'Store Internet', 'MB_SYSTEMMODAL')
    
