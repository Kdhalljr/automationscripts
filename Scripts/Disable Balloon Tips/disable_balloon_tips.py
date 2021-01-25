from Libraries.computer_lists import build_stores_list
from Libraries.Popen_background import Popen_background
from Libraries.user_pass_prompt import user_pass_prompt

if __name__ == "__main__":
    username, password = user_pass_prompt()

    output_file = open('disable_balloon_tips.txt', 'w+')
    for comp in build_stores_list():
        disable_results, err = Popen_background('winrs -r:"' + comp + '" -u:' + username + ' -p:' + password + ' reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v EnableBalloonTips /t REG_DWORD /d 0')
        output_file.write(comp + '\n----------------\n' + disable_results + '\n\n')
        print comp + '\n----------------\n' + disable_results + '\n\n'
