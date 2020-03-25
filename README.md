# docker_flask

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

### 再起動
```cmd
docker-compose restart
```
もしくは、docker-compose.ymlに
```
restart: always
```
を記述する
