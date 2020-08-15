# Tutorial 2: Redis

## Installation
On Debian, we can directly install redis:
```
$ sudo apt install redis
```
However, this is an old version(at the time of writing, it is version 5).
So we can download the redis source code from scratch, extract it. Then:
```
$ cd redis-6.0.6
$ make             # <-- this line installs from src
```
At the end you might be prompted to test the installation. But I had to install a package 1st:
```
sudo apt-get install -y tcl  # <-- tcl version > 8.5 required
```

Once installed, run:
```
make test
```
If at the end you see all ok, then redis has been installed successfully.

We can test our installation:
```
soumic@hp-laptop:~/Applications/redis-6.0.6$ src/redis-server 
```
On a second terminal, run:
```
soumic@hp-laptop:~/Applications/redis-6.0.6$ src/redis-cli

127.0.0.1:6379> set foo bar
OK
127.0.0.1:6379> get foo
"bar"
127.0.0.1:6379> 
```

## Update $PATH
Since I installed Redis from source, everytime I want to use redis, I have to manually type the absolute path of redis. This is annoying. To resolve this, I updated my `$PATH` variable by adding the installation directory location. Open `.bashrc` file and add these 2 lines
```
# Redis
export REDIS_HOME="/home/soumic/Applications/redis-6.0.6"
export PATH=$REDIS_HOME/src:$PATH 
```
Remember to replace the path with that of yours.
So now I can use redis from the terminal like this:

```
soumic@hp-laptop:~$ redis-server
```