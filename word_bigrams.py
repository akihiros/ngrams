import nltk
from nltk.collections import *


f = open('text/FIFAnews-Spanish.txt')
raw = f.read()
tokens = nltk.word_tokenize(raw)
bgs = nltk.bigrams(tokens)
fdist = nltk.FreqDist(bgs)
fdists = fdist.most_common()

print(fdists)
f.close()

'''
[(('’', 's'), 32), (('.', '``'), 17), (('.', "''"), 17), (('World', 'Cup'), 16), (('in', 'the'), 16), (('of', 'the'), 13), (('women', "'s"), 12), ((',', 'the'), 11), ((',', "''"), 9), (('.', 'I'), 9), (("'s", 'football'), 8), (('Women', "'s"), 8), (('a', 'new'), 7), (('Spain', '’'), 7), (('women', '’'), 7), (("'s", 'World'), 7), ((',', 'and'), 7), (('and', 'the'), 7), (('’', 't'), 6), (("''", 'said'), 6), (('to', 'be'), 6), (('European', 'Championship'), 6), (('.', 'We'), 6), (('we', '’'), 5), (('in', 'a'), 5), (('``', 'The'), 5), ((',', 'but'), 5), (('Championship', 'runners-up'), 5), (('at', 'the'), 5), (('the', 'best'), 5), (('on', 'the'), 5), (('is', 'the'), 5), (('for', 'the'), 5), (('the', 'FIFA'), 5), (('’', 've'), 4), ((',', '”'), 4), ((',', 'who'), 4)


[(('de', 'la'), 24), (('du', 'Monde'), 20), (('Coupe', 'du'), 17), (('la', 'Coupe'), 14), (('le', 'football'), 13), (('l', '’'), 13), (('la', 'FIFA'), 11), (('.', '``'), 11), (('football', 'feminin'), 10), (('Monde', 'Feminine'), 10), (("''", '-'), 9), (('d', '’'), 9), (('et', 'la'), 7), (("''", ','), 7), (('a', 'la'), 7), (('.', 'Je'), 7), (('Feminine', 'de'), 6), ((',', 'le'), 6), (('pour', 'la'), 6), (('du', 'football'), 6), (('.', 'La'), 6), (('Vice-championnes', "d'Europe"), 6), ((',', 'la'), 5), (('et', 'des'), 5), (('.', "''"), 5), ((',', 'ou'), 5), (('.', 'Nous'), 5), (('n', '’'), 5), (('’', 'est'), 5), (('j', '’'), 5), ((',', 'et'), 4), (('pour', 'le'), 4), (('FIFA', ','), 4), (('et', 'les'), 4), (('nous', 'avons'), 4), ((',', 'mais'), 4), (('Championnes', "d'Europe"), 4), (('jour', 'ou'), 4), ((',', 'nous'), 4), (('.', 'Le'), 4), (('sur', 'le'), 4), (('’', 'ai'), 4), (('ou', 'je'), 4), (('.', 'En'), 3), (('sur', 'les'), 3), (('.', 'On'), 3), (('Coupes', 'du'), 3), (('FIFA', 'en'), 3), (('que', 'nous'), 3), (('remporte', 'la'), 3), (('Monde', 'de'), 3), (('annee', '2018'), 3), (('feminin', 'espagnol'), 3),


[((',', 'die'), 18), (('.', '``'), 14), (('.', "''"), 13), (("''", ','), 12), (('fur', 'die'), 7), ((',', 'und'), 7), (('und', 'die'), 7), ((',', 'dass'), 7), (('.', 'Ich'), 7), (('.', 'Wir'), 6), (('.', 'Die'), 6), (('nicht', 'mehr'), 6), (('sein', ','), 5), (('.', 'Das'), 5), (('mit', 'der'), 4), (('der', 'FIFA'), 4), (('ist', 'die'), 4), (('.', 'Es'), 4), (('Es', 'ist'), 4), (('bei', 'der'), 4), (('in', 'den'), 4), ((',', 'das'), 4), (('wenn', 'ich'), 4), (('an', 'der'), 3), ((',', 'so'), 3), ((',', 'wo'), 3), (('.', 'Diese'), 3), (('auf', 'der'), 3), (('fur', 'den'), 3), (('``', 'Der'), 3), ((',', 'erklart'), 3), ((',', 'aber'), 3), (('Lopez', '.'), 3), ((',', 'mit'), 3), (('hat', 'sich'), 3), (('uber', 'die'), 3), (('ist', 'der'), 3), (('der', 'Frauenfussball'), 3), (('auf', 'die'), 3), (('in', 'der'), 3), (('.', 'Sie'), 3), (('der', 'Welt'), 3), (('sein', '.'), 3), (("''", 'Ich'), 3), (('zu', 'sein'), 3), ((',', 'wenn'), 3), (('werden', ','), 3), (('ist', 'es'), 3), (('fur', 'Trainer'), 3), (('FIFA', 'Forward'), 3), (('fur', 'Schiedsrichter'), 3), (('Schiedsrichter', 'und'), 3), (('das', 'Schiedsrichterwesen'), 3), (('Zahl', 'der'), 3), (('fur', 'das'), 3), (('Jahr', '2018'), 2), (('fur', 'ein'), 2), (('ein', 'neues'), 2), ((',', 'spannende'), 2), (('Qualifikationsspiele', 'und'), 2), (('2018', 'in'), 2), (('gar', 'nicht'), 2)


[(('de', 'la'), 34), (('en', 'el'), 16), (('el', 'futbol'), 14), (('.', '“'), 14), (('la', 'FIFA'), 13), (('”', ','), 11), (('futbol', 'femenino'), 10), (('de', 'Europa'), 10), ((',', 'el'), 9), (('y', 'la'), 9), (('en', 'la'), 9), (('la', 'Copa'), 8), (('Copa', 'Mundial'), 8), ((',', 'que'), 8), (('”', '.'), 7), ((',', 'y'), 7), (('la', 'PSSI'), 7), (('Mundial', 'Femenina'), 6), (('Subcampeonas', 'de'), 6), (('.', 'En'), 6), (('a', 'la'), 6), ((',', 'se'), 6), (('de', 'las'), 6), (("''", '.'), 6), (('de', 'Desarrollo'), 6), (('para', 'el'), 5), ((',', 'pero'), 5), (('para', 'la'), 5), (('lo', 'que'), 5), (('de', 'los'), 5), (('a', 'las'), 5), (('que', ','), 5), (('en', 'un'), 5), (('la', 'seleccion'), 5), (('.', 'La'), 5), (('La', 'PSSI'), 5), (('FIFA', 'y'), 4), (('y', 'las'), 4), (('Femenina', 'de'), 4), (('el', 'Mundial'), 4), (('y', 'en'), 4), (('que', 'se'), 4), (('Campeonas', 'de'), 4), (('mas', 'de'), 4), (('?', ','), 4), (('ganas', 'de'), 4), (('se', 'ha'), 4), (('Programa', 'de'), 4), (('arbitros', 'y'), 4), (('los', 'arbitros'), 4), (('programa', 'de'), 4), (('a', 'su'), 3), (('FIFA', ','), 3), (('del', 'futbol'), 3), (('femenino', 'espanol'), 3), (('de', 'sus'), 3), (('“', 'El'), 3), (('es', 'la'), 3), (('las', 'selecciones'), 3), (('.', 'Los'), 3), (('Europa', 'y'), 3), (('del', 'Mundo'), 3), (('Europa', 'No'), 3), (('la', 'federacion'), 3), (('jugadoras', 'federadas'), 3), (('Vilda', '.'), 3), ((',', 'en'), 3), (('de', 'un'), 3), (('las', 'ju

'''