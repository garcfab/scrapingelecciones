#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup




# Vector de Amazonas
amazonas = ["001", "004", "007", "010", "013", "016", "019", "022", "025", "028", "031", "034", "035", "037", "039", "040", "043", "046", "049", "052", "055", "058", "061", "062", "064", "067", "070", "073", "076", "078", "079", "080", "082", "085", "088", "091", "094", "097", "100", "103", "106", "109", "112", "115", "117", "118", "121", "124", "127", "130", "133", "136", "139", "140", "142", "145", "148", "150", "151", "154", "157", "160", "163", "166", "168", "169", "170", "172", "175", "178", "181", "184", "187", "190", "191", "192", "193", "196", "199", "202", "205", "206", "208", "211", "214", "217", "218", "220", "223", "226", "227", "229", "230", "231", "232", "235", "237", "238", "241", "244", "247", "250", "253", "256", "259", "262", "265", "268", "270", "271", "274", "277", "280", "282", "283", "286", "289", "290", "291", "292", "293", "295", "298", "300", "301"]
munpos =  ["MEDELLIN", "ABEJORRAL", "ABRIAQUI", "ALEJANDRIA", "AMAGA", "AMALFI", "ANDES", "ANGELOPOLIS", "ANGOSTURA", "ANORI", "ANTIOQUIA", "ANZA", "APARTADO", "ARBOLETES", "ARGELIA", "ARMENIA", "BARBOSA", "BELMIRA", "BELLO", "BETANIA", "BETULIA", "BOLIVAR", "BURITICA", "BRICENO", "CACERES", "CAICEDO", "CALDAS", "CAMPAMENTO", "CANASGORDAS", "CARACOLI", "CARAMANTA", "CAREPA", "CARMEN DE VIBORAL", "CAROLINA", "CAUCASIA", "CISNEROS", "COCORNA", "CONCEPCION", "CONCORDIA", "COPACABANA", "CHIGORODO", "DABEIBA", "DON MATIAS", "EBEJICO", "EL BAGRE", "ENTRERRIOS", "ENVIGADO", "FREDONIA", "FRONTINO", "GIRALDO", "GIRARDOTA", "GOMEZ PLATA", "GRANADA", "GUADALUPE", "GUARNE", "GUATAPE", "HELICONIA", "HISPANIA", "ITAGUI", "ITUANGO", "JARDIN", "JERICO", "LA CEJA", "LA ESTRELLA", "PUERTO NARE-LA MAGDALENA", "LA UNION", "LA PINTADA", "LIBORINA", "MACEO", "MARINILLA", "MONTEBELLO", "MURINDO", "MUTATA", "NARINO", "NECHI", "NECOCLI", "OLAYA", "PENOL", "PEQUE", "PUEBLORRICO", "PUERTO BERRIO", "PUERTO TRIUNFO", "REMEDIOS", "RETIRO", "RIONEGRO", "SABANALARGA", "SABANETA", "SALGAR", "SAN ANDRES", "SAN CARLOS", "SAN FRANCISCO", "SAN JERONIMO", "SAN JOSE DE LA MONTANA", "SAN JUAN DE URABA", "SAN LUIS", "SAN PEDRO", "SAN PEDRO DE URABA", "SAN RAFAEL", "SAN ROQUE", "SAN VICENTE", "SANTA BARBARA", "SANTA ROSA DE OSOS", "SANTO DOMINGO", "SANTUARIO", "SEGOVIA", "SONSON", "SOPETRAN", "TAMESIS", "TARAZA", "TARSO", "TITIRIBI", "TOLEDO", "TURBO", "URAMITA", "URRAO", "VALDIVIA", "VALPARAISO", "VEGACHI", "VIGIA DEL FUERTE", "VENECIA", "YALI", "YARUMAL", "YOLOMBO", "YONDO-CASABE", "ZARAGOZA"]
DANE = ["5001", "5002", "5004", "5021", "5030", "5031", "5034", "5036", "5038", "5040", "5042", "5044", "5045", "5051", "5055", "5059", "5079", "5086", "5088", "5091", "5093", "5101", "5113", "5107", "5120", "5125", "5129", "5134", "5138", "5142", "5145", "5147", "5148", "5150", "5154", "5190", "5197", "5206", "5209", "5212", "5172", "5234", "5237", "5240", "5250", "5264", "5266", "5282", "5284", "5306", "5308", "5310", "5313", "5315", "5318", "5321", "5347", "5353", "5360", "5361", "5364", "5368", "5376", "5380", "5585", "5400", "5390", "5411", "5425", "5440", "5467", "5475", "5480", "5483", "5495", "5490", "5501", "5541", "5543", "5576", "5579", "5591", "5604", "5607", "5615", "5628", "5631", "5642", "5647", "5649", "5652", "5656", "5658", "5659", "5660", "5664", "5665", "5667", "5670", "5674", "5679", "5686", "5690", "5697", "5736", "5756", "5761", "5789", "5790", "5792", "5809", "5819", "5837", "5842", "5847", "5854", "5856", "5858", "5873", "5861", "5885", "5887", "5890", "5893", "5895"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Antioquia_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&cod_depto=01&num_com=99&cod_mpio="+amazonas[munpo]
	

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