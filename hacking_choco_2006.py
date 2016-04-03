#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["004", "007", "010", "013", "016", "019", "022", "025", "029", "030", "031", "034", "037", "040", "043", "046", "049", "052", "055", "058", "061", "064", "067", "070", "072", "076", "079", "085", "088", "091", "094", "097", "100", "103", "106", "109", "112", "115", "118", "121", "124", "127", "128", "130", "132", "133", "136", "139", "142", "145", "148", "151", "154", "157", "160", "163", "166", "169", "172", "175", "178", "181", "184", "190", "193", "196", "198", "199", "202", "205", "208", "211", "214", "217", "218", "220", "223", "226", "229", "232", "235", "238", "239", "241", "244", "247", "250", "256", "259", "262", "265", "268", "271", "274", "277", "280", "283", "286", "289", "292", "295", "298", "301", "304", "307", "316", "318", "319", "322", "323", "325", "328", "331", "334", "337", "340"]
munpos =  ["AGUA DE DIOS", "ALBAN", "ANAPOIMA", "ANOLAIMA", "ARBELAEZ", "BELTRAN", "BITUIMA", "BOJACA", "CABRERA", "CACHIPAY", "CAJICA", "CAPARRAPI", "CAQUEZA", "CARMEN DE CARUPA", "COGUA", "COTA", "CUCUNUBA", "CHAGUANI", "CHIA", "CHIPAQUE", "CHOACHI", "CHOCONTA", "EL COLEGIO", "EL PEÑON", "EL ROSAL", "FACATATIVA", "FOMEQUE", "FOSCA", "FUNZA", "FUQUENE", "FUSAGASUGA", "GACHALA", "GACHANCIPA", "GACHETA", "GAMA", "GIRARDOT", "GUACHETA", "GUADUAS", "GUASCA", "GUATAQUI", "GUATAVITA", "GUAYABAL DE SIQUIMA", "GUAYABETAL", "GUTIERREZ", "GRANADA", "JERUSALEN", "JUNIN", "LA CALERA", "LA MESA", "LA PALMA", "LA PEÑA", "LA VEGA", "LENGUAZAQUE", "MACHETA", "MADRID", "MANTA", "MEDINA", "MOSQUERA", "NARIÑO", "NEMOCON", "NILO", "NIMAIMA", "NOCAIMA", "PACHO", "PAIME", "PANDI", "PARATEBUENO (LA NAGUAYA)", "PASCA", "PUERTO SALGAR", "PULI", "QUEBRADANEGRA", "QUETAME", "QUIPILE", "APULO", "RICAURTE", "SAN ANTONIO DEL TEQUENDAMA", "SAN BERNARDO", "SAN CAYETANO", "SAN FRANCISCO", "SAN JUAN DE RIOSECO", "SASAIMA", "SESQUILE", "SIBATE", "SILVANIA", "SIMIJACA", "SOACHA", "SOPO", "SUBACHOQUE", "SUESCA", "SUPATA", "SUSA", "SUTATAUSA", "TABIO", "TAUSA", "TENA", "TENJO", "TIBACUY", "TIBIRITA", "TOCAIMA", "TOCANCIPA", "TOPAIPI", "UBALA", "UBAQUE", "UBATE", "UNE", "UTICA", "VENECIA", "VERGARA", "VIANI", "VILLAGOMEZ", "VILLAPINZON", "VILLETA", "VIOTA", "YACOPI", "ZIPACON", "ZIPAQUIRA"]
DANE = ["25001", "25019", "25035", "25040", "25053", "25086", "25095", "25099", "25120", "25123", "25126", "25148", "25151", "25154", "25200", "25214", "25224", "25168", "25175", "25178", "25181", "25183", "25245", "25258", "25260", "25269", "25279", "25281", "25286", "25288", "25290", "25293", "25295", "25297", "25299", "25307", "25317", "25320", "25322", "25324", "25326", "25328", "25335", "25339", "5313", "25368", "25372", "25377", "25386", "25394", "25398", "19397", "25407", "25426", "25430", "25436", "25438", "25473", "25483", "25486", "25488", "25489", "25491", "25513", "25518", "25524", "25530", "25535", "25572", "25580", "25592", "25594", "25596", "25599", "25612", "25645", "25649", "25653", "5652", "25662", "25718", "25736", "25740", "25743", "25745", "25754", "25758", "25769", "25772", "25777", "25779", "25781", "25785", "25793", "25797", "25799", "25805", "25807", "25815", "25817", "25823", "25839", "25841", "25843", "25845", "25851", "5861", "25862", "25867", "25871", "25873", "25875", "25878", "25885", "25898", "25899"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Cundinamarca_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=15&cod_mpio="+amazonas[munpo]
	

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