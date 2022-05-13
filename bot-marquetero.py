# -*- coding: utf-8 -*-

import pywikibot
import requests
import datetime
import time
import os
import random
from bs4 import BeautifulSoup

idiomas = {
    # 'es': (u'Indicadores económicos/core', u'Actualizando Indices Bursátiles', u'¡Avisame si hay error', u'Plantilla:Indicadores económicos', u'{{uso de plantilla}}'),
    'en': (u'Stock Markets', u'Update Market Data', u'Comments (es.wikinews)', u'Template:Stock Market data', u'{{clear}}{{documentation}}'),
    'fr': (u'Market Data/core', u'Mise à jour Stock Index', u'Comments (es.wikinews)', u'Modèle:Market Data', u''),
    'tr': (u'MKB/çekirdek', u'Borsa verisi güncellemesi', u'Bir sorununuz olursa benimle irtibata geçin.', u'Şablon:MKB', u''),
    'eo': (u'akcimerkatoj', u'Updating market data', u'Comments (es.wikinews)', u'ŝablono:akcimerkataj datenoj', u''),
    'de': (u'Vorlage:Börsenindizes/core', u'Updating market data', u'Comments (es.wikinews)', u'Vorlage:Börsenindizes', u''),
    'ca': (u'Plantilla:Market Data/core', u'Updating market data', u'Comments (es.wikinews)', u'Plantilla:Market Data', ''),
    'zh': (u'Stock Markets/core', u'Updating market data', u'Comments (es.wikinews)', u'Template:Market Data', ''),
    'ar': (u'Market Data/core', u'Updating market data', u'Commens (es.wikinews)', u'Template:Market Data', '')
}

meses = {
    'es': (u'enero', u'febrero', u'marzo', u'abril', u'mayo', u'junio', u'julio', u'agosto', u'septiembre', u'octubre', u'noviembre', u'diciembre'),
    'en': (u'January', u'February', u'March', u'April', u'May', u'June', u'July', u'August', u'September', u'October', u'November', u'December'),
    'fr': (u'janvier', u'février', u'mars', u'avril', u'mai', u'juin', u'juillet', u'août', u'septembre', u'octobre', u'novembre', u'décembre'),
    'tr': (u'Ocak', u'Şubat', u'Mart', u'Nisan', u'Mayıs', u'Haziran', u'Temmuz', u'Ağustos', u'Eylül', u'Ekim', u'Kasım', u'Aralık'),
    'eo': (u'januaro', u'februaro', u'marto', u'aprilo', u'majo', u'junio', u'julio', u'aŭgusto', u'septembro', u'oktobro', u'novembro', u'decembro'),
    'de': (u'Januar', u'Februar', u'März', u'April', u'Mai', u'Juni', u'Juli', u'August', u'September', u'Oktober', u'November', u'Dezember'),
    'ca': (u'gener', u'febrer', u'març', u'abril', u'maig', u'juny', u'juliol', u'agost', u'setembre', u'octubre', u'novembre', u'desembre'),
    'ar': (u'يناير', u'فبراير', u'مارس', u'أبريل', u'مايو', u'يونيو', u'يوليو', u'أغسطس', u'سبتمبر', u'أكتوبر', u'نوفمبر', u'ديسمبر')
}

dias = {
    'es': (u'Lunes', u'Martes', u'Miércoles', u'Jueves', u'Viernes', u'Sábado', u'Domingo'),
    'en': (u'monday', u'tuesday', u'wednesday', u'thursday', u'friday', u'saturday', u'sunday'),
    'fr': (u'lundi', u'mardi', u'mercredi', u'jeudi', u'vendredi', u'samedi', u'dimanche'),
    'tr': (u'Pazartesi', u'Salı', u'Çarşamba', u'Perşembe', u'Cuma', u'Cumartesi', u'Pazar'),
    'eo': (u'lundo', u'mardo', u'merkredo', u'ĵaŭdo', u'vendredo', u'sabato', u'dimanĉo'),
    'de': (u'Montag', u'Dienstag', u'Mittwoch', u'Donnerstag', u'Freitag', u'Samstag', u'Sonntag'),
    'ca': (u'dilluns', u'dimarts', u'dimecres', u'dijous', u'divendres', u'dissabte', u'diumenge'),
    'ar': (u'الإثنين', u'الثلاثاء', u'الأربعاء', u'الخميس', u'الجمعة', u'السبت', u'الأحد')
}

params = {
    'es': (u'hora', u'fecha', u'explicaciones', u'país', u'align', u'width'),
    'en': (u'hour', u'date', u'extrainfo', u'country', u'align', u'width'),
    'fr': (u'heures', u'date', u'description', u'pays', u'align', u'width'),
    'tr': (u'saat', u'tarih', u'fazladanbilgi', u'ülke', u'hizala', u'genişlik'),
    'eo': (u'horo', u'dato', u'extrainfo', u'lando', u'align', u'width'),
    'de': (u'Stunde', u'Datum', u'Erläuterungen ', u'Staaten', u'Ausrichtung', u'Breite'),
    'ca': (u'hores', u'data', u'explicaciones', u'país', u'align', u'width'),
    'zh': (u'hour', u'date', u'extrainfo', u'country', u'align', u'width'),
    'ar': (u'heures', u'date', u'description', u'pays', u'align', u'width'),
}

cambios = {
    'es': (u'profit', u'loss', u'steady'),
    'tr': (u'kazanç', u'kayıp', u'sabit'),
    'de': (u'profit', u'loss', u'steady')
}


def reuters(fila):
    td = fila.findAll('td')
    if len(td) == 0:
        return None
    return {'val': td[3].string.strip('+-%() '), 'chg': td[4].string.strip('+-%() '), 'por': td[5].string.strip('+-%() '), 'ev': "0" if td[5].string.strip('%') == '--' else ("0" if eval(td[5].string.strip('%')) == 0 else ("+" if eval(td[5].string.strip('%')) > 0 else "-"))}


def bloomberg(fila):
    td = fila.findAll('td')
    if len(td) == 0:
        return None
    return {'val': td[0].string.strip('+-%() '), 'chg': td[1].string.strip('+-%() '), 'por': td[2].string.strip('+-%() '), 'ev': "0" if eval(td[3].string.strip('%')) == 0 else ("+" if eval(td[2].string.strip('%')) > 0 else "-")}


agents = ['Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
          'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36']

headers = {
    'User-Agent': agents[int(random.random() * 10 % 4)],
    'Referer': 'https://www.bloomberg.com/markets/'
}

time.sleep((random.random() * 10))

# Bloomberg
url = 'https://www.bloomberg.com/markets/stocks/'  # write the url here
session = requests.Session()
r = session.get(url, headers=headers)
data = r.text
soup = BeautifulSoup(data, "html.parser")
tablas = soup.find_all('table')
tablaAmerica = tablas[0].findAll('tr')
tablaEuropa = tablas[1].findAll('tr')
tablaAsia = tablas[2].findAll('tr')

indices = {
    'FTSE 100': (tablaEuropa, 2, 'bloomberg'),
    'DAX': (tablaEuropa, 3, 'bloomberg'),
    'CAC 40': (tablaEuropa, 4, 'bloomberg'),
    # 'SMI': (europas, 9, 'reuters'),
    # 'AEX': (europas, 17, 'reuters'),
    # 'BEL20': (europas, 18, 'reuters'),
    # 'MIBTel': (tablaEuropa, 6, 'bloomberg'),
    'IBEX 35': (tablaEuropa, 5, 'bloomberg'),
    # 'OMX Stockholm 30': (europas, 11, 'reuters'),
    # 'OBX Index': (europas, 14, 'reuters'),
    'Nasdaq': (tablaAmerica, 3, 'bloomberg'),
    'S&P 500': (tablaAmerica, 2, 'bloomberg'),
    # 'Merval': (suda, 0),
    # 'Bovespa': (tablaAmerica, 6, 'bloomberg'),
    'S&P TSX': (tablaAmerica, 5, 'bloomberg'),
    # 'IPC': (americas, 19, 'reuters'),
    # 'All Ordinaries': (asias, 8, 'reuters'),
    'Nikkei': (tablaAsia, 1, 'bloomberg'),
    'Hang Seng': (tablaAsia, 3, 'bloomberg'),
    # 'SSE Composite': (asias, 16, 'reuters'),
    # 'BSE Sensex': (asias, 17, 'reuters'),
    # 'IDX Composite': (asias, 13, 'reuters'),
    # 'ISE-100': (asias, 15, 'reuters')
}

ticker = ''
for indice in indices:
    buscar, lugar, pagina = indices[indice]

    try:
        if pagina == 'reuters':
            fila = reuters(buscar[lugar])
        elif pagina == 'bloomberg':
            fila = bloomberg(buscar[lugar])
    except:
        continue

    ticker += u'| ' + indice + ' = ' + fila['val'] + '\n'
    ticker += u'| ' + indice + '-c = ' + fila['chg'] + '\n'
    ticker += u'| ' + indice + '-p = ' + fila['por'] + '\n'
    ticker += u'| ' + indice + '-tl = {{' + fila['ev'] + '}}\n'

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
    elif idioma == 'ar':
        dia = dias[idioma][int(numDia) - 1] + ' ' + diaActual + \
            ' ' + meses[idioma][int(numMes) - 1] + ' ' + anyo
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
    elif idioma == 'zh':
        dia = '%s年%s月%s日' % (anyo, numMes, diaActual)
    else:
        dia = dias[idioma][int(numDia) - 1] + ' ' + diaActual + \
            ' de ' + meses[idioma][int(numMes) - 1] + ' de ' + anyo
    if idioma != 'es':
        base = ':es:'
    else:
        base = ''
    pywikibot.setAction(
        u'Bot: ' + idiomas[idioma][1] + ' [[' + base + 'User Talk:Superzerocool|' + idiomas[idioma][2] + ']]')

    ticker_lang = ticker

    try:
        ticker_lang = ticker_lang.replace(
            u'{{+}}', '{{' + cambios[idioma][0] + '}}')
        ticker_lang = ticker_lang.replace(
            u'{{-}}', '{{' + cambios[idioma][1] + '}}')
        ticker_lang = ticker_lang.replace(
            u'{{0}}', '{{' + cambios[idioma][2] + '}}')
    except:
        ticker_lang = ticker_lang.replace(
            u'{{+}}', '{{' + cambios['es'][0] + '}}')
        ticker_lang = ticker_lang.replace(
            u'{{-}}', '{{' + cambios['es'][1] + '}}')
        ticker_lang = ticker_lang.replace(
            u'{{0}}', '{{' + cambios['es'][2] + '}}')

    texto = u'{{' + idiomas[idioma][0] + '\n'
    texto = texto + u'| ' + params[idioma][1] + u' = ' + dia + u'\n'
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

    try:
        pagina = pywikibot.Page(pywikibot.Site(
            idioma, 'wikinews'), idiomas[idioma][3])
        pagina.put(texto)
    except:
        continue
