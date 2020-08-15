package redis.java;

import java.util.*;
import redis.clients.jedis.Jedis;

public class RedisController {
    
    public RedisController() {
        Jedis jedis = new Jedis("localhost");
        System.out.println("jedis.ping() = "+jedis.ping());
        
        String key = "fooJava";
        String value = "barJava";

        jedis.set(key, value);

        String output = jedis.get(key);

        System.out.println("jedis.get(key) = "+output);

    }
}