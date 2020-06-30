from flask import Flask
import docker


app     = Flask(__name__)
client  = docker.from_env()


@app.route('/')
def hello_from_docker():
    return client.containers.run('hello-world').decode() 


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
