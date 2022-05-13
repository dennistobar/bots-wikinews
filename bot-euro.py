# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
import pywikibot
import datetime
import requests

load_dotenv()

idiomas = {
    # 'es': (u'Indicadores económicos/core', u'Actualizando Indices Bursátiles', u'¡Avisame si hay error', u'Plantilla:Indicadores económicos', u'{{uso de plantilla}}'),
    'fr': (u'Modèle:Exchange Rates/core ', u'Mise à Taux de Change ', u'Comments (es.wikinews)', u'Modèle:Exchange Rates', u''),
}

meses = {
    'es': (u'enero', u'febrero', u'marzo', u'abril', u'mayo', u'junio', u'julio', u'agosto', u'septiembre', u'octubre', u'noviembre', u'diciembre'),
    'en': (u'January', u'February', u'March', u'April', u'May', u'June', u'July', u'August', u'September', u'October', u'November', u'December'),
    'fr': (u'janvier', u'février', u'mars', u'avril', u'mai', u'juin', u'juillet', u'août', u'septembre', u'octobre', u'novembre', u'décembre'),
    'tr': (u'Ocak', u'Şubat', u'Mart', u'Nisan', u'Mayıs', u'Haziran', u'Temmuz', u'Ağustos', u'Eylül', u'Ekim', u'Kasım', u'Aralık'),
    'eo': (u'januaro', u'februaro', u'marto', u'aprilo', u'majo', u'junio', u'julio', u'aŭgusto', u'septembro', u'oktobro', u'novembro', u'decembro'),
    'de': (u'Januar', u'Februar', u'März', u'April', u'Mai', u'Juni', u'Juli', u'August', u'September', u'Oktober', u'November', u'Dezember'),
    'ca': (u'gener', u'febrer', u'març', u'abril', u'maig', u'juny', u'juliol', u'agost', u'setembre', u'octubre', u'novembre', u'desembre')
}

dias = {
    'es': (u'Lunes', u'Martes', u'Miércoles', u'Jueves', u'Viernes', u'Sábado', u'Domingo'),
    'en': (u'monday', u'tuesday', u'wednesday', u'thursday', u'friday', u'saturday', u'sunday'),
    'fr': (u'lundi', u'mardi', u'mercredi', u'jeudi', u'vendredi', u'samedi', u'dimanche'),
    'tr': (u'Pazartesi', u'Salı', u'Çarşamba', u'Perşembe', u'Cuma', u'Cumartesi', u'Pazar'),
    'eo': (u'lundo', u'mardo', u'merkredo', u'ĵaŭdo', u'vendredo', u'sabato', u'dimanĉo'),
    'de': (u'Montag', u'Dienstag', u'Mittwoch', u'Donnerstag', u'Freitag', u'Samstag', u'Sonntag'),
    'ca': (u'dilluns', u'dimarts', u'dimecres', u'dijous', u'divendres', u'dissabte', u'diumenge')
}

params = {
    'es': (u'hora', u'fecha', u'explicaciones', u'país', u'align', u'width'),
    'en': (u'hour', u'date', u'extrainfo', u'country', u'align', u'width'),
    'fr': (u'heures', u'date', u'description', u'pays', u'align', u'width'),
    'tr': (u'saat', u'tarih', u'fazladanbilgi', u'ülke', u'hizala', u'genişlik'),
    'eo': (u'horo', u'dato', u'extrainfo', u'lando', u'align', u'width'),
    'de': (u'Stunde', u'Datum', u'Erläuterungen ', u'Staaten', u'Ausrichtung', u'Breite'),
    'ca': (u'hores', u'data', u'explicaciones', u'país', u'align', u'width')
}

cambios = {
    'es': (u'profit', u'loss', u'steady'),
    'tr': (u'kazanç', u'kayıp', u'sabit'),
    'de': (u'profit', u'loss', u'steady')
}

rates = ['AUD', 'USD', 'JPY', 'GBP', 'CHF', 'BRL', 'CNY', 'MXN', 'HKD',
         'RUB', 'INR', 'CRC', 'ARS', 'CLP', 'BOB', 'COP', 'NIO', 'PEN', 'UYU']


url = 'https://api.apilayer.com/exchangerates_data/latest'

jsonurl = requests.get(
    url, headers={'apikey': os.getenv('api_key_euro')})
text = jsonurl.json().get('rates')

ticker = ''
for rate in rates:
    try:
        ticker += u'| ' + rate + ' = ' + str(text[rate]) + '\n'
    except KeyError:
        continue

t = datetime.datetime.utcnow()
hora = t.strftime("%H:%M")

numDia = t.strftime("%w")
numMes = t.strftime("%m")
anyo = t.strftime("%Y")
diaActual = t.strftime("%d")

ticker_final = ticker

for idioma in idiomas:

    ticker = ticker_final
    if idioma in ['fr', 'eo']:
        dia = dias[idioma][int(numDia) - 1] + ' ' + diaActual + \
            ' ' + meses[idioma][int(numMes) - 1] + ' ' + anyo
        ticker = ticker.replace(',', ' ').replace('.', ',')
    elif idioma == 'en':
        dia = dia = diaActual + ' ' + \
            meses[idioma][int(numMes) - 1] + ', ' + anyo
    elif idioma == 'tr':
        dia = dia = diaActual + ' ' + \
            meses[idioma][int(numMes) - 1] + ' ' + anyo
    elif idioma == 'de':
        dia = dia = diaActual + '. ' + \
            meses[idioma][int(numMes) - 1] + ' ' + anyo
    elif idioma == 'ca':
        dia = dias[idioma][int(numDia) - 1] + ' ' + diaActual + (' d\'' if int(numMes) in [
            3, 7, 9] else ' de ') + meses[idioma][int(numMes) - 1] + ' de ' + anyo
        ticker = ticker.replace(',', ' ').replace('.', ',')
    else:
        dia = dias[idioma][int(numDia) - 1] + ' ' + diaActual + \
            ' de ' + meses[idioma][int(numMes) - 1] + ' de ' + anyo
    if idioma != 'es':
        base = ':es:'
    else:
        base = ''

    ticker_lang = ticker

    texto = u'{{' + idiomas[idioma][0] + '\n'
    texto = texto + u'| ' + params[idioma][1] + ' = ' + dia + '\n'
    texto = texto + u'| ' + params[idioma][0] + '= ' + hora + '\n'
    texto = texto + u'| ' + params[idioma][2] + \
        '= {{{' + params[idioma][2] + '|}}}\n'
    texto = texto + u'| ' + params[idioma][4] + \
        ' = {{{' + params[idioma][4] + '}}}\n'
    texto = texto + u'| ' + \
        params[idioma][5] + '= {{{' + params[idioma][5] + \
        '|{{#if:{{{' + params[idioma][5] + '|}}}|50%|35%}}}}}}\n'
    texto = texto + u'| ' + params[idioma][3] + \
        '= {{{' + params[idioma][3] + '}}}\n'
    texto += ticker_lang
    texto = texto + u'}}<noinclude>' + idiomas[idioma][4] + '</noinclude>'

    pagina = pywikibot.Page(pywikibot.Site(
        idioma, 'wikinews'), idiomas[idioma][3])

    pagina.put(texto, summary=u'Bot: ' +
               idiomas[idioma][1] + ' [[' + base + 'User Talk:Superzerocool|' + idiomas[idioma][2] + ']]')
