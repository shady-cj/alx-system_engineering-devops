# configuration to improve the request handling of nginx

exec { 'ulimit':
        command => "/bin/sed -i 's/ULIMIT.*/ULIMIT=\"-n 1024\"/g' /etc/default/nginx"
}

service { 'nginx':
        ensure    => running,
        subscribe => Exec['ulimit']
}
