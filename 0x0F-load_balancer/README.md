# 0x0F-load_balancer

Learning about load balancing using haproxy.

## TASKS

### 0. Double the number of webservers
In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

* Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
    * The name of the custom HTTP header must be X-Served-By
    * The value of the custom HTTP header must be the hostname of the server Nginx is running on
* Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task
    * Ignore SC2154 for 
    

Example:
```
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
```

**Files** - 0-custom_http_response_header