#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "004", "007", "010", "013", "016", "019", "022", "025", "028", "031", "034", "036", "037", "038", "040", "043", "046", "049", "051", "052", "054", "055", "058", "061", "064", "067", "069", "070", "073", "076", "079", "082", "085", "088", "091", "093", "094", "097", "100"]
munpos =  ["CUCUTA", "ABREGO", "ARBOLEDAS", "BOCHALEMA", "BUCARASICA", "CACOTA", "CACHIRA", "CONVENCION", "CUCUTILLA", "CHINACOTA", "CHITAGA", "DURANIA", "EL TARRA", "EL CARMEN", "EL ZULIA", "GRAMALOTE", "HACARI", "HERRAN", "LABATECA", "LA ESPERANZA", "LA PLAYA", "LOS PATIOS", "LOURDES", "MUTISCUA", "OCANA", "PAMPLONA", "PAMPLONITA", "PUERTO SANTANDER", "RAGONVALIA", "SALAZAR", "SAN CALIXTO", "SAN CAYETANO", "SANTIAGO", "SARDINATA", "SILOS", "TEORAMA", "TIBU", "TOLEDO", "VILLA CARO", "VILLA DEL ROSARIO"]
DANE = ["54001", "54003", "54051", "54099", "54109", "54125", "54128", "54206", "54223", "54172", "54174", "54239", "54250", "54245", "54261", "54313", "54344", "54347", "54377", "54385", "54398", "54405", "54418", "54480", "54480", "54518", "54520", "54553", "54599", "54660", "54670", "54673", "54680", "54720", "54743", "54800", "54810", "54820", "54871", "54874"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('NteSantander_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=25&cod_mpio="+amazonas[munpo]
		

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