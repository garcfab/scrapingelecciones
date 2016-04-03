#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' Borre San JUan De URE
'''

# Vector de Amazonas
amazonas = ["001", "004", "007", "010", "013", "016", "019", "022", "025", "028", "031", "034", "037", "040", "043", "044", "046", "047", "049", "050", "051", "052", "055", "056", "058", "061", "064", "067", "070", "074", "076", "079", "082", "085", "088", "091", "094"]
munpos =  ["NEIVA", "ACEVEDO", "AGRADO", "AIPE", "ALGECIRAS", "ALTAMIRA", "BARAYA", "CAMPOALEGRE", "TESALIA (CARNICERIAS)", "COLOMBIA", "ELIAS", "GARZON", "GIGANTE", "GUADALUPE", "HOBO", "ISNOS", "IQUIRA", "LA ARGENTINA (PLATA VIEJA)", "LA PLATA", "NATAGA", "OPORAPA", "PAICOL", "PALERMO", "PALESTINA", "PITAL", "PITALITO", "RIVERA", "SALADOBLANCO", "SAN AGUSTIN", "SANTA MARIA", "SUAZA", "TARQUI", "TELLO", "TERUEL", "TIMANA", "VILLAVIEJA", "YAGUARA"]
DANE = ["41001", "41006", "41013", "41016", "41020", "41026", "41078", "41132", "41797", "41206", "41244", "41298", "41306", "41319", "41349", "41359", "41357", "41378", "41396", "41483", "41503", "41518", "41524", "41530", "41548", "41551", "41615", "41660", "41668", "41676", "41770", "41791", "41799", "41801", "41807", "41872", "41885"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('HUILA_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=19&cod_mpio="+amazonas[munpo]
	

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