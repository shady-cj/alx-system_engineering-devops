# A puppet manifest to make SSH client configuration in order to use the private key ~/.ssh/school
# A puppet manifest to make SSH client configuration in order to refuse to authenticate using a password

exec { "/bin/sed -i '0,/.*PasswordAuthentication.*/{s/.*PasswordAuthentication.*/    PasswordAuthentication no/}' /etc/ssh/ssh_config": }
exec { "/bin/sed -i '0,/.*IdentityFile.*/{s/.*IdentityFile.*/    IdentityFile \~\/\.ssh\/school/}' /etc/ssh/ssh_config": }
