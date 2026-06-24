import streamlit as st

stradario_lecce = {
    1: [
        "ARCO DI PRATO", "ARCO DI TRIONFO", "CORSO VITTORIO EMANUELE III", "CORTE ANGELO PATARNELLO",
        "CORTE ANTONIO DELLA FLORA", "CORTE CAPPELLA BARLIERA", "CORTE CASTROMEDIANO", "CORTE CONTE ACCARDO",
        "CORTE DE URSIS SABATINO", "CORTE DEGLI ADORNI", "CORTE DEGLI AIELLI", "CORTE DEGLI ANDRANO",
        "CORTE DEGLI ANNIBALDI", "CORTE DEGLI SPINOLA", "CORTE DEI BALDUINI", "CORTE DEI BARONI",
        "CORTE DEI BUCCARELLI", "CORTE DEI CARNESECCHI", "CORTE DEI CARRETTI TORRE", "CORTE DEI CICALA",
        "CORTE DEI CONDO'", "CORTE DEI CRETY", "CORTE DEI FALCONI", "CORTE DEI GENOVESI",
        "CORTE DEI GHOTI", "CORTE DEI GIORGI", "CORTE DEI GIUDICI", "CORTE DEI GIUGNI",
        "CORTE DEI GRAFFOGLIETTI", "CORTE DEI LEVANTO", "CORTE DEI LUBELLI", "CORTE DEI MALEPIERI",
        "CORTE DEI MARESGALLI", "CORTE DEI MEMOLI", "CORTE DEI MESAGNESI", "CORTE DEI MONTEFUSCOLI",
        "CORTE DEI MORICINO", "CORTE DEI MORISCO", "CORTE DEI MOROSINI BONAVENTURA", "CORTE DEI MUSCO",
        "CORTE DEI PANDOLFI", "CORTE DEI ROMITI", "CORTE DEI SAETTA", "CORTE DEI SALOMI",
        "CORTE DEI SYBARIS", "CORTE DEI TARALLI", "CORTE DEI TOLOMEI", "CORTE DEI ZIANI",
        "CORTE DEL TELEGRAFO AD ASTA", "CORTE DEL VERRIO", "CORTE DELL'IDUME", "CORTE DI CHIAROMONTE",
        "CORTE FLORIO", "CORTE GAETANO STELLA", "CORTE GILBERTO BRUNSWICH", "CORTE GIUSEPPE EUGENIO BALSAMO",
        "CORTE GUARINI", "CORTE INFANZIA MATERNITA'", "CORTE METTOLA", "CORTE MIALI",
        "CORTE NHOI", "CORTE PETTI", "CORTE PIER DI NEGRO", "CORTE ROBERTO VOLTURIO",
        "CORTE SAN BLASIO", "CORTE SAN CATALDO", "CORTE SAN LEUCIO", "CORTE SAN PIETRO GARZYA",
        "CORTE SANTA IRENE", "CORTE VINCENZO LICCI", "PIAZZA D'ITALIA", "PIAZZA DUOMO",
        "PIAZZA FILIPPO BOTTAZZI", "PIAZZA GIUSEPPE MAZZINI", "PIAZZA GIUSEPPE VERDI", "PIAZZA SS. ADDOLARATA",
        "PIAZZA SANTO ORONZO", "PIAZZA SCIPIONE DE' MONTI", "PIAZZA TANCREDI", "PIAZZA VITTORIO EMANUELE II",
        "PIAZZETTA ANTONIO PANZERA", "PIAZZETTA BONIFACIO IX", "PIAZZETTA CHIESA GRECA", "PIAZZETTA DEI PERUZZI",
        "PIAZZETTA DELLA STAMPA", "PIAZZETTA DUCA GIOVANNI D'ENGHEN", "PIAZZETTA FRANCESCO NICOLA DE PACE", "PIAZZETTA GABRIELE RICCARDI",
        "PIAZZETTA GIORGIO BAGLIVI", "PIAZZETTA GIOV. ANT. ORSINI DEL BALZO", "PIAZZETTA GIOVANNI DEI FIORENTINI", "PIAZZETTA GIULIO ANTONIO ACQUAVIVA",
        "PIAZZETTA INNOCENZO XII", "PIAZZETTA LONGOBARDI", "PIAZZETTA LUCIO EPULIONE", "PIAZZETTA MARIOTTO CORSO",
        "PIAZZETTA PAUL HARRYS", "PIAZZETTA REGINA MARIA", "PIAZZETTA SIGISMONDO CASTROMEDIANO", "VIA ABRAMO BALMES",
        "VIA ACHILLE COSTA", "VIA ACHILLE LARDUCCI", "VIA ALFONSO LAMARMORA", "VIA ANDREA MANTEGNA",
        "VIA ANT. COSTAN. CASETTI", "VIA ANTONIETTA DE PACE", "VIA ANTONIO GALATEO", "VIA ASCANIO GRANDI",
        "VIA BECCHERIE VECCHIE", "VIA BRACCIO MARTELLO", "VIA CARLO RUSSI", "VIA CASALE FORNELLO",
        "VIA CASANELLO", "VIA CESARE AUGUSTO LUCREZIO", "VIA CESARE BATTISTI", "VIA COLONNELLO COSTADURA",
        "VIA CONTE GAUFRIDO", "VIA CORRADO GIAQUINTO", "VIA COTA", "VIA D'AMELIO FRANCESCO ANTONIO",
        "VIA DASUMMO", "VIA DEI PERRONI", "VIA DEL DELFINO", "VIA DEL PARCO TORRE",
        "VIA DEL PITTACCIO", "VIA DEL TEATRO ROMANO", "VIA DELLA CARTAPESTA ARTE", "VIA DELLA SINAGOGA",
        "VIA DELLE BOMBARDE", "VIA DELLE GIRAVOLTE", "VIA DELLE NOCCHE RAFFAELLO MONSIGNORE", "VIA DIETRO LO OSPEDALE DEI PELLEGRINI",
        "VIA ERMENEGILDO PERSONE'", "VIA FABIO FILZI", "VIA FERRANTE LOFFREDA", "VIA FILIPPO BACILE",
        "VIA FILIPPO CORRIDONI", "VIA FRANCESCO BERNARDINI", "VIA FRANCESCO CASOTTI", "VIA FRANCESCO GUARINI",
        "VIA FRANCESCO PETRARCA", "VIA FRANCESCO RUBICHI", "VIA FRATELLI PELUSO", "VIA GAETANO BRUNETTI",
        "VIA GABRIELE D'ANNUNZIO", "VIA GIAC. ANT. FERRARI", "VIA GIACOMO ARDITI", "VIA GIACOMO MATTEOTTI",
        "VIA GIAMBATTISTA CRISPO", "VIA GIOV. ANDREA COPPOLA", "VIA GIOVANNI BOCCACCIO", "VIA GIOVANNI GENTILE",
        "VIA GIROLAMO BALDUINI", "VIA GIUS. MARIA ZUCCARO", "VIA GIUSEPPE DESA", "VIA GIUSEPPE GARIBALDI",
        "VIA GIUSEPPE MANTOVANO", "VIA GIUSEPPE PARINI", "VIA GIUSEPPE PISANELLI", "VIA GIUSEPPE ZANARDELLI",
        "VIA GOBETTI", "VIA GUALTIERO DI BRIENNE", "VIA GUGLIELMO IL MALO", "VIA GUGLIELMO MARCONI",
        "VIA GUGLIELMO OBERDAN", "VIA IDOMENEO", "VIA IMPERATORE ADRIANO", "VIA IMPERATORE AUGUSTO",
        "VIA ISABELLA CASTRIOTA", "VIA LAZIO", "VIA LIBORIO ROMANO", "VIA LUDOVICO MAREMONTI",
        "VIA LUIGI SCARAMBONE", "VIA LUIGI STURZO", "VIA MADONNA DEGLI STUDENTI", "VIA MAGGIORE GALLIANO",
        "VIA MAGGIORE TOSELLI", "VIA MALENNIO", "VIA MARCO BASSEO", "VIA MARIO BERNARDINI",
        "VIA MARINO BRANCACCIO", "VIA MATTEO DA LECCE", "VIA MATTEO RENATO IMBRIANI", "VIA MATTEO TAFURO",
        "VIA MICHELE DE PIETRO", "VIA NICOLA CATALDI", "VIA NICOLA SCHIAVONI", "VIA ORONZO TISO",
        "VIA PADOVANO BAX", "VIA PALAZZO DEI CONTI DI LECCE", "VIA PIETRO BELLI", "VIA POMPEO DE' RENZI",
        "VIA PORCIGLIANO", "VIA PRINCIPI DI SAVOIA", "VIA QUATTRO NOVEMBRE", "VIA QUINTO ENNIO",
        "VIA QUINTO FABIO BALBO", "VIA QUINTINO SELLA", "VIA REGINA ELENA", "VIA REGINA ISABELLA",
        "VIA RICHEL RUBICHI", "VIA ROBERTO DI BICCARI", "VIA S. LEONARDO CONSERVATORIO", "VIA SACRO REGIO CONSIGLIO",
        "VIA SALICE LIBORIO", "VIA SALVATORE GRANDE", "VIA SALVATORE TRINCHESE", "VIA SAN FRANCESCO ASSISI",
        "VIA SANTA MARIA DEL PARADISO", "VIA SANTA MARIA VETERANI", "VIA SANTA VENERA", "VIA SEPOLCRI MESSAPICI",
        "VIA SERAFINO ELMO", "VIA SINDACO MARANGIO", "VIA SS. GIACOMO E FILIPPO", "VIA TEMPLARI",
        "VIA TORQUATO TASSO", "VIA ULDERIGO BOTTI", "VIA VINCENZO BALSAMO", "VIA VITO FAZZI",
        "VIA VITO MARIO STAMPACCHIA", "VIA VITTORIO ALFIERI", "VIA XXV LUGLIO", "VIA XXIV MAGGIO",
        "VIALE DEL MARE", "VIALE DELLA UNIVERSITA'", "VIALE GALLIPOLI", "VIALE GIACOMO LEOPARDI",
        "VIALE JAPIGIA", "VIALE LO RE FRANCESCO", "VIALE MARCHE", "VIALE OTRANTO",
        "VIALE ROSSINI GIOACCHINO", "VICO ARCO DEI MILANESI", "VICO BOEMONDO", "VICO BONAVENTURA DEI MATTHEI",
        "VICO DEI FEDELE", "VICO DEI FIESCHI", "VICO DEI GUIDANI", "VICO DEI PALEOLI",
        "VICO DEI PENSINI", "VICO DELLA CAVALLERIZZA", "VICO LA BAGLIVA DIETRO", "VICO MONDO NUOVO",
        "VICO NOBILISSIMI DEI PROTO", "VICO SAN GIUSTO", "VICO SFERRACAVALLI", "VICO SOTTARRANEI",
        "VICO STORTO VECCHIA CARITA'", "VICO VERNAZZA"
    ],
    2: [
        "LARGO LUIGI TASSELLI", "LARGO SAN PIO X", "PIAZZA DANTE ALIGHERI", "PIAZZA DEI PARTIGIANI",
        "PIAZZA SAN GIOVANNI BATTISTA", "PIAZZA VINCENZO CARDARELLI", "PIAZZALE RUDIAE", "PIAZZETTA SAN VINCENZO DE' PAOLI",
        "VIA ABRUZZI", "VIA ADDA", "VIA ADIGE", "VIA ADRIATICA",
        "VIA ADUA", "VIA ALCIDE DE GASPERI", "VIA ALDO MORO", "VIA AMBA ALAGI",
        "VIA AMILCARE FOSCARINI", "VIA ANDREA PENNETTERA", "VIA ANDREA SOZZO", "VIA ANTONIO CECCHI",
        "VIA ANTONIO MANNARINO", "VIA ANTONIO PROFILO", "VIA ANTONIO ROSMINI", "VIA ANTONIO ZIMBALO",
        "VIA ARMANDO DIAZ", "VIA ARMANDO PEROTTI", "VIA ARNO", "VIA ASTI",
        "VIA AURELIANO DIMITRI", "VIA BALDASSARRE PAPADIA", "VIA BARTOLOMEO RAVENNA", "VIA BASENTO",
        "VIA BASILICATA", "VIA BATTAGLINI", "VIA BELLINZONA", "VIA BENEDETTO CROCE",
        "VIA BERNARDINO BONIFACIO", "VIA BERNARDINO BRACCIO", "VIA BERNARDINO PADRE REALINO", "VIA BRADANO",
        "VIA BRUNO CANTOBELLI", "VIA CAP. RITUCCI", "VIA CARLO DALLA CHIESA", "VIA CARLO MASSA",
        "VIA CARLO SALERNI", "VIA CASALE BAGNARA", "VIA CAVOUR", "VIA CECINA",
        "VIA CESARE ABBA", "VIA CESARE RAHO", "VIA CORRADO ALVARO", "VIA CORSICA",
        "VIA CORVAGLIA", "VIA COSIMO DE GIORGI", "VIA COSTANTINO DIMITRI", "VIA DALMAZIA",
        "VIA DALMAZIO BIRAGO", "VIA DEI BASILIANI", "VIA DEI FERRARI", "VIA DEI FIORI",
        "VIA DEI SALESIANI", "VIA DELL'ABATE ANTONIO", "VIA DEGLI SCARPARI", "VIA DIEGO PERSONE'",
        "VIA DOGALI", "VIA DOM. TOMMASO ALBANESE", "VIA DOMENICO DE ANGELIS", "VIA DON BOSCO",
        "VIA D'OTRANTO MARTIRI", "VIA DUCAS ORSINI", "VIA E.A. MARIO", "VIA EGIDIO REALE",
        "VIA EMAN. MARIA BUCCARELLI", "VIA EMILIA", "VIA ENRICO BOZZI", "VIA ENRICO DE NICOLA",
        "VIA ETTORE D'AMORE", "VIA EUGENIO MONTALE", "VIA FERRANTE CARACCIOLO", "VIA FIUME",
        "VIA FORTUNATO CESARI", "VIA FRANCESCO ANTONIO ASTORE", "VIA FRANCESCO CALASSO", "VIA FRANCESCO CILEA",
        "VIA FRANCESCO DE MURA", "VIA FRANCESCO D'ELIA", "VIA FRANCESCO POLI", "VIA FRANCESCO RIGLIACO",
        "VIA FRANCESCO SCARPA", "VIA FRANCESCO STORELLA", "VIA FRANCESCO TRINCHERA", "VIA GAETANO ARGENTO",
        "VIA GAETANO DELLA NOCE", "VIA GAETANO DONIZETTI", "VIA GAETANO SALVEMINI", "VIA GALILEO GALILEI",
        "VIA GARIGLIANO", "VIA GASPARE PAPATODERO", "VIA GIAN MARIA SCUPOLA", "VIA GIANCARLO LAZARI",
        "VIA GIAMBATTISTA DEL TUFO", "VIA GIORDANO BRUNO", "VIA GIOACCHINO ROSSINI", "VIA GIOV. LEON. MARUGI",
        "VIA GIOVANDOME. CATALANO", "VIA GIOVANNI DI CASTRI", "VIA GIOVANNI GUERRIERI", "VIA GIOVANNI NOCCO",
        "VIA GIOVANNI PRESTA", "VIA GIROLAMO MARCIANO'", "VIA GIUSEPPE BATTISTA", "VIA GIUSEPPE CHIRIATTI",
        "VIA GIUSEPPE CINO", "VIA GIUSEPPE GHEZZI", "VIA GIUSEPPE GRASSI", "VIA GIUSEPPE MAGGIO",
        "VIA GIUSEPPE PALAMA", "VIA GIUSEPPE SARAGAT", "VIA GIUSEPPE SARNO", "VIA GIUSEPPE ZIMBALO",
        "VIA GIUSTINO DE IACOBIS", "VIA GORIZIA", "VIA IGNAZIO CIAIA", "VIA INDIPENDENZA",
        "VIA ISIDORO CHIRULLI", "VIA ISONZO", "VIA LIRI", "VIA LIVIO ANDRONICO",
        "VIA LOMBARDIA", "VIA LUDOVICO PEPE", "VIA LUIGI CADORNA", "VIA LUIGI EINAUDI",
        "VIA LUIGI GUACCI", "VIA LUIGI PAPPACODA", "VIA MARIO DI LECCE", "VIA MARIO NACCI",
        "VIA MARTINO MARINOSCI", "VIA MASSAGLIA", "VIA MASSENZIO PICCINNI", "VIA MAURO MANIERI",
        "VIA MICHELANGELO BUONARROTI", "VIA MICHELE SAPONARO", "VIA MINCIO", "VIA MONTE GRAPPA",
        "VIA MONTE SABOTINO", "VIA MONTE SEI BUSI", "VIA MONTELLO", "VIA NICOLA ANDRIA",
        "VIA NICOLO' DA LEQUILE", "VIA NINO BIXIO", "VIA NIZZA", "VIA OFANTO",
        "VIA ORDINE DI VITTORIO VENETO", "VIA ORONZO DE DONNO", "VIA ORONZO GARGIULO", "VIA ORONZO MASSARI",
        "VIA ORONZO QUARTA", "VIA ORTIGARA", "VIA OSLAVIA", "VIA OTTAVIO SCALFO",
        "VIA PAOLO COLACI", "VIA PAOLO STOMEO", "VIA PASQUALE CAFARO", "VIA PASQUALE CECERE",
        "VIA PIEMONTE", "VIA PIERO BARGELLINI", "VIA PIETRO MARTI", "VIA PIETRO MIGALI",
        "VIA PITAGORA", "VIA PO", "VIA PORDENONE", "VIA POZZUOLO",
        "VIA QUINTO MARIO CORRADO", "VIA RAFFAELE RUBINI", "VIA RAFFAELLO SANZIO", "VIA REDIPUGLIA",
        "VIA RICCARDO BACCHELLI", "VIA RUDIAE", "VIA S. LIGUORI DELLE VITE", "VIA SAGRADO",
        "VIA SALVATOR ROSA", "VIA SALVATORE MARTINI", "VIA SAN CESARIO", "VIA SAN DOMENICO SAVIO",
        "VIA SAN GIOV. MARIA VIANNEY", "VIA SAN PIETRO IN LAMA", "VIA SANT'ELIA", "VIA SANTA MARIA DELL' IDRIA",
        "VIA SAVERIO MERCADANTE", "VIA SELE", "VIA SETTELACQUARE", "VIA SILVIO SPAVENTA",
        "VIA SPALATO", "VIA SUPERSTRADA", "VIA TIZIANO VECELLIO", "VIA TOMMASO TRAETTA",
        "VIA TRENTO", "VIA TRIESTE", "VIA UDINE", "VIA UMBRIA",
        "VIA VECCHIA CAVALLINO", "VIA VECCHIA SAN CESARIO", "VIA VESPASIANO GENUINO", "VIA VINCENZO AMPOLO",
        "VIA VINCENZO CEPOLLA", "VIA VINCENZO CIARDO", "VIA VINCENZO PERSANO", "VIA VINCENZO SABATO",
        "VIA VITO BERNARDINO", "VIA VITO FORNARI", "VIA VITTORIO BODINI", "VIA VITTORIO VENETO",
        "VIA VOLTURNO", "VIALE DELLA LIBERTA'", "VIALE DELLO STADIO", "VIALE SAN NICOLA"
    ],
    3: [
        "CONTRADA LAMA", "CORTE DEI PALMA", "CORTE DELLE ARMELLINE", "LOCALITA' CASA SIMINI",
        "LOCALITA' CASALABATE", "LOCALITA' MEZZAGRANDE PADOVA", "LOCALITA' MEZZAGRANDE PERUGIA", "LUNGOMARE MARINAI D'ITALIA",
        "PIAZZA DEL PALIO", "PIAZZA NAPOLI", "PIAZZA NICODEMO ARGENTO", "PIAZZA QUASIMODO",
        "PIAZZA SALERNO", "PIAZZALE ADRIANO", "PIAZZALE ARTURO TOSCANINI", "PIAZZALE ATTILIO ADAMO",
        "PIAZZALE BOLOGNA", "PIAZZALE CUNEO", "PIAZZALE MILANO", "PIAZZALE PISA",
        "PIAZZALE SIENA", "PIAZZETTA ALBERTI", "PIAZZETTA DUCA DI ATENE", "PIAZZETTA FORMOSO LUCE",
        "PIAZZETTA GIUSEPPE PELLEGRINO", "PIAZZETTA SCIPIONE DA SUMMA", "STRADA ADRIATICA SOLICARA", "STRADA ESTERNA ARNESANO",
        "STRADA ESTERNA CALIO'", "STRADA ESTERNA FRIGOLE MONTEGRAPPA", "STRADA ESTERNA GIAMMATTEO GRAPPA", "STRADA ESTERNA GIAMMATTEO T. RINALDA",
        "STRADA ESTERNA LEQUILE", "STRADA ESTERNA LEUCA", "STRADA ESTERNA PISELLO", "STRADA ESTERNA SAN CATALDO",
        "VIA ADRIANO BALBI", "VIA AGNESE BATTISTA", "VIA AGRI", "VIA AGRIGENTO",
        "VIA ALBERICO LONGO", "VIA ALBERTO MAGNAGHI", "VIA ALDO ESTRAFALLACES", "VIA ALDO MASCIULLO",
        "VIA ALDO PALAZZESCHI", "VIA ALESSANDRIA", "VIA ALESSANDRO MALASPINA", "VIA ALESSANDRO VOLTA",
        "VIA ALFONSO SOZY CARAFA", "VIA ALFREDO CATALANI", "VIA AMBROGIO CANTARINI", "VIA AMERIGO VESPUCCI",
        "VIA AMILCARE PONCHELLI", "VIA AMLETO POSO", "VIA ANCONA", "VIA ANDREA DORIA",
        "VIA ANDREA VIGNES", "VIA ANIENE", "VIA ANTONIO BORTONE", "VIA ANTONIO BRUNI",
        "VIA ANTONIO CARACCIO", "VIA ANTONIO D'ANDREA", "VIA ANTONIO MALASPINA", "VIA ANTONIO MEUCCI",
        "VIA ANTONIO PIGAFETTA", "VIA ANTONIO RENZO", "VIA ANTONIO SALANDRA", "VIA ANTONIO VIVALDI",
        "VIA ANTONIOTTO USODIMARE", "VIA ARCHIMEDE", "VIA AREZZO", "VIA ARGENTINA",
        "VIA ARNESANO", "VIA ARNESANO 1 TRAV SX", "VIA ARNESANO COOPERATIVA VIVALDI", "VIA ARNESANO TRAV IPPODROMO",
        "VIA ARRIGO BOITO", "VIA ASCOLI PICENO", "VIA ATTILIO BIASCO", "VIA AUSONIO",
        "VIA AVELLINO", "VIA BALDASSARRE PAPADIA", "VIA BARI", "VIA BARTOLOMEO DE RINALDIS",
        "VIA BARTOLO LONGO", "VIA BELICE", "VIA BELISARIO ACQUAVIVA", "VIA BELLUNO",
        "VIA BENEDETTO BRIN", "VIA BENEDETTO TORSELLO", "VIA BENEVENTO", "VIA BENIAMINO ROSSI",
        "VIA BERGAMO", "VIA BERING", "VIA BERNARDO VARENIO", "VIA BIFERNO",
        "VIA BIVIO MONTERONI", "VIA BIZAMANO", "VIA BOLZANO", "VIA BONAVENTURA MOROSINI",
        "VIA BORMIDA", "VIA BRUNO LUCREZI", "VIA CAGLIARI", "VIA CAIROLI",
        "VIA CALORE", "VIA CALTANISETTA", "VIA CALVANI", "VIA CAMILLO GIOVANNI PALMA",
        "VIA CAMPANIA", "VIA CAMPI", "VIA CAMPOBASSO", "VIA CAPITANO RIVABELLA",
        "VIA CARLO BARBIERI", "VIA CARLO PIAGGIA", "VIA CARLO PISACANE", "VIA CARLO PORTA",
        "VIA CARSO", "VIA CASERTA", "VIA CATANIA", "VIA CATANZARO",
        "VIA CATANZARO 1 TRAVERSA", "VIA CEFALONIA", "VIA CERRATE", "VIA CHIETI",
        "VIA CIMAROSA", "VIA CLAUDIO TOLOMEO", "VIA CLEMENTE ANTONACI", "VIA CLEMENTE REBORA",
        "VIA CONTE ROBERTO", "VIA COOPERATIVA TORRICELLI", "VIA CORRADO CAPECE", "VIA COSENZA",
        "VIA COSIMO BERTACCHI", "VIA CREMONA", "VIA CRISTOFORO NEGRI", "VIA CUNEO",
        "VIA CUOCO", "VIA D'ACQUISTO", "VIA D'ARAGONA", "VIA D'ARPE",
        "VIA D'ASTORE", "VIA DA CA' MOSTO", "VIA DAL POZZO TOSCANELLI", "VIA DANIELE",
        "VIA DE AGOSTINI", "VIA DE BLASI", "VIA DE PASCALIS", "VIA DE RINALDIS",
        "VIA DE ROMA", "VIA DE ROSIS", "VIA DE SIMONE", "VIA DEGLI ALBERICI",
        "VIA DEGLI INDONATORI", "VIA DEGLI OLITA", "VIA DEGLI OREFICI", "VIA DEGLI OROPELLAI",
        "VIA DEGLI STAMPACCHIA", "VIA DEI PITTORI BIANCHI", "VIA DEL RISORGIMENTO", "VIA DELLA REPUBBLICA",
        "VIA DELLA TECNICA", "VIA DELLA TRIGLIA", "VIA DELLA VEDOVA", "VIA DELLE BENEDETTINE",
        "VIA DELLE GINESTRE", "VIA DELLE SCIENZE", "VIA DELL'AGRICOLTURA", "VIA DELL'ARTIGIANATO",
        "VIA DELL'OCCHIATA", "VIA DELL' ULIVO SAN LIGORIO", "VIA DI GIACOMO", "VIA DI PALMA",
        "VIA DI TAFAGNANO", "VIA DI VASTE", "VIA DI VERETO", "VIA DIEGO VALERI",
        "VIA DINO BUZZATI", "VIA DONNO", "VIA DORIA", "VIA DORSO",
        "VIA DUBROVINIK", "VIA EBOLI", "VIA ELIA", "VIA EMANUELE ORFANO",
        "VIA EMANUELE PASSABY", "VIA EMILIO STASI PAOLO", "VIA ENNIO CARLINO", "VIA ENRICO LUPINACCI",
        "VIA EPANIMONDA VALENTINI", "VIA ERCOLE STASI", "VIA EREDIA", "VIA ERNESTO SIMINI",
        "VIA ERRIQUEZ", "VIA ESTERNA CALIO'", "VIA ESTERNA GIAMMATTEO", "VIA ESTERNA LO PAPA",
        "VIA ESTERNA MALECARNE", "VIA ESTERNA MONTERONI", "VIA ESTERNA NOVOLI", "VIA ESTERNA SURBO",
        "VIA ESTRAFALLACES", "VIA EUGENIO MACCAGNANI", "VIA EUIPPA", "VIA FALCO",
        "VIA FANULI", "VIA FEDELE ALBANESE", "VIA FELICE CAVALLOTTI", "VIA FERDINANDO MAGELLANO",
        "VIA FERECIDE SIRO", "VIA FERMI", "VIA FERNANDO MANNO", "VIA FERRANDI",
        "VIA FERRANDO", "VIA FERRARA", "VIA FILIPPO LIPPI", "VIA FILIPPO MURATORE",
        "VIA FILIPPO PORENA", "VIA FILIPPO SMALDONE", "VIA FIORE", "VIA FIORINI",
        "VIA FIRENZE", "VIA FLACCO", "VIA FLASCASSOVITTI", "VIA FLEMING",
        "VIA FLUMENDOSA", "VIA FOGAZZARO", "VIA FOGGIA", "VIA FONDONE",
        "VIA FONTANA", "VIA FORLANINI", "VIA FORLI'", "VIA FORTORE",
        "VIA FOSCOLO", "VIA FRANC. SAVERIO CANDIDO", "VIA FRANCESCO CAMASSA", "VIA FRANCESCO MARMOCCHI",
        "VIA FRANCESCO PASANISI", "VIA FRANCESCO PETRELLI", "VIA FRANCESCO PIZARRO", "VIA FRANCESCO RIBEZZO",
        "VIA FRANCO CASAVOLA", "VIA FREUD", "VIA FRIGOLE", "VIA FRIULI",
        "VIA FUORI LE MURA SANTO ORONZO", "VIA FULCIGNANO", "VIA GABRIELI", "VIA GAETANO CASATI",
        "VIA GAETANO MARTINEZ", "VIA GAETANO RUCCO", "VIA GAETANO STABILI", "VIA GAGLIARDO",
        "VIA GALATINO", "VIA GALLO", "VIA GASTALDI", "VIA GEMITO",
        "VIA GENOVA", "VIA GENTILE", "VIA GEREMIA RE", "VIA GESSI",
        "VIA GIAMMATTEO", "VIA GIAN MARIA SCUPOLA", "VIA GIANCANE", "VIA GIANMARIA TARANTINO",
        "VIA GIANSERIO STRAFELLA", "VIA GIACOMO BOVE", "VIA GIACOMO BRUCE", "VIA GIACOMO CARTIER",
        "VIA GIACOMO PUCCINI", "VIA GIDIULI", "VIA GIGLI", "VIA GIGLIOLI",
        "VIA GIOACCHINO TOMA", "VIA GIOACCHINO UNGARO", "VIA GIOIA", "VIA GIORDANO",
        "VIA GIORGIO VASARI", "VIA GIOTTO", "VIA GIOVENALE", "VIA GIOVANNI DA VERRAZZANO",
        "VIA GIOVANNI MAGINI", "VIA GIOVANNI MARINELLI", "VIA GIOVANNI MIANI", "VIA GIOVANNI PASCOLI",
        "VIA GIOVANNI VERGA", "VIA GIURGOLA", "VIA GIUSEPPE APRILE", "VIA GIUSEPPE CANDIDO",
        "VIA GIUSEPPE CASCIARO", "VIA GIUSEPPE CASTIGLIONE", "VIA GIUSEPPE MALECORE", "VIA GIUSEPPE MANFREDI",
        "VIA GIUSEPPE MANZO", "VIA GIUSEPPE MOSCATI", "VIA GIUSEPPE MOSCHETTINI", "VIA GIUSEPPE PALMIERI",
        "VIA GIUSEPPE PETRAGLIONE", "VIA GIUSEPPE RICCHIERI", "VIA GIUSEPPE SAPETO", "VIA GIUSEPPE SCARDIA",
        "VIA GIUSEPPE TARTINI", "VIA GIUSEPPE TRICARICO", "VIA GIUSEPPE UNGARETTI", "VIA GIUSTI",
        "VIA GOLDONI", "VIA GOZZANO", "VIA GREGORIO MESSERE", "VIA GRIMALDI",
        "VIA GROSSETO", "VIA GUARIGLIA", "VIA GUERRAZZI", "VIA GUGLIELMO BAFFIN",
        "VIA GUGLIELMO PAISIELLO", "VIA GUGLIELMOTTO D'OTRANTO", "VIA GUIDO CAVALCANTI", "VIA GUIDO PIOVENE",
        "VIA GUSTAVO STRAFFORELLO", "VIA IDELBRANDO PIZZETTI", "VIA II TRAVERSA ANDRIANI", "VIA IMPERIA",
        "VIA INDONATORI", "VIA INDRACCOLO", "VIA  DELL'INDUSTRIA", "VIA INFANTINO",
        "VIA ISARCO", "VIA ITACA", "VIA KEPLERO", "VIA LA LIZZA",
        "VIA LA SPEZIA", "VIA LANCILLOTTO MALOCELLO", "VIA LATINA", "VIA LENIO",
        "VIA LEONARDO PRATO", "VIA LEONCAVALLO", "VIA LEONE", "VIA LEONE PANCALDO",
        "VIA LEPANTO", "VIA LEQUILE", "VIA LEUCA", "VIA LIBERO BOVIO",
        "VIA LIGURIA", "VIA LIVENZA", "VIA LIVORNO", "VIA LORENZO PEROSI",
        "VIA LUCCA", "VIA LUCIO APULEIO", "VIA LUDOVICO ARIOSTO", "VIA LUIGI CARLUCCIO",
        "VIA LUIGI MAGGIULLI", "VIA LUIGI MARIANO", "VIA LUIGI MARTUCCI", "VIA LUIGI PASTEUR",
        "VIA LUIGI PIRANDELLO", "VIA LUIGI SCORRANO", "VIA LUIGI TINELLI", "VIA LUIGI VANVITELLI",
        "VIA LUISA AMALIA PALADINI", "VIA LUPIAE", "VIA MAESTRI DEL LAVORO", "VIA MALTA",
        "VIA MANFREDO CAMPERIO", "VIA MANGIONELLO", "VIA MANIFATTURA TABACCHI", "VIA MANTOVA",
        "VIA MARCO AURELIO", "VIA MARCO PACUVIO", "VIA MARCO POLO", "VIA MARGARITO DA BRINDISI",
        "VIA MARIA FRANCESCO PIAVE", "VIA MARIO MOSCARDINO", "VIA MASACCIO", "VIA MATERA",
        "VIA MATTEO RICCI", "VIA DELLE MEDAGLIE D'ORO", "VIA MERCATORE", "VIA MESSINA",
        "VIA METAURO", "VIA MICHELE MASSARI", "VIA MICHELE PALUMBO", "VIA MICHELE VITERBO",
        "VIA MICELLI", "VIA MOLISE", "VIA MONTERONI", "VIA MONTONE",
        "VIA MORELLI", "VIA MORI", "VIA NICCOLO' MACHIAVELLI", "VIA NICCOLO' TOMMASEO",
        "VIA NICOLA ARGENTIERI", "VIA NICOLA CAPUTI", "VIA NICOLA NACUCCHI", "VIA NICOLA VACCA",
        "VIA NICOLA VALLETTA", "VIA NICOLO' PAGANINI", "VIA NICOLOSO DA RECCO", "VIA NOVARA",
        "VIA NUORO", "VIA NUZZO BARBA", "VIA ODORICO DA PORDENONE", "VIA OGLIO",
        "VIA OMBRONE", "VIA ORONZO PARLANGELI", "VIA OTTORINO RESPIGHI", "VIA PACELLI",
        "VIA PALADINI", "VIA PALERMO", "VIA PANARO", "VIA PANTALEONE",
        "VIA PANTELLERIA", "VIA PAOLO REVELLI", "VIA PAOLO VERONESE", "VIA PAPINI",
        "VIA PARMA", "VIA PATRASSO", "VIA PAVIA", "VIA PELLEGRINO MATTEUCCI",
        "VIA PEREGRINO SCARDINO", "VIA PESARO", "VIA PESCARA", "VIA PIACENZA",
        "VIA PIAVE", "VIA PIETRO CAVALLO", "VIA PIETRO CAVOTI", "VIA PIETRO MICHELI",
        "VIA PIETRO PALUMBO", "VIA PIETRO VALZANI", "VIA PINTO", "VIA PIPPO VIGONI",
        "VIA PISTOIA", "VIA PORCIGLIANO", "VIA POTENZA", "VIA PRAZIO ANTINORI",
        "VIA PREMUDA", "VIA PRIMO UMBERTO", "VIA PROPERZIO", "VIA PUBLIO OVIDIO NASONE",
        "VIA PUGLIA", "VIA RAFFAELE D'ARPE", "VIA RAMONDELLO ORSINI", "VIA RAPOLLA",
        "VIA RENO", "VIA RICCIOTTO CANUDO", "VIA RIETI", "VIA ROBERTO ALMAGIA'",
        "VIA ROCCO SCOTELLARO", "VIA ROMA", "VIA ROSSI", "VIA ROVIGO",
        "VIA RUBICONE", "VIA SACCO", "VIA SALSO", "VIA SALVATORE PANAREO",
        "VIA SALVATORE RAELI", "VIA SAN CESARIO QUASIMODO", "VIA SAN LIGORIO", "VIA SAN MICHELE MONTE",
        "VIA SAN NICOLA", "VIA SAN SABINO", "VIA SANDALO", "VIA SANGRO",
        "VIA SARDEGNA", "VIA SASSARI", "VIA SCIPIONE AMMIRATO", "VIA SCRIVIA",
        "VIA SCUOLA ELEMENTARE", "VIA SEBASTIANO CABOTO", "VIA SEBASTIANO VENIERO", "VIA SECCHIA",
        "VIA SERRA BIANCA TRAVERSA", "VIA SESIA", "VIA SONDRIO", "VIA STANISLAO SIDOTI",
        "VIA STURA", "VIA TAGLIAMENTO", "VIA TANAGRO", "VIA TANARO",
        "VIA TARANTO", "VIA TARO", "VIA TEOCRITO", "VIA TERAMO",
        "VIA TERNI", "VIA TEVERE", "VIA TICINO", "VIA TIRSO",
        "VIA TITO MINNITI", "VIA TORINO", "VIA TORRE MOZZA", "VIA TOSCANA",
        "VIA TREBBIA", "VIA TRIFONE NUTRICATI", "VIA TRILUSSA", "VIA UGOLINO VIVALDI",
        "VIA UMBERTO NOBILE", "VIA UMBERTO SABA", "VIA URBINO", "VIA VALERIO CATULLO",
        "VIA VALONA", "VIA VARESE", "VIA VECCHIA CARMIANO", "VIA VECCHIA LIZZANELLO",
        "VIA VECCHIA SAN PIETRO IN LAMA", "VIA VECCHIA SURBO", "VIA VELINO", "VIA VENEZIA",
        "VIA VENOSA", "VIA VERCELLI", "VIA VERNOLE", "VIA VERONA",
        "VIA VICENZA", "VIA VINCENZO ANDRIANI", "VIA VIRGILIO", "VIA VITO CARLUCCIO",
        "VIA VITO RAGUSA", "VIA VITTORE BELLIO", "VIA VITTORIO BOTTEGO", "VIA VITTORIO PAGANO",
        "VIA VITTORIO PRIOLO", "VIA WOLFANG MOZART", "VIA XX SETTEMBRE", "VIA ZANTE",
        "VIALE DELLA LIBERTA'", "VIALE DON MINZONI", "VICINALE RAMANNO", "VICO DEI PALEOLI",
        "VICO DEI RAYNO'", "VICO DELLA SAPONEA", "VICO LEANDRO DEGLI ALBANESI", "VICO PANEVINO",
        "ZONA BELSITO", "ZONA INDUSTRIALE", "ZONA MACCHITELLI", "ZONA PAGLIARONE",
        "ZONA PAMPOLI"
    ]
}
st.subheader("Generalità")
via = st.text_input("Inserisci la via senza numero civico, nome completo").upper()
mq_tot = st.number_input("Inserire i mq(superficie calpestabile al netto delle pareti")


for k in stradario_lecce.keys():
    stradario_lecce[k] = [i.strip().replace(" ", "") for i in stradario_lecce[k]]

pulizia = lambda x : x.replace(" ", "").strip().upper()

can_min = 0.0
can_max = 0.0

if via and via.strip()!="":
    if all(pulizia(via) not in stradario_lecce[k] for k in stradario_lecce.keys()):
        st.warning("La via non è stata trovata")
    if pulizia(via) in stradario_lecce[1]:

        car1 = st.checkbox("Appartamenti dal 1° piano fuori terra")
        car2 = st.checkbox("Allacciamento gas metano")
        car3 = st.checkbox("Ascensore a partire dal 2° piano")
        car4 = st.checkbox("Autoclave")
        car5 = st.checkbox("Impianto elettrico interno adeguato alla legge n.37/08 (già n. 46/90)")
        car6 = st.checkbox("Riscaldamento autonomo o centralizzato")
        car7 = st.checkbox("Infissi interni ed esterni in buono stato")
        car8 = st.checkbox(
            "Servizi igienici completi (tazza, bidet, lavabo, doccia ovvero vasca da bagno) posti all'interno dell'alloggio.")
        condizioni = [car1, car2, car3, car4, car5, car6, car7, car8]
        counter = sum(con for con in condizioni if con == True)
        servizi_igienici = st.checkbox("Servizi igienici interni all'alloggio?")
        if counter >= 6 and servizi_igienici == True:
            can_min = 4.7
            can_max = 5.4
            st.success(f"Assegnata: SUB-FASCIA A")
        elif counter < 6 and counter >= 4 and servizi_igienici == True:
            can_min = 3.6
            can_max = 4.6
            st.info(f"Assegnata: SUB-FASCIA B")
        else:
            can_min = 1.8
            can_max = 3.5
            st.warning(f"Assegnata: SUB-FASCIA C")
    if pulizia(via) in stradario_lecce[2]:

        car1 = st.checkbox("Allacciamento al gas metano")
        car2 = st.checkbox("Ascensore a partire dal 3° piano")
        car3 = st.checkbox("Autoclave")
        car4 = st.checkbox("Verde condominiale")
        car5 = st.checkbox("Cortile in comune")
        car6 = st.checkbox(
            "Impianto elettrico interno adeguato alla legge n.37/08 (già n.46/90)")
        car7 = st.checkbox("Impianto di ricezione satellitare")
        car8 = st.checkbox("Riscaldamento centralizzato oppure autonomo")
        car9 = st.checkbox("Porta blindata")
        car10 = st.checkbox("Ripostiglio e/o Cantina")
        car11 = st.checkbox("Doppi servizi")
        car12 = st.checkbox("Impianto di condizionamento")
        car13 = st.checkbox("Infissi interni ed esterni in buono stato")
        car14 = st.checkbox("Posto auto")
        car15 = st.checkbox("2° Posto auto")
        car16 = st.checkbox("Attico")

        condizioni = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12, car13, car14, car15,
                      car16]
        counter = sum(con for con in condizioni if con == True)

        st.markdown("**Condizioni Speciali (Fascia A)**")

        zona_pregio = st.checkbox("Zona di pregio: immobili individuati nella zona due dell'allegato 1")
        immobile_A7 = st.checkbox("Immobili accatastati A/7")

        if (counter >= 9 or zona_pregio == True or immobile_A7 == True) and car6 == True:

            can_min = 4.70
            can_max = 5.40
            st.success(f"Assegnata: SUB-FASCIA A ")

        elif counter >= 6:

            can_min = 3.90
            can_max = 4.60
            st.info(f"Assegnata: SUB-FASCIA B ")

        else:
            can_min = 3.00
            can_max = 3.80
            st.warning(f"Assegnata: SUB-FASCIA C ")

    if pulizia(via) in stradario_lecce[3]:

        car1 = st.checkbox("Allacciamento al gas metano")
        car2 = st.checkbox("Ascensore a partire dal 3° piano")
        car3 = st.checkbox("Autoclave")
        car4 = st.checkbox("Verde esclusivo")
        car5 = st.checkbox("Verde condominiale e/o verde attrezzato")
        car6 = st.checkbox("Cortile in comune")
        car7 = st.checkbox("Impianto elettrico interno adeguato alla legge n.37/08 (già n. 46/90)")
        car8 = st.checkbox("Impianto di ricezione satellitare")
        car9 = st.checkbox("Impianti sportivi")
        car10 = st.checkbox("Riscaldamento centralizzato oppure autonomo")
        car11 = st.checkbox("Porta blindata")
        car12 = st.checkbox("Ripostiglio e/o cantina")
        car13 = st.checkbox("Doppi servizi")
        car14 = st.checkbox("Impianto di condizionamento")
        car15 = st.checkbox("Infissi interni ed esterni in buono stato")
        car16 = st.checkbox("1° Posto auto")
        car17 = st.checkbox("2° Posto auto")
        car18 = st.checkbox("Box auto")
        car19 = st.checkbox("Cassaforte")
        car20 = st.checkbox("Parquet")
        car21 = st.checkbox("Attico")

        condizioni = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10,
                      car11, car12, car13, car14, car15, car16, car17, car18, car19, car20, car21]

        counter = sum(con for con in condizioni if con == True)


        if counter >= 13:
            can_min = 3.90
            can_max = 4.30
            st.success(f"Assegnata: SUB-FASCIA A")

        elif counter >= 8:

            can_min = 3.20
            can_max = 3.80
            st.info(f"Assegnata: SUB-FASCIA B ")

        else:

            can_min = 2.40
            can_max = 3.20
            st.warning(f"Assegnata: SUB-FASCIA C")
        st.subheader("1. Accessori e pertinenze")

        if st.checkbox("Presenti balconi, terrazze ad uso esclusivo o cantine?"):
            mq_balconi = st.number_input("Inserire i mq (balconi, terrazze, cantine):")
            mq_tot += mq_balconi * 0.25

        if st.checkbox("Presente autorimessa singola?"):
            mq_autorimessa = st.number_input("Inserire i mq dell'autorimessa singola:")
            mq_tot += mq_autorimessa * 0.50

        if st.checkbox("Presente posto macchina in autorimesse di uso comune?"):
            mq_posto_comune = st.number_input("Inserire i mq del posto macchina (autorimessa comune):")
            mq_tot += mq_posto_comune * 0.20

        if st.checkbox("Presente posto macchina in spazi comuni?"):
            mq_posto_spazi = st.number_input("Inserire i mq del posto macchina (spazi comuni):")
            mq_tot += mq_posto_spazi * 0.15

        if st.checkbox("Presente superficie scoperta ad uso esclusivo (area verde o pavimentata non a livello)?"):
            mq_scoperta = st.number_input("Inserire i mq della superficie scoperta:")

            if mq_scoperta > 0:

                mq_scoperta_utile = min(mq_scoperta, 300.0)

                if mq_scoperta_utile <= mq_tot:
                    mq_tot += mq_scoperta_utile * 0.20
                else:
                    mq_tot += (mq_tot * 0.20) + ((mq_scoperta_utile - mq_tot) * 0.10)

        st.subheader("Altre superfici")

        if st.checkbox("Presenti vani con altezza utile compresa fra 1,00 e 1,70 metri?"):
            mq_vani_bassi = st.number_input("Inserire i mq dei vani (h 1,00 - 1,70 m):")
            mq_tot += mq_vani_bassi * 0.70

        if st.checkbox("Presenti soppalchi ed ammezzati con altezza utile superiore a 1,70 metri (con scala fissa)?"):
            mq_soppalchi = st.number_input("Inserire i mq dei soppalchi/ammezzati:")
            mq_tot += mq_soppalchi * 1.00

        moltiplicatore = 1.0

        if mq_tot > 115.0:
            moltiplicatore = 0.90


        elif mq_tot > 0 and mq_tot < 45.0:

            moltiplicatore = 1.25


        elif mq_tot >= 45.0 and mq_tot < 60.0:
            moltiplicatore = 1.20

        mq_tot = mq_tot * moltiplicatore

        can_finale_min = mq_tot * can_min
        can_finale_max = mq_tot * can_max
        ammobiliato = st.checkbox("Immobile totalmente immobiliato?", help="""Per immobile totalmente ammobiliato si intende quello dotato dei seguenti arredi:
            -Cucina
            -Pensili a muro oppure credenza
            -Frigorifero
            -Fornello
            -Tavolo con sedie
            -Scolapiatti e stoviglie
            -Camera da letto
            -Letto con materasso
            -Comodino
            -Armadio e/o guardaroba
            -Sedia
            -Camera — studio
            -Scrivania con sedia
            -Libreria
            -Soggiorno — tinello
            -Tavolo con sedie
            -Vetrinetta
            -Bagno arredato (mensole, specchio, e sedile)

            Tutte le camere devono essere provviste di idonea illuminazione elettrica.
            Per immobile parzialmente arredato si intende quello dotato di parte degli arredi innanzi indicati. Gli arredi del vano cucina, della camera da letto e del bagno devono essere sempre presenti.""")

        parz_ammobiliato = st.checkbox("Immobile parzialmente arredato?")

        if ammobiliato == True and parz_ammobiliato == False:
            can_finale_max = can_finale_max + can_finale_max * 0.2
            can_finale_min = can_finale_min + can_finale_min * 0.2
        if parz_ammobiliato == True and ammobiliato == False:
            can_max = can_finale_max * 0.08 + can_finale_max
            can_min = can_finale_min * 0.08 + can_finale_min

        lala = st.button("Stima il range")

        if lala:
            if ammobiliato == True and parz_ammobiliato == False:
                can_max = can_max + can_max * 0.2
                can_min = can_min + can_min * 0.2
            if parz_ammobiliato == True and ammobiliato == False:
                can_max = can_max * 0.08 + can_max
                can_min = can_min * 0.08 + can_min
            if parz_ammobiliato == True and ammobiliato == True:
                st.warning("Entrambe le opzioni di arredamento sono spuntate")
            st.success(f"Range di canone stimato: da {can_finale_min:.2f} € a {can_finale_max:.2f} €")

