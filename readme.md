## 新建python虚拟环境

```shell
python -m venv venv
```

## 进入虚拟环境

```shell
source ./venv/bin/activate
```

## 导出依赖

```shell
pip freeze > requirements.txt
```

## 安装依赖

```shell
pip install -r requirements.txt

# 使用代理
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 启动uwsgi

```shell
#启动
uwsgi --ini uwsgi/uwsgi.ini

#重启
uwsgi --reload uwsgi/uwsgi.pid

#停止
uwsgi --stop uwsgi/uwsgi.pid
```

## 配置nginx

```conf
server {
    listen       8085;
    server_name  localhost;
    access_log   logs/localhost.log  main;
    error_log    logs/localhost-error.log;

    charset utf-8;

    index  index.html;

    location / {
        include          uwsgi_params;
        uwsgi_pass       unix:/Users/tim/codes/demo-python/flaskProject/uwsgi/uwsgi.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; 
    }
}
```

