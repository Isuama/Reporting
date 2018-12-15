import pika
import traceback
import os

# create global variable
hostname = os.getenv('hostname','localhost')
port = os.getenv('port',5672)
username = os.getenv('username','admin')
password = os.getenv('password','admin')
vhost = os.getenv('vhost','reporting_vhost')
exchange = os.getenv('exchange','reporting')
queue = os.getenv('queue','reportingFrameworkQueue')
autoAck = os.getenv('autoAck','False')
routeKey = os.getenv('routeKey','python')
ssl = os.getenv('ssl',False)

class Connection():

    def _create_connection(self):
        try:
            credentials = pika.PlainCredentials(username, password)
            parameters = pika.ConnectionParameters(hostname,port, vhost, credentials, ssl=ssl)
            return pika.BlockingConnection(parameters)
        except Exception as e:
            print(repr(e))
            traceback.print_exc()
            raise e
        finally:
            del credentials, parameters

class Publisher:

    def publish(self, message):
        try:
            rabConn = Connection()
            connection = rabConn._create_connection()
            channel = connection.channel()
            channel.exchange_declare(exchange=exchange, passive=True)
            channel.basic_publish(exchange=exchange,
                                      routing_key=routeKey,
                                      body=message)
    
            print(" [x] Sent message %r" % message)
        except Exception as e:
            print(repr(e))
            traceback.print_exc()
            raise e
        finally:
            if connection:
                connection.close()
            del rabConn, connection, channel

class Subscriber:
    
    def subscribe(self):
        print("hi there")