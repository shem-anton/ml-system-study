import redis
from datetime import datetime


class LogService():

    def __init__(self, name):
        self.redis = redis.Redis(host='redis', port=6379)
        self.stream = "log"
        self.name = name

    def log(self, message):
        self.redis.xadd(self.stream, {"message": "{} | {}".format(self.name, message)})

    # Return *count* last records with human-readable timestamps
    def read_log(self, count):
        response = self.redis.xread({self.stream: 0}, count = count)
        result = []
        for i in range(count):
            message_bytes = response[0][1][i][1][b'message']
            message = message_bytes.decode('utf-8')
            time_bytes = response[0][1][i][0]
            # Discard the trailing -0 and the last three digits to convert to seconds from miliseconds
            time = time_bytes.decode('utf-8')[0:-5]
            timestamp = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
            result.append({"timestamp": timestamp, "message": message})
        return result
