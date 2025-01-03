import os
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
    os.system(f'{python_name} -m venv {env_path}')

print('Installing dependencies ...')
scripts_path = f'{env_path}\\Scripts\\' if os_type == 'Windows' else f'{env_path}/bin/'
url = 'https://mirrors.ustc.edu.cn/pypi/simple'
os.system(f"{scripts_path}{python_name} -m pip install -U -i {url} pip")
os.system(f'{scripts_path}pip3 install -i {url} wheel')
os.system(f'{scripts_path}pip3 install -i {url} -r requirements.txt')

print('Packing ...')
os.system(f'{scripts_path}pyinstaller -y --noconsole main.py')

print('Copying configuration file ...')
shutil.copy('config.yml', os.path.join('dist', 'main', 'config.yml'))

print('Done!')
