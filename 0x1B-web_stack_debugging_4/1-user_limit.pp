# increasing the limit of files that can be opened for a restricted user

exec { "sed -i '/holberton.*/d' /etc/security/limits.conf": }
