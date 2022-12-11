# Using puppet to install flask 2.1.0 from pip3

package { 'Flask':
ensure   =>    '2.1.0',
name     =>    'Flask',
provider =>    pip3,
}
