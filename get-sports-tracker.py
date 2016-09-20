import os
from datetime import datetime

i = datetime.now()

USUARIO = 'jeeean'
DATA = i.strftime('%Y-%m-%d')
NOME_DA_PASTA = 'sports-tracker'

f = open('list.txt', 'r')
lista = f.readline()

ids = set([])

while(lista):
	expressao_inicio = '<a href="/workout/'
	inicio = lista.find(expressao_inicio+USUARIO+'/') + len(expressao_inicio)+1 + len(USUARIO)
	fim = inicio + 24
	identificador = lista[inicio:fim]
	if len(identificador) == 24 and identificador.find(' ') == -1 and identificador.find('>') == -1:
		ids.add(lista[inicio:fim])
	lista = lista[fim:]

token = '24bp4kkk8gbdkf491jfogv1is7e1jd5d'

for identificador in ids:
	url = 'http://www.sports-tracker.com/apiserver/v1/workout/exportGpx/'+identificador+'?token='+token
	os.system('wget '+url+' -O '+NOME_DA_PASTA+'-'+identificador+'.gpx')

os.system('mkdir '+NOME_DA_PASTA)
os.system('mv *.gpx '+NOME_DA_PASTA)
os.system('tar -zcvf '+NOME_DA_PASTA+DATA+'.tar.gz '+NOME_DA_PASTA)
os.system('rm -r '+NOME_DA_PASTA)