import redis
from datetime import datetime


class LogService():

    def __init__(self, name, host, port=6379):
        self.redis = redis.Redis(host=host, port=port)
        self.stream = "log"
        self.name = name

    def log(self, message):
        self.redis.xadd(self.stream, {"message": "{} | {}".format(self.name, message)})

    def read_log(self):
        response = self.redis.xread({self.stream: 0})
        result = []
        for i in range(len(response[0][1])):
            message_bytes = response[0][1][i][1][b'message']
            message = message_bytes.decode('utf-8')
            time_bytes = response[0][1][i][0]
            # Discard the trailing -0 and the last three digits to convert to seconds from miliseconds
            time = time_bytes.decode('utf-8').split('-')[0][0:-3]
            timestamp = datetime.utcfromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
            result.append({"timestamp": timestamp, "message": message})
        return result
