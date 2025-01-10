# kill process killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
 onlyif  => 'pgrep killmenow',
}
