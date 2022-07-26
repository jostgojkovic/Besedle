from model import Besedle
from model import nova_igra
import bottle

besedle = nova_igra()

@bottle.get('/')
def osnovna_stran():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    igra = nova_igra()
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    return bottle.template('igra.tpl')

bottle.run(reloader=True, debug=True)