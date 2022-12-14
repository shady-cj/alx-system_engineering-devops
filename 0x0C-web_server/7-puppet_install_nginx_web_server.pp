# using puppet to install and configure nginx


package { 'nginx':
	ensure => installed,
	before => Service['nginx']
}

service { 'nginx':
	ensure => running,
	require => Package['nginx'],
	subscribe => File['/etc/nginx/sites-available/default']
}


File { '/var/www/html/index.html':
	ensure => file,
	content => 'Hello World!'
}

File { '/var/www/html/404.html':
	ensure => file,
	content => "Ceci n'est pas une page"
}

@content = @(CONTENT)
	server {
        	listen 80 default_server;
        	listen [::]:80 default_server;
        	root /var/www/html;
        	index index.html index.htm index.nginx-debian.html;

        	location /redirect_me {
                	return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        	}

        	error_page 404  /404.html;

	}
	| CONTENT

File { '/etc/nginx/sites-available/default':
	ensure => present,
	content => $content,
	notify => Service['nginx']
}
