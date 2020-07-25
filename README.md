# docker_flask
docker上でflaskによる簡単なwebアプリケーションのデモ  
<img width="380" alt="screenshot20200725" src="https://user-images.githubusercontent.com/31844364/88418122-09fae600-ce1e-11ea-8649-ba799f971fb2.png">  
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
### 初期化
```cmd
docker-compose down
```
イメージ、コンテナ、ボリューム、ネットワークをすべて削除する。
