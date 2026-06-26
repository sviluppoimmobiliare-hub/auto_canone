import streamlit as st


zone_bari = {
    "ZONA 1": "CITTA' VECCHIA",
    "ZONA 2": "MURAT",
    "ZONA 3": "LIBERTA'",
    "ZONA 4": "MADONNELLA",
    "ZONA 5": "JAPIGIA E SANT'ANNA",
    "ZONA 6": "SAN PAOLO",
    "ZONA 7": "STANIC",
    "ZONA 8": "SAN GIROLAMO - FESCA",
    "ZONA 9": "TORRE A MARE SAN GIORGIO",
    "ZONA 10": "CARRASSI - SAN PASQUALE",
    "ZONA 11": "POGGIOFRANCO - PICONE",
    "ZONA 12": "CARBONARA - CEGLIE - LOSETO",
    "ZONA 13": "SANTO SPIRITO - PALESE"
}

caratteristiche_comuni = [
    "Appartamenti dal 1º piano fuori terra",
    "Ingresso alloggio da piazza o da mare",
    "Balcone con vista su piazza o mare",
    "Allacciamento gas metano",
    "Impianto di condizionamento",
    "Secondo servizio igienico",
    "Spazi esterni ad uso esclusivo e/o condominiale",
    "Porta blindata",
    "Cantina o soffitta o giardino privato o terrazza a livello",
    "Posto auto di pertinenza e/o condominiale assegnato",
    "Box auto",
    "Ascensore",
    "Portierato",
    "Videosorveglianza condominiale o individuale",
    "Impianto fotovoltaico o pannelli solari produzione acqua calda",
    "Impianto citofono",
    "Impianto di videocitofono",
    "Impianto di autoclave",
    "Impianto elettrico interno adeguato ai sensi del D.M. 37/2008",
    "Attico",
    "Ripostiglio",
    "Parquet",
    "Postazione di ricarica veicoli elettrici nel box/posto auto o antenna satellitare",
    "Cucina abitabile di almeno 9 mq. con finestra",
    "Sistemi di sicurezza allarme",
    "Sistemi di domotica in almeno il 50% dell'unità immobiliare",
    "Riscaldamento autonomo o centralizzato o pompa di calore",
    "Infissi interni ed esterni in buono stato",
    "Cassaforte",
    "Doppio ingresso o cortile/giardino recintato"
]

lista_zone = list(zone_bari.values())
zona = st.selectbox("Selezionare la zona", lista_zone)
mq = st.number_input("Inserire i mq dell'immobile")
st.subheader("Selezionare le caratteristiche")
valori_checkbox = {}

for elemento in caratteristiche_comuni:
    valori_checkbox[elemento] = st.checkbox(label=elemento, value=False)

counter = list(valori_checkbox.values()).count(True)

if zona == "CITTA' VECCHIA":
    zona_pregio = st.checkbox("Zona di Pregio",
                              help="gli immobili con balcone su mare o su Piazza Mercantile – Piazza Ferrarese – Piazza Massari – Via Venezia")
    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")
    requisiti_pregio = (zona_pregio and valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and  valori_checkbox["Impianto elettrico interno adeguato ai sensi del D.M. 37/2008"])

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:
        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""
        if counter > 5 or requisiti_pregio:
            fascia_nativa = "A"
        elif counter > 3:
            fascia_nativa = "B"
        else:
            fascia_nativa = "C"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.26, 6.37
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"
                can_min, can_max = 5.26, 6.37

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"
                can_min, can_max = 5.26 * 1.10, 6.37 * 1.10

            else:
                if fascia_nativa == "B":
                    can_min, can_max = 4.38, 5.25
                else:
                    can_min, can_max = 2.18, 4.37

        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} MQ - Canone Massimo: {can_max:.2f} MQ")

if zona == "MURAT":
    zona_pregio = st.checkbox(
        "Zona di Pregio",
        help="Immobili con balcone e ingresso su via Sparano, C.so V. Emanuele, C.so Cavour, piazza Garibaldi, Piazza Umberto, piazza Moro"
    )
    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")
    requisiti_pregio = (zona_pregio and valori_checkbox["Impianto di autoclave"] and
                        valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and valori_checkbox[
                            "Impianto elettrico interno adeguato ai sensi del D.M. 37/2008"] and valori_checkbox["Ascensore"])

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if requisiti_pregio:
            fascia_nativa = "A"
        elif counter > 7:
            fascia_nativa = "A"
        elif counter >= 6:
            fascia_nativa = "B"
        elif counter >= 5:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 6.63, 8.20
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.63, 8.20

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.63 * 1.10, 8.20 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 5.38, 6.62
                else:  # Fascia C
                    can_min, can_max = 4.76, 5.37

        elif fascia_nativa == "D":
            can_min, can_max = 2.37, 4.75

        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")

if zona == "LIBERTA'":

    zona_pregio = st.checkbox(
        "Zona di Pregio",
        help="Zona Executive – zona contrada Barone"
    )
    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:
        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )

        fascia_nativa = ""

        if zona_pregio:
            fascia_nativa = "A"
        elif counter > 7:
            fascia_nativa = "A"
        elif counter >= 6:
            fascia_nativa = "B"
        elif counter >= 5:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":
            can_min, can_max = 5.13, 6.06
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:
            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"
                can_min, can_max = 5.13, 6.06

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.13 * 1.10, 6.06 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.51, 5.12
                else:
                    can_min, can_max = 4.11, 4.50

        elif fascia_nativa == "D":
            can_min, can_max = 3.88, 4.10


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")

if zona == "MADONNELLA":
    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )

        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 6:
            fascia_nativa = "B"
        elif counter >= 5:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":
            can_min, can_max = 6.01, 6.50
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:
            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.01, 6.50

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.01 * 1.10, 6.50 * 1.10

            else:
                if fascia_nativa == "B":
                    can_min, can_max = 5.31, 6.00
                else:
                    can_min, can_max = 4.41, 5.30

        elif fascia_nativa == "D":

            can_min, can_max = 3.41, 4.40

        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")

if zona == "JAPIGIA E SANT'ANNA":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter >= 8:
            fascia_nativa = "A"
        elif counter > 6:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"

        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.26, 6.00
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.26, 6.00

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.26 * 1.10, 6.00 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.81, 5.25
                else:
                    can_min, can_max = 3.51, 4.80

        elif fascia_nativa == "D":

            can_min, can_max = 3.00, 3.50


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")
if zona == "SAN PAOLO":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter > 6:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 4.94, 5.18
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 4.94, 5.18

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 4.94 * 1.10, 5.18 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.57, 4.93
                else:
                    can_min, can_max = 4.32, 4.56

        elif fascia_nativa == "D":

            can_min, can_max = 2.16, 4.31


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")
if zona == "STANIC":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.19, 5.50
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.19, 5.50

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.19 * 1.10, 5.50 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.91, 5.18
                else:
                    can_min, can_max = 4.31, 4.90

        elif fascia_nativa == "D":

            can_min, can_max = 2.16, 4.30


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")
if zona == "SAN GIROLAMO - FESCA":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.13, 6.00
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.13, 6.00

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.13 * 1.10, 6.00 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.51, 5.12
                else:
                    can_min, can_max = 3.88, 4.50

        elif fascia_nativa == "D":

            can_min, can_max = 1.93, 3.87


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")

if zona == "TORRE A MARE SAN GIORGIO":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        else:
            fascia_nativa = "C"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.51, 5.90
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.51, 5.90

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.51 * 1.10, 5.90 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.71, 5.50
                else:  # Fascia C
                    can_min, can_max = 3.70, 4.70


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")

if zona == "CARRASSI - SAN PASQUALE":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:  #
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        else:
            fascia_nativa = "C"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 7.01, 7.50
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 7.01, 7.50

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 7.01 * 1.10, 7.50 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 6.01, 7.00
                else:  # Fascia C
                    can_min, can_max = 5.50, 6.00


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")

if zona == "POGGIOFRANCO - PICONE":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 6.88, 7.50
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.88, 7.50

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 6.88 * 1.10, 7.50 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 6.26, 6.87
                else:
                    can_min, can_max = 5.61, 6.25

        elif fascia_nativa == "D":

            can_min, can_max = 5.00, 5.60


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")

if zona == "CARBONARA - CEGLIE - LOSETO":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        elif counter >= 6:
            fascia_nativa = "C"
        else:
            fascia_nativa = "D"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.26, 5.70
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.26, 5.70

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.26 * 1.10, 5.70 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 4.88, 5.25
                else:
                    can_min, can_max = 4.13, 4.87

        elif fascia_nativa == "D":

            can_min, can_max = 2.06, 4.12


        st.success(f"Assegnata: FASCIA {fascia_finale}")
        st.info(f"Canone Minimo: {can_min:.2f} €/MQ - Canone Massimo: {can_max:.2f} €/MQ")
if zona == "SANTO SPIRITO - PALESE":

    parzialmente_ammobiliato = st.checkbox("L'immobile è parzialmente ammobiliato?")
    totalmente_ammobiliato = st.checkbox("L'immobile è totalmente ammobiliato?")

    if totalmente_ammobiliato and parzialmente_ammobiliato:
        st.warning("L'immobile non può essere totalmente e parzialmente arredato allo stesso tempo")
    else:

        requisiti_arredo = (
                valori_checkbox["Impianto di autoclave"] and
                valori_checkbox["Riscaldamento autonomo o centralizzato o pompa di calore"] and
                valori_checkbox["Infissi interni ed esterni in buono stato"]
        )


        fascia_nativa = ""

        if counter > 7:
            fascia_nativa = "A"
        elif counter >= 7:
            fascia_nativa = "B"
        else:
            fascia_nativa = "C"


        fascia_finale = fascia_nativa
        can_min = 0.0
        can_max = 0.0

        if fascia_nativa == "A":

            can_min, can_max = 5.69, 6.12
            if parzialmente_ammobiliato:
                can_min *= 1.10
                can_max *= 1.10
            elif totalmente_ammobiliato:
                can_min *= 1.20
                can_max *= 1.20

        elif fascia_nativa in ["B", "C"]:

            if parzialmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.69, 6.12

            elif totalmente_ammobiliato and requisiti_arredo:
                fascia_finale = "A"

                can_min, can_max = 5.69 * 1.10, 6.12 * 1.10

            else:

                if fascia_nativa == "B":
                    can_min, can_max = 5.13, 5.68
                else:
                    can_min, can_max = 2.56, 5.12


        st.success(f"Assegnata: FASCIA {fascia_finale}")

stima = st.button("Stima canone")
if stima:
    can_finale_minimo = round(can_min*mq , 2)
    can_finale_massimo = round(can_max*mq , 2)
    st.success(f"Range stimato: minimo ->{can_finale_minimo} euro , massimo ->{can_finale_massimo} euro ")
