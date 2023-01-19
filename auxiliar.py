import random

# ---- CATEGORÍAS GRAMATICALES ----


# CONECTORES
det = ['la']
# adv  = ['a','para','allá a','más','tras','mas','cada','hasta']
adv = ['a', 'tras', 'mas']


# SUSTANTIVOS
sus = ['balda', 'rama', 'parra', 'sala', 'garganta', 'mama', 'cana', 'pana']
sus += ['cama', 'baba', 'amalgama', 'nana',
        'aldaba', 'ala', 'atalaya', 'mamada']
sus += ['hamaca', 'caña', 'raya', 'araña', 'camada', 'masa', 'mata', 'cañada']
sus += ['manzana', 'pasta', 'gansa', 'mañana',
        'arcada', 'arca', 'calada', 'cala']
sus += ['tapa', 'carcajada', 'rama', 'armada',
        'mamá', 'lana', 'anagrama', 'maga']
sus += ['hada', 'cara', 'capa', 'rata',
        'pata', 'mata', 'bala', 'chalana', 'alma']
sus += ['campana', 'manzana', 'granada', 'chamana', 'pala', 'nada', 'panza']
sus += ['malla', 'carraca', 'camarada',
        'canalla', 'kata', 'catalana', 'balanza']
sus += ['avalancha', 'lancha', 'maza',
        'mampara', 'lámpara', 'manta', 'alabanza']
sus += ['hazaña', 'lata', 'catarata', 'patata',
        'arpa', 'carpa', 'rampa', 'calzada']
sus += ['maraca', 'papa', 'alacrana', 'campana', 'pava', 'amarra', 'macarra']
sus += ['carraca', 'lancha', 'carta', 'tarta',
        'mapa', 'tartana', 'zarza', 'planta']
sus += ['fabada', 'caspa', 'aspa', 'ñapa',
        'maña', 'hampa', 'ganga', 'manga', 'rampa']
sus += ['naranja', 'patraña', 'calaña', 'palabra', 'pájara', 'fama', 'charla']
sus += ['marcha', 'batalla', 'ráfaga',
        'fantasma', 'parrafada', 'trampa', 'jarana']
sus += ['manada', 'calma', 'patada', 'campanada', 'arma', 'grada', 'palma']
sus += ['garra', 'cagada']
# sus += ['maña','maldad','sal','tana','mar','paz',]

# SUSTANTIVOS PROPIOS
sus += ['Tara', 'Zahara', 'Alma', 'Lara',
        'Alba', 'Maná', 'Sara', 'Granada', 'Alana']
sus += ['Amaya', 'Ana', 'Amanda', 'Marajá', 'Marga', 'Alcántara']


# ADJETIVOS
adj = ['salada', 'marcada', 'ganada',
       'alcanzada', 'sacada', 'sanada', 'atascada']
adj += ['rayada', 'arrancada', 'asada',
        'alabada', 'amada', 'amañada', 'arañada']
adj += ['arrastrada', 'arrasada', 'alta', 'acallada', 'mansa', 'mala', 'ajada']
adj += ['atrapada', 'acabada', 'traspasada',
        'tapada', 'armada', 'acallada', 'callada']
adj += ['marrana', 'amarrada', 'atada',
        'cabalgada', 'larga', 'chalada', 'alargada']
adj += ['capada', 'cazada', 'achaparrada',
        'tallada', 'parada', 'malparada', 'mascada']
adj += ['cansada', 'acampada', 'apalabrada', 'acaparada', 'flaca', 'malsana']
adj += ['rasgada', 'mascada', 'asamblada',
        'asalvajada', 'plantada', 'casada', 'alzada']
adj += ['canalla', 'alzada', 'arramplada',
        'aplanada', 'plana', 'agasajada', 'acampanada']
adj += ['avanzada', 'jalada', 'mazada', 'dañada',
        'lacada', 'pasada', 'majara', 'trabada']
adj += ['amparada', 'ajada', 'maja', 'alada',
        'majara', 'alarmada', 'amarga', 'amargada']
# adj += ['arada',]

# VERBOS
#   - PRESENTE
ver = ['falla', 'ama', 'mata', 'gana', 'casa', 'tapa', 'alcanza', 'alaba']
ver += ['arranca', 'caga', 'cava', 'calla', 'mama', 'amasa', 'traga', 'amansa']
ver += ['arma', 'rasga', 'saca', 'bala', 'marcha', 'cabalga', 'acalla', 'sana']
ver += ['ara', 'araña', 'caza', 'raya', 'asa',
        'amaga', 'daña', 'amamanta', 'acapara']
ver += ['halla', 'arrasa', 'da', 'talla',
        'marca', 'habla', 'fala', 'campa', 'canta']
ver += ['manja', 'tala', 'alza', 'agarra', 'baña', 'aplana', 'alaba', 'lanza']
ver += ['avanza', 'casca', 'raja', 'raspa', 'abarca', 'da']
ver += ['trabaja', 'plasma', 'hazla', 'atrapa',
        'machaca', 'ladra', 'arrastra', 'anda']
ver += ['manda', 'achanta', 'abarca', 'cansa', 'va', 'agrada', 'taladra']

#   - PASADO
ver += ['fallaba', 'amaba', 'amargaba', 'mataba', 'ganaba', 'casaba', 'tapaba']
ver += ['alcanzaba', 'alababa', 'abarcaba',
        'arrancaba', 'cagaba', 'cavaba', 'callaba']
ver += ['arañaba', 'rayaba', 'mamaba',
        'amasaba', 'tragaba', 'amansaba', 'armaba']
ver += ['plasmaba', 'pastaba', 'atrapaba', 'rasgaba', 'ataba', 'castraba']
ver += ['araba', 'asaba', 'cantaba', 'balaba',
        'marchaba', 'cabalgaba', 'cazaba']
ver += ['acallaba', 'rasgaba', 'sacaba',
        'sanaba', 'amagaba', 'dañaba', 'amamantaba']
ver += ['acaparaba', 'hallaba', 'arrasaba',
        'daba', 'marcaba', 'tallaba', 'hablaba']
ver += ['campaba', 'manjaba', 'talaba',
        'alzaba', 'agarraba', 'bañaba', 'avanzaba']
ver += ['cascaba', 'rajaba', 'raspaba', 'paraba', 'agradaba', 'taladraba']

#   - FUTURO
ver += ['sabrá', 'alcanzará', 'alabará',
        'arañará', 'amará', 'amansará', 'casará']
ver += ['arañará', 'rayará', 'tragará', 'amasará', 'arrancará', 'blablablá']
ver += ['acallará', 'callará', 'cabalgará', 'tapará', 'plasmará', 'pastará']
ver += ['cavará', 'cabrá', 'acabará', 'mamará',
        'atrapará', 'rasgará', 'amamantará']
ver += ['rasgará', 'sanará', 'amagará',
        'dañará', 'cazará', 'acaparará', 'campará']
ver += ['hallará', 'arrasará', 'dará',
        'tallará', 'marcará', 'hablará', 'manjará']
ver += ['talará', 'alzará', 'agarrará', 'sabrá', 'hará', 'lanzará', 'avanzará']
ver += ['cascará', 'rajará', 'raspará',
        'parará', 'amargará', 'dará', 'agradará']
ver += ['taladrará']

# FRASES HECHAS
fra = ['cada mañana', 'para nada', 'a cada nada',
       'a cada calada', 'tras la mar']
fra += ['a la mañana', 'tralará', 'a las tantas', '¡AJÁ!']

# LOCURAS
loc = ['¡MAMÁ, LANZA XANAX!', 'Cavaba la rana sin ganas']


# GENERADOR DE CAT PLURALES
detp = [str(d)+'s' if d != '' else '' for d in det]
susp = [str(s)+'s' if s != '' else '' for s in sus]
adjp = [str(s)+'s' if s != '' else '' for s in adj]
verp = [str(s)+'n' if s != '' else '' for s in ver]

# RIMAS
rimas = ['0011', '0101', '0111', '0110']

# random.shuffle
for _ in range(10):
    random.shuffle(rimas)
    random.shuffle(adv)
    random.shuffle(sus)
    random.shuffle(adj)
    random.shuffle(ver)
    random.shuffle(fra)
    random.shuffle(detp)
    random.shuffle(susp)
    random.shuffle(adjp)
    random.shuffle(verp)


# ESTRUCTURA DE VERSO - SUBLISTAS INDICAN CONTENIDO OPCIONAL
e1 = [[['det', 'sus'], ''], ['adj', ''], 'ver',
      [['adv', 'det', 'sus'], ''], ['adj', '']]
e2 = [['adj', ''], [['det', 'sus'], ''], 'ver',
      [['adv', 'det', 'sus'], ''], ['adj', '']]
e3 = [[['det', 'sus'], ''], ['adj', ''], 'ver',
      ['adj', ''], [['adv', 'det', 'sus'], '']]
e4 = [['adj', ''],  [['det', 'sus'], ''], 'ver',
      ['adj', ''], [['adv', 'det', 'sus'], '']]
_ESTRUCTURA_VERSO_ = [e1, e2, e3, e4]


def get_rand_struct(estructura=random.choice(_ESTRUCTURA_VERSO_)):
    if isinstance(estructura, str) and estructura != '':
        return [estructura]
    res = []
    for elem in estructura:
        if elem == '':
            continue
        elif isinstance(elem, str):
            res += [elem]
        else:
            if sum([1 if isinstance(e, str) and e != '' else 0 for e in elem]) == len(elem):
                res += elem
            else:
                res += get_rand_struct(random.choice(elem))
    return res


# ORDEN E INDEXADO DE PALABRAS
_CAT_IDX_ = ['det', 'sus', 'adj', 'ver', 'adv',
             'fra', 'loc', 'detp', 'susp', 'adjp', 'verp']
_CAT_ = [det, sus, adj, ver, adv, fra, loc, detp, susp, adjp, verp]


# TERMINACIONES
ter = {}
for c in _CAT_:
    for p in c:
        if p[-3:] not in ter.keys() and (p[-3:]).isalpha():
            ter[p[-3:]] = 1
        elif p[-3:] in ter.keys():
            ter[p[-3:]] += 1

# FUNCIONES AUXILIARES
def riman(p1, p2):
    return p1[-3:] == p2[-3:]


def limpia_texto(texto):
    while '  ' in texto or ' ,' in texto or '\n ' in texto:
        texto = texto.replace('  ', ' ')
        texto = texto.replace(' ,', ' ')
        texto = texto.replace('\n ', '\n')
    return texto


def instancia_estructuras(n=1000):
    res = []
    for i in range(n):
        r = get_rand_struct()
        res += [r] if r not in res else []
        random.shuffle(res)
    return res


def texto_to_dict(texto):
    d = {}
    for w in texto.split(' '):
        if w.isalpha():
            if w in d.keys():
                d[w] += 1
            else:
                d[w] = 1
    return d


def get_plural(estructura):
    return [str(r) + 'p' if str(r)+'p' in _CAT_IDX_ else str(r) for r in estructura]


def get_rima(cat, term):
    categoria = _CAT_[_CAT_IDX_.index(cat)]
    random.shuffle(categoria)
    for p in categoria:
        if riman(p, term):
            return p
    return random.choice(categoria)


def get_categoria(buscado):
    for c in _CAT_:
        if buscado in c:
            return _CAT_IDX_[_CAT_.index(c)]


def split_m(linea):
    terminales, res, actual = ['\n', ',', '.',
                               '?', '¿', '!', '¡', '{', '}'], [], ''
    for c in linea:
        if c in terminales:
            if actual != '':
                res += [actual]
            actual = ''
            continue
        actual += c.lower()
    if res != [] and res != ['']:
        return res
    return []

# CLASE STRUCT VERSO
class StructVerso():
    def __init__(self, texto_anterior, plural=0, a_rimar=''):
        self.rima = a_rimar
        self.plural = plural
        self.estructuras = instancia_estructuras()
        self.texto_anterior = texto_anterior

    def choice_word(self, cat):
        arr_p = [100 if w not in self.ocurrencias.keys() else 1 for w in cat]
        arr_p = [ap/sum(arr_p) for ap in arr_p]
        return random.choices(cat, weights=arr_p,k=1)[0]

    def get_instancia(self):
        res = ''
        self.ocurrencias = texto_to_dict(self.texto_anterior)
        self.estructura = self.get_rythm_struct()
        if self.plural == 1:
            self.estructura = get_plural(self.estructura)
        for i in range(len(self.estructura) - 1):
            palabra = self.choice_word(
                _CAT_[_CAT_IDX_.index(self.estructura[i])])
            if palabra not in self.ocurrencias.keys():
                self.ocurrencias[palabra] = 0
            self.ocurrencias[palabra] += 1
            res += palabra + ' '
        for _ in range(500):
            palabra = get_rima(self.estructura[-1], self.rima)
            if palabra not in self.ocurrencias.keys():
                self.ocurrencias[palabra] = 0
                break
        self.ocurrencias[palabra] += 1
        return res + palabra, self.ocurrencias

    def get_rythm_struct(self):
        for estructura in self.estructuras:
            for p in _CAT_[_CAT_IDX_.index(estructura[-1])]:
                if riman(p, self.rima):
                    return estructura
        return random.choice(self.estructuras)
