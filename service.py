import sys
import servicemanager
import win32event
import win32service
import win32serviceutil

import os,sys
import os.path as op

config_name = 'myapp.cfg'
basename = os.path.splitext(os.path.basename(__file__))[0]

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    running_mode = 'Frozen/executable'
else:
    try:
        app_full_path = os.path.realpath(__file__)
        application_path = os.path.dirname(app_full_path)
        running_mode = "Non-interactive (e.g. 'python " + os.path.basename(__file__) + "')"
    except NameError:
        application_path = os.getcwd()
        running_mode = 'Interactive'

config_full_path = os.path.join(application_path, config_name)

def mainApp():
    print('----------------------------------------')
    print('file:',__file__)
    print('arguments:',sys.argv)
    print('basename:',basename)
    print('working location:',os.getcwd())
    print('Running mode:', running_mode)
    print('  Appliction path  :', application_path)
    print('  Config full path :', config_full_path)

def service():
    import time
    with open(os.path.realpath(f"{application_path}\{basename}.log"), "a") as file:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")
        print(f"{current_time}")
    time.sleep(1)  # Wait for 6 seconds

class BookScraperService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'samplepywinservice'
    _svc_display_name_ = 'samplepywinservice'
    _svc_description_ = 'Sample application for windows service'
    _exe_args_ = 'service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.event = win32event.CreateEvent(None, 0, 0, None)
        self.is_running = True

    def GetAcceptedControls(self):
        result = win32serviceutil.ServiceFramework.GetAcceptedControls(self)
        result |= win32service.SERVICE_ACCEPT_PRESHUTDOWN
        return result

    def SvcDoRun(self):
        self.is_running = True
        while self.is_running:
            service()
        #     import time
        #     with open(os.path.realpath(f"{application_path}\service.log"), "a") as file:
        #         current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        #         file.write(f"{current_time}\n")
        #         print(f"{current_time}")
        #     time.sleep(6)  # Wait for 6 seconds

    def SvcStop(self):
        self.is_running = False
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.event)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        mainApp()
    elif len(sys.argv) == 2 and sys.argv[1] == 'service':
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(BookScraperService)
        servicemanager.StartServiceCtrlDispatcher()
    elif len(sys.argv) >= 2 and ['install','update','remove','start','stop','restart'].count(sys.argv[1]):
        win32serviceutil.HandleCommandLine(BookScraperService)
    else:
        print("Invalid Parameter")




# pyinstaller --onefile --hidden-import win32timezone --hidden-import servicemanager --icon application.ico --add-data application.ico --splash splash.png --version-file version.txt service.py

# https://oxylabs.io/blog/python-script-service-guide
# https://www.youtube.com/watch?v=pLqtenLVKsg