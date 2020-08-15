import redis

''' 
warning: DONOT make any folder name  = `redis`, otherwise python will load `your redis folder` instead of the `actual redis folder`
'''
'''
@brief: a hello world kinda demo
    1. we connect to redis
    2. set a key - value pair (foo, bar)
    3. get the value using key
'''
def hello_redis():
    r = redis.Redis(); 
    #  Redis(host = '127.0.0.1',post = '6379',password = ''); // looks like this constructor is depricated
    r.set('foo', 'bar');

    key = 'foo'
    value_bytes = r.get(key);
    value_str = value_bytes.decode("utf-8");
    print(value_str);
    pass;

if __name__ == "__main__":
    hello_redis();
    pass;