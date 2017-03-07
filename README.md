# haproxysetup
This is an sample Haproxy setup between two servers

# Install Haproxy by

```shell
sudo add-apt-repository ppa:vbernat/haproxy-1.7
sudo apt-get update
sudo apt-get install haproxy
```

# Run two python servers in two tabs in terminal by 

`python -m server1` in one tab

`python -m server2` in another tab

# Check Python servers by

`http://127.0.0.1:8001` and `http://127.0.0.1:8002/`

# Now copy these code in  haproxy.cfg  `sudo nano /etc/haproxy/haproxy.cfg`
{%highlight code%}
frontend localnodes
    bind 127.0.0.1:9000
    mode http
    default_backend nodes

backend nodes
    mode http
    balance roundrobin
    option forwardfor
    server web01 127.0.0.1:8001 check
    server web02 127.0.0.1:8002 check


listen stats
    bind 127.0.0.1:1936
    mode http
    stats enable
    stats uri /
    stats hide-version
    stats auth test:test
{% endhighlight%}


# Now restart HAProxy by
`sudo service haproxy restart`

# Now open browser and hit `http://127.0.0.1:9000`


# Check the stats page by `http://127.0.0.1:1936`

`username: test`
`password: test`

Displays the detailed stats of all servers.

