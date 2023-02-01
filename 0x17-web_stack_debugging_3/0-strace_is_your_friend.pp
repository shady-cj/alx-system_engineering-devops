# Using puppet to automate errors detected by strace

exec { '/bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php': }
