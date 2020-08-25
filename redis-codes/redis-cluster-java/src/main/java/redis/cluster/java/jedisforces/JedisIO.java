package redis.cluster.java.jedisforces;

import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;

import java.io.IOException;

/**
 * For some reason it is not working :/
 * */
public class JedisIO {
    /** Konsts */
    public static final String TAG = JedisIO.class.getSimpleName();

    /** Variables */
    JedisCluster jedisClusterConn = null;

    /** Constructors */
    public JedisIO() {

    }

    /** Private methods */
    private void initJedisClusterConn() {
        try  {
            jedisClusterConn = new JedisCluster(new HostAndPort("127.0.0.1", 8000));
            // use the jedisCluster resource as if it was a normal Jedis resource
        } catch (Exception x) {
            System.out.println("Exception -> "+x.getMessage());
        }
    }

    /** Public apis */
    public JedisCluster getJedisClusterConn() { return jedisClusterConn; }

}
