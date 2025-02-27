# automated puppet fix (to find out why Apache is returning a 500 error)

exec { 'fix_wp_settings': 
  command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  onlyif => 'grep ".phpp" /var/www/html/wp-settings.php',
  path => ['/bin', '/usr/bin'],
}
