import auxiliar as aux
from auxiliar import StructVerso as SV
import random


class PoemA:

    def __init__(self, estrofas=4):
        self.estrofas = estrofas
        self.rima = ''
        self.ocurrencias = {}
        self.poema = '\n'
        # self.traza         = ''

    def init_rimas(self):
        rimas_dict = {}
        for i in set(self.rima):
            for _ in range(50):
                c = random.choice(list(aux.ter.keys()))
                if int(aux.ter[c]) > 5 and c not in rimas_dict.values():
                    break
            rimas_dict[i] = c
        return rimas_dict

    def get_poem(self):

        for _ in range(self.estrofas):

            # PARA CADA ESTROFA ELEGIMOS UN PAtron DE RIMAS
            self.rima   = random.choice(aux.rimas)
            self.patron = self.init_rimas()
            self.plural = random.randint(0, 1)
            t = []

            for i in range(len(self.rima)):
                idx = str(self.rima[i])
                for _ in range(10):
                    # INSTANCIAMOS UN VERSO Y ACTUALIZAMOS LAS OCURRENCIAS
                    s = SV(self.poema, self.plural, self.patron[idx])
                    verso, occ = s.get_instancia()
                    if verso.split(' ')[-1] not in self.ocurrencias.keys():
                        break

                self.ocurrencias = occ
                t.append(verso.split(' ')[-1])

                if i == 0:
                    verso = verso[0].upper() + verso[1:]

                # AÑADIMOS EL VERSO Y EL SIGNO CORRESP
                self.poema += verso + \
                    ',\n' if i < len(self.rima) - 1 else verso + ',\n'

            self.poema += '\n\n'
        self.poema = aux.limpia_texto(self.poema)
        return self.poema


p = PoemA()
p.get_poem()
print(p.poema)
