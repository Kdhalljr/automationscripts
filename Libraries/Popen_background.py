from subprocess import Popen, PIPE, STARTUPINFO, STARTF_USESHOWWINDOW, SW_HIDE

# Popen_background equires 2 output variables in form of var1, var2 = Popen_background(...)
def Popen_background(input_func):
    
    # Prevents console from appearing on screen during Popen
    startupinfo = None
    startupinfo = STARTUPINFO()
    startupinfo.dwFlags |= STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = SW_HIDE
    
    result = Popen(input_func, stdout=PIPE, stderr=PIPE, startupinfo=startupinfo)
    out, err = result.communicate()
    return out, err
