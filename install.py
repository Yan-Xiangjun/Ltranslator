import os
import sys
import platform

os_type = platform.system()
if os_type not in ['Windows', 'Darwin', 'Linux']:
    print(f'不支持当前操作系统：{os_type}')
    exit(1)

print('创建虚拟环境……')
python_path = sys.executable
if not os.path.exists('ltrans_env'):
    os.system(f'{python_path} -m venv ltrans_env')

print('安装依赖库……')
scripts_path = '.\\ltrans_env\\Scripts\\' if os_type == 'Windows' else './ltrans_env/bin/'
os.system(f"{scripts_path}{python_path[python_path.rfind('python'):]} -m pip install -U -i https://mirrors.ustc.edu.cn/pypi/simple pip")
os.system(f'{scripts_path}pip3 install -i https://mirrors.ustc.edu.cn/pypi/simple wheel')
os.system(f'{scripts_path}pip3 install -i https://mirrors.ustc.edu.cn/pypi/simple openai pyside2 pynput pyperclip pyyaml')

print('创建启动脚本……')
this_dir = os.path.dirname(os.path.realpath(__file__))
if os_type == 'Windows':
    with open('Ltranslator启动器.cmd', 'w') as launcher_file:
        launcher_file.write(f'{this_dir}\\{scripts_path}python.exe {this_dir}\\main.py')
elif os_type == 'Darwin':
    with open(f'Ltranslator启动器.command', 'w') as launcher_file:
        launcher_file.write('#!/bin/bash\n'
                            'set -x\n'
                            f'sudo {this_dir}/{scripts_path}python3 {this_dir}/main.py')
    os.system(f'chmod +x Ltranslator启动器.command')
else:  # Linux
    with open('Ltranslator启动器.sh', 'w') as launcher_file:
        launcher_file.write('#!/bin/bash\n'
                            'set -x\n'
                            f'{this_dir}/{scripts_path}python3 {this_dir}/main.py')
    os.system('chmod +x Ltranslator启动器.sh')

print('完成！')
