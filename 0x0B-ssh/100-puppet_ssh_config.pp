# A puppet manifest to make SSH client configuration in order to use the private key ~/.ssh/school
# A puppet manifest to make SSH client configuration in order to refuse to authenticate using a password


exec { "/bin/echo 'IdentityFIle ~/.ssh/school' >> /etc/ssh/ssh_config": }
