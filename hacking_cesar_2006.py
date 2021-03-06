#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "075", "150", "170", "180", "200", "225", "300", "375", "410", "415", "450", "525", "600", "608", "625", "650", "700", "720", "750", "800", "825", "850", "875", "900"]
munpos =  ["VALLEDUPAR", "AGUACHICA", "AGUSTIN CODAZZI", "ASTREA", "BECERRIL", "BOSCONIA", "CURUMANI", "CHIMICHAGUA", "CHIRIGUANA", "EL COPEY", "EL PASO", "GAMARRA", "GONZALEZ", "LA GLORIA", "LA JAGUA DE IBIRICO", "MANAURE BALCON DEL CESAR (MANA", "PAILITAS", "PELAYA", "PUEBLO BELLO", "RIO DE ORO", "SAN ALBERTO", "LA PAZ", "SAN DIEGO", "SAN MARTIN", "TAMALAMEQUE"]
DANE = ["20001", "20011", "20013", "20032", "20045", "20060", "20228", "20175", "20178", "20238", "20250", "20295", "20310", "20383", "20400", "20443", "20517", "20550", "20570", "20614", "20710", "20621", "20750", "20770", "20787"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Cesar_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=12&cod_mpio="+amazonas[munpo]
	

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