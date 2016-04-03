#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "010", "020", "030", "040", "041", "042", "045", "048", "049", "050", "055", "060", "080", "100", "120", "160", "180", "190", "200", "220", "240", "260", "280", "300", "320"]
munpos =  ["SINCELEJO", "BUENAVISTA", "CAIMITO", "COLOSO (RICAURTE)", "COROZAL", "COVENAS", "EL ROBLE", "CHALAN", "GALERAS (NUEVA GRANADA)", "GUARANDA", "LA UNION", "LOS PALMITOS", "MAJAGUAL", "MORROA", "OVEJAS", "PALMITO", "SAMPUES", "SAN BENITO ABAD", "SAN JUAN DE BETULIA (BETULIA)", "SAN MARCOS", "SAN ONOFRE", "SAN PEDRO", "SINCE", "SUCRE", "TOLU", "TOLUVIEJO"]
DANE = ["70001", "15109", "70124", "70204", "70215", "70221", "70233", "70230", "70235", "70265", "5400", "70418", "70429", "70473", "70508", "70523", "70670", "70678", "70702", "70708", "70713", "5664", "70742", "19785", "70820", "70823"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Sucre_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=28&cod_mpio="+amazonas[munpo]
		

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