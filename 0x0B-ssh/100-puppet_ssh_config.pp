# A puppet manifest to make SSH client configuration in order to use the private key ~/.ssh/school
# A puppet manifest to make SSH client configuration in order to refuse to authenticate using a password
include stdlib
file_line { 'passwordauth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '.*PasswordAuthentication.*'
}


file_line { 'IdentityFile':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  after    => 'StrictHostKeyChecking',
  line     => '    IdentityFile ~/.ssh/school',
  match    => '.*IdentityFile.*',
  multiple => true
}
