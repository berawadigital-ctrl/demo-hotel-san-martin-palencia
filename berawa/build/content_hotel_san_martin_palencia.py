# Contenido de la demo Hotel San Martín (Frómista, Palencia) (es/en/fr/de). Hechos de hotelsanmartin.es leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Habitaciones dobles','Suite y habitación adaptada'],'en':['Double rooms','Suite and accessible room'],'fr':['Chambres doubles','Suite et chambre adaptée'],'de':['Doppelzimmer','Suite und barrierefreies Zimmer']}
RD={
'es':['17 habitaciones dobles con baño completo, televisor, wifi gratuito, teléfono, hilo musical y calefacción individual.','Una suite y una habitación para personas con movilidad reducida, en un edificio sin barreras arquitectónicas.'],
'en':['17 double rooms with full bathroom, TV, free wifi, telephone, piped music and individual heating.','One suite and one room for guests with reduced mobility, in a building without architectural barriers.'],
'fr':['17 chambres doubles avec salle de bains complète, téléviseur, wifi gratuit, téléphone, musique d’ambiance et chauffage individuel.','Une suite et une chambre pour personnes à mobilité réduite, dans un bâtiment sans barrières architecturales.'],
'de':['17 Doppelzimmer mit komplettem Bad, Fernseher, kostenlosem WLAN, Telefon, Hintergrundmusik und individueller Heizung.','Eine Suite und ein Zimmer für Personen mit eingeschränkter Mobilität, in einem barrierefreien Gebäude.']}
ART={
'hero':('hills',5511,['#1c1e1a','#b88a4a','#efe2c4','#5d5a45','#3b3a2d','#191a16']),
'intro':('arches',5512,['#f3efe5','#fbf8f0','#86622f','#5b5440','#28261c']),
'r1':('columns',5521,['#efeadd','#ddb978','#86622f','#5b5440','#28261c']),
'r2':('arches',5522,['#1c1e1a','#c39553','#f1e5c9','#635f4a','#403e30','#1c1d18']),
'g1':('hills',5531,['#eae5d6','#efe0bf','#ddb978','#9a9474','#6e6a52','#454331']),
'g2':('waves',5532,['#1c1e1a','#b88a4a','#efe2c4','#5d5a45','#3b3a2d','#191a16']),
'g3':('columns',5533,['#f2eee4','#faf7ef','#86622f','#5b5440','#28261c']),
'g4':('skyline',5534,['#1c1e1a','#c39553','#f1e5c9','#635f4a','#403e30','#1c1d18'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel San Martín · Hotel familiar en Frómista, en el Camino de Santiago',see_rooms='Ver las habitaciones',hero_k='Frómista · Plaza San Martín, 7',hero_t='Hotel familiar junto a la iglesia de San Martín de Tours',hero_s='En Frómista (Palencia), en el Camino de Santiago, el Camino del Agua y el Camino de Hierro.',
 intro_t='Bienvenidos al Hotel San Martín',intro_p1='Un establecimiento de carácter familiar con 19 habitaciones: 1 suite, 1 para personas con movilidad reducida y 17 dobles.',
 intro_p2='Tiene restaurante, cafetería, terraza en verano y jardín interior con terraza para uso exclusivo del hotel. Al lado está la iglesia románica de San Martín, del siglo XI.',
 stats=['Junto a San Martín de Tours','19 habitaciones','Wifi gratuito','Se admiten animales bajo petición'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con baño completo, televisor, wifi gratuito, teléfono, hilo musical y calefacción individual.',
 svcs=['Restaurante y cafetería','Terraza (en verano) y jardín interior','Aparcamiento en el exterior','Parking interior para bicicletas','Edificio sin barreras arquitectónicas','Se admiten animales, bajo petición'],
 loc_p='Plaza San Martín, 7 · 34440 Frómista (Palencia). Teléfono: 979 810 000. Correo: info@hotelsanmartin.es.',
 chips=['¿Qué habitaciones tenéis?','¿Admitís mascotas?','¿Hay restaurante?','¿Cómo reservo?']),
'en':dict(title='Hotel San Martín · Family hotel in Frómista, on the Way of St James',see_rooms='See the rooms',hero_k='Frómista · Plaza San Martín, 7',hero_t='Family hotel next to the church of San Martín de Tours',hero_s='In Frómista (Palencia), on the Way of St James, the Water Way and the Iron Way.',
 intro_t='Welcome to Hotel San Martín',intro_p1='A family-run hotel with 19 rooms: 1 suite, 1 for guests with reduced mobility and 17 doubles.',
 intro_p2='It has a restaurant, café, a terrace in summer and an inner garden with terrace for hotel guests only. Next door stands the Romanesque church of San Martín, from the eleventh century.',
 stats=['Next to San Martín de Tours','19 rooms','Free wifi','Pets allowed on request'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with full bathroom, TV, free wifi, telephone, piped music and individual heating.',
 svcs=['Restaurant and café','Terrace (in summer) and inner garden','Outdoor parking area','Indoor bicycle parking','Building without architectural barriers','Pets allowed on request'],
 loc_p='Plaza San Martín, 7 · 34440 Frómista (Palencia). Phone: +34 979 810 000. Email: info@hotelsanmartin.es.',
 chips=['Which rooms do you have?','Do you allow pets?','Is there a restaurant?','How do I book?']),
'fr':dict(title='Hôtel San Martín · Hôtel familial à Frómista, sur le Chemin de Saint-Jacques',see_rooms='Voir les chambres',hero_k='Frómista · Plaza San Martín, 7',hero_t='Hôtel familial à côté de l’église San Martín de Tours',hero_s='À Frómista (Palencia), sur le Chemin de Saint-Jacques, le Chemin de l’Eau et le Chemin de Fer.',
 intro_t='Bienvenue à l’Hôtel San Martín',intro_p1='Un établissement familial de 19 chambres : 1 suite, 1 pour personnes à mobilité réduite et 17 doubles.',
 intro_p2='Il dispose d’un restaurant, d’une cafétéria, d’une terrasse en été et d’un jardin intérieur avec terrasse réservé aux clients. Juste à côté se dresse l’église romane de San Martín, du XIe siècle.',
 stats=['À côté de San Martín de Tours','19 chambres','Wifi gratuit','Animaux admis sur demande'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec salle de bains complète, téléviseur, wifi gratuit, téléphone, musique d’ambiance et chauffage individuel.',
 svcs=['Restaurant et cafétéria','Terrasse (en été) et jardin intérieur','Parking extérieur','Local à vélos intérieur','Bâtiment sans barrières architecturales','Animaux admis sur demande'],
 loc_p='Plaza San Martín, 7 · 34440 Frómista (Palencia). Téléphone : +34 979 810 000. E-mail : info@hotelsanmartin.es.',
 chips=['Quelles chambres avez-vous ?','Acceptez-vous les animaux ?','Y a-t-il un restaurant ?','Comment réserver ?']),
'de':dict(title='Hotel San Martín · Familienhotel in Frómista am Jakobsweg',see_rooms='Zimmer ansehen',hero_k='Frómista · Plaza San Martín, 7',hero_t='Familienhotel neben der Kirche San Martín de Tours',hero_s='In Frómista (Palencia), am Jakobsweg, am Wasserweg und am Eisenweg.',
 intro_t='Willkommen im Hotel San Martín',intro_p1='Ein familiengeführtes Haus mit 19 Zimmern: 1 Suite, 1 Zimmer für Personen mit eingeschränkter Mobilität und 17 Doppelzimmer.',
 intro_p2='Es gibt ein Restaurant, ein Café, eine Terrasse im Sommer und einen Innengarten mit Terrasse nur für Hotelgäste. Direkt daneben steht die romanische Kirche San Martín aus dem XI. Jahrhundert.',
 stats=['Neben San Martín de Tours','19 Zimmer','Kostenloses WLAN','Haustiere auf Anfrage'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit komplettem Bad, Fernseher, kostenlosem WLAN, Telefon, Hintergrundmusik und individueller Heizung.',
 svcs=['Restaurant und Café','Terrasse (im Sommer) und Innengarten','Parkplätze im Außenbereich','Fahrradraum im Haus','Barrierefreies Gebäude','Haustiere auf Anfrage erlaubt'],
 loc_p='Plaza San Martín, 7 · 34440 Frómista (Palencia). Telefon: +34 979 810 000. E-Mail: info@hotelsanmartin.es.',
 chips=['Welche Zimmer gibt es?','Sind Haustiere erlaubt?','Gibt es ein Restaurant?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='info@hotelsanmartin.es')
D=dict(name='Hotel San Martín',ac='#1c1e1a',ac2='#86622f',ac2_a11y='#6b4d22',book=BOOK,around=[],foot=FOOT,
 address='Plaza San Martín, 7 · 34440 Frómista (Palencia)',phones=['+34 979 810 000'],emails=['info@hotelsanmartin.es'],maps='Hotel San Martín, Plaza San Martín 7, 34440 Frómista, Palencia',t=T)
META=dict(repo='demo-hotel-san-martin-palencia',name='Hotel San Martín',legal_name='VIRGEN DEL OTERO SL, NIF B34145268 (aviso legal de su web)',registry_ids=['B34145268'],
 url='https://hotelsanmartin.es/',domain='hotelsanmartin.es',municipality='Frómista',province='Palencia',sector='hotel familiar de 19 habitaciones en Frómista, en el Camino de Santiago',
 read_at='2026-11-02T09:02:00+01:00',created_at='2026-11-02T09:01:00+01:00',built_at='2026-11-02T09:12:00+01:00',audit_date='2026-11-02T09:02:00+01:00',
 rating=dict(value=4.4,coincide=['web'],date='2026-10-29',url='https://www.google.com/maps/search/Hotel+San+Mart%C3%ADn+Palencia+Fr%C3%B3mista'),
 book=dict(mode='mail',url='mailto:info@hotelsanmartin.es',note='sin motor de reservas: su pagina de contacto dice «teléfono (979.810.000) o por email info@hotelsanmartin.es» y la de reservas (solo en ingles) es un formulario. Los botones Reservar abren un correo a info@hotelsanmartin.es y el telefono real 979 810 000 va en tel: (mismo criterio que Nastasi y Lupercas).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Admitís mascotas?','K03'),('¿Hay restaurante?','K04'),('¿Hay parking?','K05'),('¿Puedo guardar la bici?','K05'),('¿Está adaptado para silla de ruedas?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Qué ver en Frómista?','K09'),('¿Pasa el Camino de Santiago?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Do you allow pets?','K03'),('Is there a restaurant?','K04'),('Is there parking?','K05'),('Can I store my bike?','K05'),('Is it wheelchair accessible?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('What to see in Frómista?','K09'),('Is it on the Way of St James?','K10'),('What is your phone number?','K11'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Acceptez-vous les animaux ?','K03'),('Y a-t-il un restaurant ?','K04'),('Y a-t-il un parking ?','K05'),('Puis-je ranger mon vélo ?','K05'),('Est-ce accessible en fauteuil roulant ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Que voir à Frómista ?','K09'),('Est-ce sur le Chemin de Saint-Jacques ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Sind Haustiere erlaubt?','K03'),('Gibt es ein Restaurant?','K04'),('Gibt es einen Parkplatz?','K05'),('Kann ich mein Fahrrad abstellen?','K05'),('Ist das Hotel rollstuhlgerecht?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Was kann man in Frómista besichtigen?','K09'),('Liegt es am Jakobsweg?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
