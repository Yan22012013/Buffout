import subprocess
import urllib.request
import os
 
def install_software(package):
    """
    Function to install a software package.
    """
    try:
        if package == 'python':
            url = 'https://www.python.org/ftp/python/3.13.0/python-3.13.0b2.exe'
            installer_path = 'установка python'
            urllib.request.urlretrieve(url, installer_path)
            subprocess.check_call([installer_path, '-ms'])
            os.remove(installer_path)
        else:
            subprocess.check_call(['pip', 'install', package])
        print("успешно установлено {package}")
    except subprocess.CalledProcessError:
        print("не удалось установить {package}")
 
 
software_packages = ['numpy', 'pandas', 'matplotlib', 'python']
 
for package in software_packages:
    if package == "python":
        install_software(package)