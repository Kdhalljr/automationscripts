from Libraries.computer_lists import build_stores_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt
from os import system

if __name__ == '__main__':
    username, password = user_pass_prompt()

    for comp in build_stores_list():
        arch_results, err = Popen_background('wmic /node:' + comp + ' /user:' + username + ' /password:' + password + ' os get osarchitecture')
        os_results, err = Popen_background('wmic /node:' + comp + ' /user:' + username + ' /password:' + password + ' os get name')
        print comp
        print '-------------------'
        try :
            if 'Microsoft Windows 7' in str(filter(None, os_results.splitlines())[1]):
                if str(filter(None, arch_results.splitlines())[1]).strip() == '32-bit':
                    print str(filter(None, arch_results.splitlines())[1]).strip()
                    mkdir_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec -s \\\\' + comp + ' mkdir C:\\KB4012212\\')
                    print mkdir_results
                    xcopy_results, err = Popen_background('xcopy /-y /d "xxxxxx\\windows6.1-kb4012212-x86_6bb04d3971bb58ae4bac44219e7169812914df3f.msu" \\\\' + comp + '\\c$\\KB4012212\\')
                    print xcopy_results
                    extract_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec -s \\\\' + comp + ' wusa.exe C:\\KB4012212\\windows6.1-kb4012212-x86_6bb04d3971bb58ae4bac44219e7169812914df3f.msu /extract:C:\\KB4012212\\')
                    print extract_results
                    install_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec -s \\\\' + comp + ' dism.exe /online /add-package /PackagePath:C:\\KB4012212\\KB4012212.cab')
                    print install_results
                    print '\n\n'
                elif str(filter(None, arch_results.splitlines())[1]).strip() == '64-bit':
                    print str(filter(None, arch_results.splitlines())[1]).strip()
                    mkdir_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec -s \\\\' + comp + ' mkdir C:\\KB4012212\\')
                    print mkdir_results
                    xcopy_results, err = Popen_background('xcopy /-y /d "\\\\ctc-hq-fs01\\it\\INSTALL\\Microsoft\\KB4012212\\windows6.1-kb4012212-x64_2decefaa02e2058dcd965702509a992d8c4e92b3.msu" \\\\' + comp + '\\c$\\KB4012212\\')
                    print xcopy_results
                    extract_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec -s \\\\' + comp + ' wusa.exe C:\\KB4012212\\windows6.1-kb4012212-x64_2decefaa02e2058dcd965702509a992d8c4e92b3.msu /extract:C:\\KB4012212\\')
                    print extract_results
                    install_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec -s \\\\' + comp + ' dism.exe /online /add-package /PackagePath:C:\\KB4012212\\KB4012212.cab')
                    print install_results
                    print '\n\n'
##            elif ('Microsoft Windows 10' in str(filter(None, os_results.splitlines())[1])) and (str(filter(None, arch_results.splitlines())[1]).strip() == '64-bit'):
##                print str(filter(None, arch_results.splitlines())[1]).strip()
##                xcopy_results, err = Popen_background('xcopy /-y /t /d \\\\ctc-hq-fs01\\it\\INSTALL\\Microsoft\\???\\??? \\\\' + comp + '\\c$\\???\\')
##                print xcopy_results
##                extract_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec -s \\\\' + comp + ' wusa.exe C:\\???\\??? /extract:C:\\???\\')
##                install_results, err = Popen_background('..\\..\\Libraries\\PSTools\\psexec -s \\\\' + comp + ' dism.exe /online /add-package /PackagePath:C:\\???\\???.cab')
##                print '\n\n'
        except IndexError:
            print 'Could not connect to computer' + '\n'

    system('pause')
