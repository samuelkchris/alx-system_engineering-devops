exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/bin:/usr/bin:/usr/local/bin',
  onlyif  => 'pgrep killmenow',
}
