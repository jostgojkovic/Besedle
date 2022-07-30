import model
import bottle

besedle = model.nova_igra()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id_igre = besedle.prost_id_igre()
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra = model.nova_igra()
    return bottle.template('igra.tpl', igra=igra, id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    beseda = bottle.request.forms.getunicode('beseda')
    besedle.ugibaj(id_igre, beseda)
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/img/<picture>')
def serve_picture(picture):
    return bottle.static_file(picture, root='img')

bottle.run(reloader=True, debug=True)