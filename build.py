import os
import subprocess
import sys
import platform
import shutil

os_type = platform.system()
if os_type not in ['Windows', 'Darwin', 'Linux']:
    print(f'The current operating system ({os_type}) is not supported!')
    exit(1)
if len(sys.argv) == 1:
    env_path = '%USERPROFILE%\\ltrans_env' if os_type == 'Windows' else '~/ltrans_env'
if len(sys.argv) == 2:
    env_path = os.path.join(sys.argv[1], 'ltrans_env')
if len(sys.argv) >= 3:
    print('Usage: python build.py [env_path]')
    exit(1)

print('Creating a virtual environment ...')
python_name = sys.executable[sys.executable.rfind('python'):]
if not os.path.exists(env_path):
    subprocess.run(f'{python_name} -m venv {env_path}', check=True, shell=True)

print('Installing dependencies ...')
scripts_path = f'{env_path}\\Scripts\\' if os_type == 'Windows' else f'{env_path}/bin/'
url = 'https://mirrors.ustc.edu.cn/pypi/simple'
subprocess.run(f"{scripts_path}{python_name} -m pip install -U -i {url} pip",
               check=True,
               shell=True)
subprocess.run(f'{scripts_path}pip3 install -i {url} wheel', check=True, shell=True)
subprocess.run(f'{scripts_path}pip3 install -i {url} -r requirements.txt', check=True, shell=True)

print('Packing ...')
subprocess.run(f'{scripts_path}pyinstaller -y --noconsole main.py', check=True, shell=True)

print('Copying configuration file ...')
shutil.copy('config.yml', os.path.join('dist', 'main', 'config.yml'))

print('Done!')
