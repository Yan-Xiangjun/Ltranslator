import os
import platform

os_type = platform.system()
if os_type not in ['Windows', 'Darwin', 'Linux']:
    print(f'不支持当前操作系统：{os_type}')
    exit(1)

print('创建虚拟环境……')
if not os.path.exists('ltrans_env'):
    os.system(f'python3 -m venv ltrans_env')

print('安装依赖库……')
pip_executable = '.\\ltrans_env\\Scripts\\pip3' if os_type == 'Windows' else './ltrans_env/bin/pip3'
os.system(f'{pip_executable} install -i https://mirrors.ustc.edu.cn/pypi/simple wheel')
os.system(f'{pip_executable} install -i https://mirrors.ustc.edu.cn/pypi/simple openai pyside2 pynput pyperclip pyyaml')

print('创建启动脚本……')
this_dir = os.path.dirname(os.path.realpath(__file__))
if os_type == 'Windows':
    with open('Ltranslator启动器.cmd', 'w') as launcher_file:
        launcher_file.write(f'{this_dir}\\ltrans_env\\Scripts\\python3 {this_dir}\\main.py')
elif os_type == 'Darwin':
    with open(f'Ltranslator启动器.command', 'w') as launcher_file:
        launcher_file.write(f'#!/bin/bash\nset -x\nsudo {this_dir}/ltrans_env/bin/python3 {this_dir}/main.py')
    os.system(f'chmod +x Ltranslator启动器.command')
else:  # Linux
    with open('Ltranslator启动器.sh', 'w') as launcher_file:
        launcher_file.write(f'#!/bin/bash\nset -x\n{this_dir}/ltrans_env/bin/python3 {this_dir}/main.py')
    os.system('chmod +x Ltranslator启动器.sh')

print('完成！')
