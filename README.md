# docker_flask
docker上でflaskによる簡単なwebアプリケーションのデモ  
以下のキーワードの技術を含んでいる
- Docker
- Python
- Flask
- Flask-Bootstrap
- HTML
- ~~CSS~~
- jinja2

### 起動


```cmd
docker-compose up -d
```
up : 起動する  
-d : バックグラウンドで起動する


Dockerfileを更新した場合
```cmd
docker-compose up -d --build
```

### 停止
```cmd
docker-compose stop
```

### コンテナの中で作業をする
```cmd
docker-compose exec flask bash
```
コマンド中のflaskは、docker-compose.ymlで指定したコンテナ名
### 再起動
```cmd
docker-compose restart
```
もしくは、docker-compose.ymlに
```
restart: always
```
を記述する
