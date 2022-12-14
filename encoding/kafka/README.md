## Simple run

```
docker-compose up
```

## To run consumer

```
python3 main.py
```

## To run producer

```
uvicorn main:app --host 0.0.0.0 --port 8080
```