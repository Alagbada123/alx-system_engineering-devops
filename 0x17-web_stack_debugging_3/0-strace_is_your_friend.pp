# automated puppet fix (to find out why Apache is returning a 500 error)

exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/\.phpp/.php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
