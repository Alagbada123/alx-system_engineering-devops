# Fix Apache 500 error caused by incorrect permissions on web directory
file { '/var/www/html':
  ensure  => directory,
  mode    => '0755',
  owner   => 'www-data',
  group   => 'www-data',
  recurse => true, # Optional: recursively set permissions if needed
  notify  => Service['apache2'], # Restart Apache if changes are made
}

# Ensure Apache service is managed
service { 'apache2':
  ensure => running,
  enable => true,
}
