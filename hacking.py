#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup




# Vector de Amazonas
amazonas = ["001", "007", "010", "013", "016", "017", "019", "021", "022", "030", "040"]
munpos =  ["LETICIA", "PUERTO NARINO", "EL ENCANTO", "LA CHORRERA", "LA PEDRERA", "LA VICTORIA", "MIRITI PARANA", "PUERTO SANTANDER", "TARAPACA", "PUERTO ALEGRIA", "PUERTO ARICA"]
DANE = ["91001", "", "91263", "91405", "91407", "91430", "91460", "91669", "91798", "91530", "91536"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Amazonas_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&cod_depto=60&num_com=99&cod_mpio="+amazonas[munpo]
	

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
	print valores[20].text

	f.write(munpos[munpo]+ '\t'+str(DANE[munpo]) + '\t'+ valores[6].text+ '\t' + valores[8].text + '\t' + valores[10].text + '\t' + valores[12].text + '\t' +\
		     valores[14].text + '\t' + valores[20].text+ '\t' + valores[22].text + '\t' + valores[24].text + '\t' + valores[26].text + \
		    '\t' + valores[28].text + '\t' + valores[30].text+ '\t' + valores[32].text+'\n')

f.close()