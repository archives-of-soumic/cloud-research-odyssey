package redis.cluster.java.jedisforces;

import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class B918 {
    JedisIO jedisIO;
    JedisCluster jedisClusterMap;   // cz in this problem, we'll use it as a map
    public B918() {
        jedisIO = new JedisIO();
//        jedisClusterMap = jedisIO.getJedisClusterConn(); //
        jedisClusterMap = new JedisCluster(new HostAndPort("127.0.0.1", 8000));

        int n, m, ipLength;
        String serverName, serverIp, command, ip, keyIp;
        Scanner sc = null;
        try {
            String filePath = "./src/main/java/redis/cluster/java/jedisforces/input.txt";
            sc = new Scanner(new File(filePath));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        if(jedisClusterMap != null && sc != null) {
            n = sc.nextInt();
            m = sc.nextInt();

            for(int i=0; i<n; i++) {
                serverName = sc.next().trim(); // trim removes \n, \t, etc string literals
                serverIp = sc.next().trim();
                serverIp = serverIp + ";";
                jedisClusterMap.set(serverIp, serverName);
            }
//            System.err.println("----------------------");
            for(int i=0; i<m; i++) {
                command = sc.next().trim();
                ip = sc.next().trim();
                serverName = jedisClusterMap.get(ip);
                System.out.println(command+" "+ip+" #"+serverName);
            }
        }
        sc.close();
    }
}
