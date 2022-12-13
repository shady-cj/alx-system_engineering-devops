# A puppet manifest to make SSH client configuration in order to use the private key ~/.ssh/school
# A puppet manifest to make SSH client configuration in order to refuse to authenticate using a password


include ssh::client
class { 'ssh::client':
  options => {
    'Host *' => {
      'PasswordAuthentication' => 'no',
      'IdentityFile'           => '~/.ssh/school',
    },
  },
}
