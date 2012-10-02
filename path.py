import os

LOCAL = '/usr/local/bin:/usr/local/sbin:'
HOME = '/Users/jaigouk'  ### !!! REPLACE WITH YOUR HOME PATH !!! ###
RVM = HOME + '/.rvm/bin:'
NODE = HOME + '/.nvm/v0.8.9/bin:'
# Sublime's default path is
# /usr/bin:/bin:/usr/sbin:/sbin
os.environ['PATH'] += ':'
os.environ['PATH'] += LOCAL
os.environ['PATH'] += RVM
os.environ['PATH'] += NODE
print 'PATH = ' + os.environ['PATH']
