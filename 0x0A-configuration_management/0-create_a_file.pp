# Using puppet to create a file /tmp/school
# The file owner and group should be www-data
# The file permission should be 0744
# The file content should be 'I love Puppet'

file { 'school':
ensure  => present,
path    => '/tmp/school',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
}
