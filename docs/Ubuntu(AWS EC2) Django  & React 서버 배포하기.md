# Ubuntu(AWS EC2) Django / React 서버 배포하기

Ubuntu 접속 후 Django / React 서버 배포를 위한 세팅 작업

---

## 서버 환경 설정

1. locale 설정

   ```bash
   sudo vi /etc/default/locale
   ```

   다음을 추가한 뒤 서버에 재접속한다.

   ```b
   LC_CTYPE="en_US.UTF-8"
   LC_ALL="en_US.UTF-8"
   LANG="en_US.UTF-8"
   ```

2. 패키지 정보 업데이트

   ```bash
   sudo apt-get update
   ```

3. 패키지 의존성 검사 및 업그레이드

   ```bash
   sudo apt-get dist-upgrade
   ```

4. Python 패키지 매니저 설치

   ```bash
   sudo apt-get install python-pip
   sudo pip install --upgrade pip
   ```

5. zsh 설치

   ```bash
   sudo apt-get install zsh
   ```

6. oh my zsh 설치

   ```bash
   sudo curl -L http://install.ohmyz.sh | sh
   ```

7. 기본 쉘을 zsh로 변경한 뒤 재접속 (chsh 다음에 유저명을 입력해주어야한다.)

   ```bash
   sudo chsh ubuntu -s /usr/bin/zsh
   ```



## Python 환경 설정

- pyenv 설치 및 환경 설정

  ```bash
  sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev
  ```

  ```bash
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
  ```

  ~/.zshrc` 의 pyenv 환경변수 설정은 아래와 같이 입력해준다.

  ```
  export PATH="/home/ubuntu/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  ```

- Django 프로젝트 설정

  ```bash
  cd /srv/
  ```

  `/srv/` 폴더로 이동해서 Django 프로젝트를 clone 받아준다.

  ```bash
  sudo chown -R ubuntu:ubuntu /srv/
  ```

  `srv` 폴더 소유자를 `ubuntu` 로 변경해준다.

- Python 설치

  pyenv를 통해서 Django 프로젝트 에 맞는 Python 버전을 설치한다.

  ```bash
  pyenv install 3.7.4
  ```

  ```bash
  pyenv virtualenv 3.7.4 project-env
  ```

- Pillow를 위한 Python 라이브러리 설치

  ```bash
  sudo apt-get install python-dev python-setuptools
  ```

* virtualenv 설정

  프로젝트 폴더에서 virtualenv 설정 해준다.

  ```
  pyenv local project-env
  ```

* Django requirements 설치

  ```bash
  sudo pip install -r reqirements.txt 
  ```



## WSGI 설정

* uWSGI 설치

  배포에 사용할 새로운 유저를 `deploy` 라는 이름으로 생성해준다.
  보안을 위해 각 기능 별 유저를 설정해주는 것이 좋다.

  ```bash
  sudo adduser deploy
  ```

  그런 다음, uWSGI를 설치할 별도의 Python 가상환경을 생성해준다.

  ```bash
  pyenv virtualenv 3.7.4 uwsgi-env
  ```

  이 가상환경을 지금 현재의 가상 컴퓨터 셸에만 일시적으로 적용하도록 설정해준다.
  서버 전체에서 하나의 uwsgi를 사용하게 하기 위함이다.

  ```bash
  pyenv shell uwsgi-env
  ```

  이제 가상환경에 `uwsgi` 를 설치한다.

  ```bash
  pip install uwsgi
  ```

* ini file 설정

  Django 프로젝트 폴더에 `.config` 라는 폴더를 하나 새로 생성하고 그 안에 다시 `uwsgi` 폴더를 생성한다.
  `uwsgi` 폴더 안에 `mysite.ini` 파일을 만들어 준다.

  ```bash
  EC2_Deploy_Project
  ├── .config
  │   └── uwsgi
  │       └── mysite.ini
  ├── .git
  ├── .gitignore
  ├── mysite
  └── requirements.txt
  ```

  mysite.ini를 열고 다음과 같이 입력한다.

  ```ini
  [uwsgi]
  project = <project_name>
  base = <project_base_directory>
  chdir = %(base)/%(project)
  module = %(project).wsgi:application
  home = /home/ubuntu/.pyenv/versions/%(project)
  
  # env variables
  env=<SOME_VAR>=foobar
  
  uid = deploy
  gid = deploy
  
  socket = /tmp/%(project).sock
  chmod-socket = 666
  chown-socket = deploy:deploy
  
  enable-threads = true
  master = true
  processes = 4
  vacuum = true
  pidfile = /tmp/%(project).pid
  logto = /var/log/uwsgi/%(project)/@(exec://date +%%Y-%%m-%%d).log
  log-reopen = true
  ```

  uWSGI를 실행하기 전에 `mysite.ini` 파일에 설정해주었던 `logto` 옵션의 디렉토리를 직접 생성해주어야 한다.

  ```bash
  sudo mkdir -p /var/log/uwsgi/<project_name>
  ```

  uWSGI 실행

  ```bash
  sudo /home/ubuntu/.pyenv/versions/uwsgi-env/bin/uwsgi -i /srv/EC2_Deploy_Project/.config/uwsgi/mysite.ini 
  ```

  uWSGI 백그라운드 실행

  리눅스에서 관리하는 `service` 파일을 만들어 서버가 실행될 때 자동으로 uWSGI를 백그라운드에 실행시켜주도록 하자.

   `/장고 프로젝트 폴더/.config/uwsgi/` 에 `uwsgi.service` 파일을 생성한다.

  ```
  .config
  └── uwsgi
      ├── uwsgi.service
      └── mysite.ini
  ```

  `uwsgi.service` 파일안에 아래와 같이 작성한다.

  ```
  [Unit]
  Description=uWSGI service
  After=syslog.target
  
  [Service]
  ExecStart=/home/ubuntu/.pyenv/versions/uwsgi-env/bin/uwsgi -i /srv/ec2_deploy_project/.config/uwsgi/mysite.ini
  
  Restart=always
  KillSignal=SIGQUIT
  Type=notify
  StandardError=syslog
  NotifyAccess=all
  
  [Install]
  WantedBy=multi-user.target
  ```

   `uwsgi.service` 파일을 `/etc/systemd/system/` 에 하드링크를 걸어준다.

  ```
  sudo ln -f /srv/EC2_Deploy_Project/.config/uwsgi/uwsgi.service /etc/systemd/system/uwsgi.service
  ```

  **nginx 설정 후에 실행할 것임!**

  

  ## Nginx 설정

  * Nginx 설치

    ```bash
    # PPA 추가를 위한 필요 패키지
    sudo apt-get install software-properties-common software-properties-common
    # nginx 안정화 최신버전 PPA 추가
    sudo add-apt-repository ppa:nginx/stable
    # PPA 저장소 업데이트
    sudo apt-get update
    # nginx 설치
    sudo apt-get install nginx
    ```

    ```bash
    nginx -v
    ```

  * 유저 설정

    배포에 관한 작업은 `deploy` 유저가 담당하므로 `Nginx` 의 유저를 `deploy` 로 바꿔준다.
    `Nginx` 관련 설정은 `/etc/nginx/nginx.conf` 에서 관리한다.

    ```
    sudo vi /etc/nginx/nginx.conf
    ```

    파일의 첫 줄 `user www-data;` 를 `user deploy;` 로 수정해준다.

    ```
    # nginx.conf
    
    user deploy;
    ```
    
  * Nginx 설정 파일 생성 및 연결
    uWSGI 설정을 저장했던 `.config` 폴더에 `nginx` 폴더를 새로 만들고 그 아래에 `mysite.conf` 파일을 생성한다.
  
    ```
    .config
    ├── nginx
    │   └── mysite.conf
    └── uwsgi
        └── mysite.ini
    ```
  
    `mysite.conf` 파일을 열어 아래와 같이 작성한다.

    ```
  server {
        listen 80;
        server_name *.compute.amazonaws.com;
        charset utf-8;
      client_max_body_size 128M;
    
      location / {
            uwsgi_pass  unix:///tmp/mysite.sock;
            include     uwsgi_params;
        }
    }
    ```
  
    Django 프로젝트 폴더 내의 `mysite.conf` 파일을 `/etc/nginx/sites-available/` 경로에 복사해준다.
  
    ```bash
    sudo cp -f /srv/EC2_Deploy_Project/.config/nginx/mysite.conf /etc/nginx/sites-available/mysite.conf
    ```
  
    이제 다음 명령을 입력하여 `sites-available` 에 있는 설정파일을 `sites-enabled` 폴더에 링크해준다.
  
    ```bash
    sudo ln -sf /etc/nginx/sites-available/mysite.conf /etc/nginx/sites-enabled/mysite.conf
    ```
  
    `sites-enabled` 폴더의 `default` 링크는 삭제해준다.
  
    ```bash
    sudo rm /etc/nginx/sites-enabled/default
    ```
  
    파일을 연결해준 뒤 아래 명령을 실행해서 데몬을 리로드 해준다.
  
    ```bash
    sudo systemctl daemon-reload
    ```
  
    그 다음 아래 명령어로 uwsgi 데몬을 활성화 해준다.
  
    ```bash
    sudo systemctl enable uwsgi
    ```
  
    

## Static 설정



## React 설정

* Node 설치

  ```bash
  curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
  sudo apt-get install -y nodejs
  ```

* Yarn 설치

  ```bash
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
  sudo apt-get update && sudo apt-get install yarn
  ```

* frontend depencies 설치 및 빌드

  ```bash
  yarn
  yarn build
  ```

* Nginx 설정

  frontend 디렉토리에도 동일하게 .config 폴더를 만들어주고 `frontend.conf` 파일을 작성해준다.

  ```
  sudo mkdir -p .config/nginx/
  sudo vi .config/nginx/frontend.conf
  ```

   `frontend.conf` 파일을 `/etc/nginx/sites-available/` 경로에 복사해준다.

  ```bash
  sudo cp -f /srv/project/frontend/.config/nginx/frontend.conf /etc/nginx/sites-available/frontend.conf
  ```

  이제 다음 명령을 입력하여 `sites-available` 에 있는 설정파일을 `sites-enabled` 폴더에 링크해준다.

  ```bash
  sudo ln -sf /etc/nginx/sites-available/frontend.conf /etc/nginx/sites-enabled/frontend.conf
  ```

  파일을 연결해준 뒤 아래 명령을 실행해서 데몬을 리로드 해준다.

  ```bash
  sudo systemctl daemon-reload
  ```

  

