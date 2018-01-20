# ButterSalt-saltapi


ButterSalt-saltapi is a wrapper for salt rest_cherrypy API!

## Installation

`pip install buttersalt-saltapi`

## Usage

A full-access access for linux user lfzyx need to add the following configuration items to the /etc/salt/master configuration file :

<pre>
external_auth:
  pam:
    lfzyx:
        - .*
        - '@runner'
        - '@wheel'

rest_cherrypy:
  port: 8000
  disable_ssl: True
</pre>

Then run `systemctl restart salt-api && systemctl restart salt-master.service`

Now in you project, use the following code :

`from buttersalt_saltapi import saltapi`

`salt = saltapi.SaltApi(baseurl='SALT API address', username='SALT API username', password='SALT API password')`

`salt.login()`