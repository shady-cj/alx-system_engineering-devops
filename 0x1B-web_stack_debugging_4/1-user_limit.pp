# increasing the limit of files that can be opened for a restricted user

exec { "/bin/sed -i '/holberton hard/s/5/10000/g' /etc/security/limits.conf": }

exec { "/bin/sed -i '/holberton soft/s/4/9000/g' /etc/security/limits.conf": }
