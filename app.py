from flask import Flask
import redis

app = Flask(__name__)

# Подключение к Redis
r = redis.Redis(host='redis', port=6379)

@app.route('/count')
def count():
    # Увеличиваем счетчик посещений в Redis
    visits = r.incr('counter')
    return f'Количество посещений: {visits}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
