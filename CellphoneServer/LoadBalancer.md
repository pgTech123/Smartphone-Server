Overview
----
The load balancer is the system that will dispatch requests among the smartphones available.
Your load balancer can either run on a cellphone; ideally the most powerful phone you have access to as any failure will cause the whole system to crash or you can run it on a small computer; such as the Raspberry Pi. The advantage to run it on a Raspberry Pi for example is that we can have a wired conection to the internet, which should be more efficient when a lot of requests are received. The steps to intall the load balancer on a smartphone and a Raspberry Pi is the same.

1. If you use a smartphone, [install Linux on the phone](TODO)

2. Find the IP of the device. You can do that by disconnecting the device and running the command
```bash
nmap -sP 192.168.0.*    #Adapt the beginning of the IP to your local network
```
Connect the device and run the same command again. You should see one more host. Note the IP address. We will use it later.

3. Connect to the device via ssh
```bash
ssh <username>@<ip> # Replace <username> by your username and <ip> by the ip address found in step 2.
```
You might be asked to enter a password. If so, enter your password.
You should now be connected. You should see something like "username@computer_name ~ $" in your terminal.

4. Install NGINX on the remote device
```bash
sudo apt-get install nginx-full
```

5. It's now time to configure NGINX to act as a load balancer. At this point we will need the IP address of all the smartphones endpoints. [Setting up the endpoint](TODO) should be done now if it's not already done. To know the IP address of a phone, open the app "Linux Deploy". If the system is not started yet, click "Start". You should then see the IP address in the top of the app.

In the file /etc/nginx/nginx.conf, and add the following lines between the http braces:
```json
#http {


    upstream backend {
        server ipsrv1:80;
        server ipsrv2:80;
        server ipsrv3:80;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://backend;
        }
    }
# ...
# Other stuff
# ...
#}
```

6. Restart the server
```bash
sudo service nginx restart
```
If you get an error saying that port 80 is already in use, run:
```bash
sudo fuser -k 80/tcp
```

7. Make sure the server is started on the smartphone endpoints. You can test that by typing the IP in your web browser. You should see the default web page appear. 

8. Access the IP of the load balancer. You should see the web page from stored on the smartphone.