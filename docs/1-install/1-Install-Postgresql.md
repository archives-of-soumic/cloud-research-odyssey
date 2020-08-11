# Installing Postgresql
The course will be using this database. Hence the first thing to do is install the database. I am 
currently using `Debian 10 Testing` (actually it's `Linux Mint Debian Edition` alias `LMDE4`, and I tweaked the software sources file by changing `stable` into `testing`, so it's really `Debian 10 Testing` with a different 'skin') as my main os. In production however, one should use a stable os.

Follow my instructions precisely:
1. Go to [postgresql download page](https://www.postgresql.org/download/) and select your distro (debian for my case). Then follow the instructions. You can add the repository, or directly download 
from debian's repository.
```
$ sudo apt-get install postgresql
```
***Warning***: If you add postgresql repository, you may encounter an error. To fix it, go to `/etc/apt/sources.list.d`, and then open the `pgdg.list` as root. Then you'll see: `deb http://apt.postgresql.org/pub/repos/apt <DISTRO>-pgdg main`. Change the distro to `buster` (it is the official name of debian 10).
So in my case, I saw `deb http://apt.postgresql.org/pub/repos/apt debbie-pgdg main` and so I changed it into `deb http://apt.postgresql.org/pub/repos/apt buster-pgdg main`.

