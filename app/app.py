from flask import Flask, request, render_template
import rabbit
import redis 

app = Flask(__name__)
default_key = '1'

cache = redis.StrictRedis(host='localhost', port=6379, db=0)
cache.set(default_key, "one")

@app.route('/', methods=['GET', 'POST'])
def mainpage():

    key = default_key
    if 'key' in request.form:
        key = request.form['key']

    if request.method == 'POST' and request.form['submit'] == 'save':
        try:
            cache.set(key, request.form['cache_value'])
            print("key : %r saved in cache" % key)
            print("value : %r saved in cache" % request.form['cache_value'])
        except:
            print('could not connect with Redis server')
            return render_template('index.html')

        pub = None
        try:
            pub = rabbit.Publisher()
            if pub.publish(cache.get(key).decode('utf-8')):
                print('Message was published')
            else:
                print('Message was returned')
        except:
            print('Message was returned')
        finally:
            # Destroy references
            del pub

    cache_value = None
    if cache and key in cache:
        cache_value = cache.get(key).decode('utf-8')

    return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#def rabbitconnect():

    # install rabbit docker
    # docker run -d --hostname csi-rabbit --name csi-rabbit \
    # -e RABBITMQ_DEFAULT_VHOST=reporting_vhost \
    # -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin \
    # -p 4369:4369 -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq:3.6-alpine
    # docker exec csi-rabbit rabbitmq-plugins enable rabbitmq_management