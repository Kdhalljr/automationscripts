from Libraries.computer_lists import build_mgr_list
from Libraries.Popen_background import Popen_background

if __name__ == "__main__":

    output_file = open('copy_results.txt', 'w+')
    for comp in build_mgr_list():
        copy_result, err = Popen_background('xcopy /k /i /y "Troubleshooting Store Internet.pdf" \\\\' + comp + '\c$\Users\Public\Desktop')
        output_file.write(comp + ' = ' + copy_result + '\n')
        print comp + ' = ' + copy_result

    output_file.close()
