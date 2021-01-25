"C:\Users\khall\Documents\Automation Scripts\Libraries\PSTools\psexec" @allpcs.txt -s cmd /c "winrm set winrm/config/service/auth @{Basic="False"}"
pause