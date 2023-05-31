# Resume API
Searching far and wide for API projects.

## How to Run

**docker-compose**
```
docker-compose up --build
```

**docker**
```
docker build -t resume-api . && docker run -p 80:5000 -v "$(pwd):/app" resume-api
```

## Documentation

API documentation can be found at [/swagg-ui](http://127.0.0.1/swagger-ui).