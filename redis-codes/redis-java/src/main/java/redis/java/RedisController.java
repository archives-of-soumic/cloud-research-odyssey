package redis.java;

import java.util.*;

import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisCluster;

public class RedisController {
    
    public RedisController() {
//        Jedis jedis = new Jedis("localhost");
        JedisCluster jedis = new JedisCluster(new HostAndPort("127.0.0.1", 8000));

//        System.out.println("jedis.ping() = "+jedis.ping());
        
        String key = "fooJava";
        String value = "barJava";

        jedis.set(key, value);

        String output = jedis.get(key);

        System.out.println("jedis.get(key) = "+output);

    }
}