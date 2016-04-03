#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "004", "007", "010", "013", "016", "019", "022", "025", "028", "031", "034", "037", "040", "043", "046", "049", "052", "055", "058", "061", "064", "067", "070", "073", "076", "079", "080", "082", "085", "087", "088", "089", "091", "094", "097", "100", "103", "105", "106", "109", "112", "115", "118", "121", "124", "127"]
munpos =  ["IBAGUE", "ALPUJARRA", "ALVARADO", "AMBALEMA", "ANZOATEGUI", "ARMERO (GUAYABAL)", "ATACO", "CAJAMARCA", "CARMEN DE APICALA", "CASABIANCA", "COELLO", "COYAIMA", "CUNDAY", "CHAPARRAL", "DOLORES", "ESPINAL", "FALAN", "FLANDES", "FRESNO", "GUAMO", "HERVEO", "HONDA", "ICONONZO", "LERIDA", "LIBANO", "MARIQUITA", "MELGAR", "MURILLO", "NATAGAIMA", "ORTEGA", "PALOCABILDO", "PIEDRAS", "PLANADAS", "PRADO", "PURIFICACION", "RIOBLANCO", "RONCESVALLES", "ROVIRA", "SALDANA", "SAN ANTONIO", "SAN LUIS", "SANTA ISABEL", "SUAREZ", "VALLE DE SAN JUAN", "VENADILLO", "VILLAHERMOSA", "VILLARRICA"]
DANE = ["73001", "73024", "73026", "73030", "73043", "73055", "73067", "73124", "73148", "73152", "73200", "73217", "73226", "73168", "73236", "73268", "73270", "73275", "73283", "73319", "73347", "73349", "73352", "73408", "73411", "73443", "73449", "73461", "73483", "73504", "73520", "73547", "73555", "73563", "73585", "73616", "73622", "73624", "73671", "73675", "73678", "73686", "73770", "73854", "73861", "73870", "73873"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Tolima_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=29&cod_mpio="+amazonas[munpo]
		

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