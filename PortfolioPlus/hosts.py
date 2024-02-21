from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'handbook', 'handbook.urls', name='handbook'),
)
