from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import redis
import pandas as pd


REDIS_HOST = "localhost"
REDIS_PORT = 6379
QUEUE = "activity_detection"

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1)
step = 0

class RequestHandlerHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        global step
        print('you got this http')
        print(self.requestline)
        t = self.requestline.split("?")
        t = t[1].split(" ")
        t = t[0].split("&")
        ax = float(t[0].split("=")[1])
        ay = float(t[1].split("=")[1])
        az = float(t[2].split("=")[1])
        id = int(t[3].split("=")[1])
        tmp = [float(0.0),ax, ay, az]
        with open("/Users/v/PycharmProjects/untitled3/dungyen.csv", 'a') as fd:
            fd.write(str(tmp)+"\n")
        df = pd.DataFrame(tmp)
        df.to_csv("/Users/v/PycharmProjects/untitled3/"+str(id)+".csv", index=False)
        step += 1
        print(step)
        redis_client.lpush(QUEUE, json.dumps({"ax": ax, "ay": ay, "az": az, "step": step}))

    def do_POST(self):
        print("nkt request !!!")
        # if self.path == '/nkt':
        # messagetosend = bytes('{"id": 123, "name": "nkt"}', "utf")
        # self.send_response(200)
        # self.send_header('Content-Type', 'application/json')
        # self.send_header('Content-Length', len(messagetosend))
        # self.end_headers()
        # self.wfile.write(messagetosend)
        return
server_address = ('192.168.43.209', 8888)
httpd = HTTPServer(server_address, RequestHandlerHTTP)
print("start")
httpd.serve_forever()