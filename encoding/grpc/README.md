### Simple run

```
docker-compose up
```


#### To compile proto for M1

```
brew install protobuf@3                                                                                                   
brew link --overwrite protobuf@3
brew install protoc-gen-grpc-web  
```

#### To create & run proxy

```
docker build -t grpc_proxy ./proxy
docker run -d -p 9090:9090 grpc_proxy
```

### To run services

```
python3 backend/main.py
npm start 
```