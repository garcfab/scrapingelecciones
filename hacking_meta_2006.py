#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "005", "006", "008", "010", "015", "020", "025", "027", "028", "030", "035", "040", "041", "042", "043", "044", "045", "046", "047", "048", "049", "050", "055", "058", "059", "060", "074", "080"]
munpos =  ["VILLAVICENCIO", "ACACIAS", "BARRANCA DE UPIA", "CABUYARO", "CASTILLA LA NUEVA", "CUBARRAL", "CUMARAL", "EL CALVARIO", "EL CASTILLO", "EL DORADO", "FUENTE DE ORO", "GRANADA", "GUAMAL", "LA MACARENA", "LEJANIAS", "PUERTO GAITAN", "MESETAS", "PUERTO LOPEZ", "MAPIRIPAN", "PUERTO CONCORDIA", "PUERTO LLERAS", "PUERTO RICO", "RESTREPO", "SAN CARLOS DE GUAROA", "SAN JUAN DE ARAMA", "SAN JUANITO", "SAN MARTIN DE LOS LLANOS", "URIBE", "VISTA HERMOSA"]
DANE = ["50001", "50006", "50110", "50124", "50150", "50223", "50226", "50245", "50251", "50270", "50287", "50313", "50318", "50350", "50400", "50568", "50330", "50573", "50325", "50450", "50577", "50590", "50606", "50680", "50683", "50686", "50689", "50370", "50711"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Meta_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=52&cod_mpio="+amazonas[munpo]
	

	# Parsing link
	page = urllib2.urlopen(url)

	# Hacienda la Sopa
	soup = BeautifulSoup(page,convertEntities=BeautifulSoup.HTML_ENTITIES)
	# soup2 = soup.prettify(formatter=None)
	# print soup2.contents
	# print soup
	# print 'vamos'

	# Orden de grabacion. 
	'''
	1. Votos en Blanco (6)
	2. Potencial de votacion (8)
	3. Votos Validos (10)
	4. Votos Totales (12)
	5. Votos Nulos (14)
	6. Uribe (20)
	7. Carlos Gaviria (22)
	8. Horacio Serpa (24)
	9. Mockus (26)
	10. Enrique Parejo Gonzalez (28)
	11. Alvaro Leyva (30)
	12. Carlos Arturo Rincón Barreto (32)
	'''

	# Celdas es lo que tiene el dato de interes
	valores=soup.findAll('td',{'class':'valor_contenido'})

	# Valores es lo que tiene el rotulo de cada dato
	rotulo=soup.findAll('td',{'class':'datos_contenido'})
	print "Grabando municipio", munpos[munpo]

	f.write(munpos[munpo]+ '\t'+str(DANE[munpo]) + '\t'+ valores[6].text+ '\t' + valores[8].text + '\t' + valores[10].text + '\t' + valores[12].text + '\t' +\
		     valores[14].text + '\t' + valores[20].text+ '\t' + valores[22].text + '\t' + valores[24].text + '\t' + valores[26].text + \
		    '\t' + valores[28].text + '\t' + valores[30].text+ '\t' + valores[32].text+'\n')

f.close()