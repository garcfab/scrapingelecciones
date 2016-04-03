#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' Borre San JUan De URE
'''

# Vector de Amazonas
amazonas = ["001", "004", "007", "009", "010", "013", "014", "016", "019", "020", "022", "023", "024", "025", "027", "028", "031", "032", "033", "034", "037", "040", "043", "046", "049", "055", "058", "061"]
munpos =  ["MONTERIA", "AYAPEL", "BUENAVISTA", "CANALETE", "CERETE", "CIENAGA DE ORO", "COTORRA (BONGO)", "CHIMA", "CHINU", "LA APARTADA (FRONTERA)", "LORICA", "LOS CORDOBAS", "MOMIL", "MONTELIBANO", "MONITOS", "PLANETA RICA", "PUEBLO NUEVO", "PUERTO LIBERTADOR", "PUERTO ESCONDIDO", "PURISIMA", "SAHAGUN", "SAN ANDRES DE SOTAVENTO", "SAN ANTERO", "SAN BERNARDO DEL VIENTO", "SAN CARLOS", "SAN PELAYO", "TIERRALTA", "VALENCIA"]
DANE = ["23001", "23068", "23079", "23090", "23162", "23189", "23300", "23168", "23182", "23350", "23417", "23419", "23464", "23466", "23500", "23555", "23570", "23580", "23574", "23586", "23660", "23670", "23672", "23675", "23678", "23686", "23807", "23815", "23855"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Cordoba_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=13&cod_mpio="+amazonas[munpo]
	

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