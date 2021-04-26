import os
import threading


# create and run web developer blog


web_developer_blog = 'https://github.com/AlexanderPort/web_developer_blog.git'
frontend = 'https://github.com/AlexanderPort/frontend.git'


class CMDThread(threading.Thread):
    def __init__(self, command):
        threading.Thread.__init__(self)
        self.command = command

    def run(self) -> None:
        os.system(self.command)


if __name__ == '__main__':
    if not os.path.exists('./web_developer_blog'):
        print('cloning source code from github repositories...')
        os.system(f'git clone {web_developer_blog}')
        os.system(f'cd web_developer_blog && git clone {frontend}')
        print('installing necessary js libraries...')
        print('installing react-router-dom...')
        os.system('cd web_developer_blog/frontend && npm install react-router-dom --save')
        print('installing material ui...')
        os.system('cd web_developer_blog/frontend && npm install @material-ui/core --save')
        os.system('cd web_developer_blog/frontend && npm install @material-ui/icons --save')
        print('installing froala editor...')
        os.system('cd web_developer_blog/frontend && npm install react-froala-wysiwyg --save')
        print('installing react js...')
        os.system('cd web_developer_blog/frontend && npm install react-modules babel-template --save')
        print('installing necessary python libraries...')
        os.system('pip install django djangorestframework django-cors-headers')
    python = input('choose python command: python / python3 ')
    print('running web site...')
    CMDThread(f'cd web_developer_blog && {python} manage.py runserver').start()
    CMDThread(f'cd web_developer_blog/frontend && npm start').start()
