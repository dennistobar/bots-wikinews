# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import pywikibot
import datetime
import time
import os
import re
import requests

load_dotenv()

data = {}
convertion = {}

data["AUD"] = {'code': "AUD", 'cours': "1.430064846",
               'date': "4/12/2016", 'abreviation': "$ AUD", 'nom': "dollar australien"}
data["JPY"] = {'code': "JPY", 'cours': "121.0363269",
               'date': "4/12/2016", 'abreviation': "JPY", 'nom': "yen"}
data["USD"] = {'code': "USD", 'cours': "1.066399356",
               'date': "4/12/2016", 'abreviation': "$", 'nom': "dollar"}
data["GBP"] = {'code': "GBP", 'cours': "0.837903163",
               'date': "4/12/2016", 'abreviation': "GBP", 'nom': "livre sterling"}
data["CHF"] = {'code': "CHF", 'cours': "1.077863149",
               'date': "4/12/2016", 'abreviation': "Fr.", 'nom': "franc suisse"}
data["BRL"] = {'code': "BRL", 'cours': "3.707603961",
               'date': "4/12/2016", 'abreviation': "BRL", 'nom': u"réal (nouveau)"}
data["CNY"] = {'code': "CNY", 'cours': "7.342906045",
               'date': "4/12/2016", 'abreviation': "CNY", 'nom': "yuan renminbi"}
data["MXN"] = {'code': "MXN", 'cours': "21.99805915",
               'date': "4/12/2016", 'abreviation': "MXN", 'nom': "peso"}
data["HKD"] = {'code': "HKD", 'cours': "8.270726805",
               'date': "4/12/2016", 'abreviation': "HKD", 'nom': "dollar de Hong Kong"}
data["RUB"] = {'code': "RUB", 'cours': "68.08970551",
               'date': "4/12/2016", 'abreviation': "RUB", 'nom': "rouble russe"}
data["INR"] = {'code': "INR", 'cours': "72.53808379",
               'date': "4/12/2016", 'abreviation': "INR", 'nom': "roupie indienne"}
data["CAD"] = {'code': "CAD", 'cours': "1.417404704",
               'date': "4/12/2016", 'abreviation': "$C", 'nom': "dollar canadien"}

data["AED"] = {'code': "AED", 'cours': "3.916458307",
               'date': "4/12/2016", 'abreviation': "AED", 'nom': "dirham"}
data["AFN"] = {'code': "AFN", 'cours': "70.91555717",
               'date': "4/12/2016", 'abreviation': "AFN", 'nom': "afghani (nouvel)"}
data["ALL"] = {'code': "ALL", 'cours': "136.4714605",
               'date': "4/12/2016", 'abreviation': "ALL", 'nom': "lek"}
data["AMD"] = {'code': "AMD", 'cours': "512.6448304",
               'date': "4/12/2016", 'abreviation': "AMD", 'nom': "dram"}
data["ANG"] = {'code': "ANG", 'cours': "1.88752684",
               'date': "4/12/2016", 'abreviation': "ANG", 'nom': "florin"}
data["AOA"] = {'code': "AOA", 'cours': "176.0348127", 'date': "4/12/2016",
               'abreviation': "AOA", 'nom': u"kwanza (ajusté) (2000-)"}
data["ARS"] = {'code': "ARS", 'cours': "16.99627293",
               'date': "4/12/2016", 'abreviation': "ARS", 'nom': "peso (nouveau)"}
data["AWG"] = {'code': "AWG", 'cours': "1.908854847",
               'date': "4/12/2016", 'abreviation': "AWG", 'nom': "florin"}
data["AZN"] = {'code': "AZN", 'cours': "1.84849663",
               'date': "4/12/2016", 'abreviation': "AZN", 'nom': "manat (nouveau)"}
data["BAM"] = {'code': "BAM", 'cours': "1.95583", 'date': "4/12/2016",
               'abreviation': "BAM", 'nom': "mark convertible (ou marka)"}
data["BBD"] = {'code': "BBD", 'cours': "2.132798712", 'date': "4/12/2016",
               'abreviation': "BBD", 'nom': "dollar de la Barbade,"}
data["BDT"] = {'code': "BDT", 'cours': "84.74675811",
               'date': "4/12/2016", 'abreviation': "BDT", 'nom': "taka"}
data["BGN"] = {'code': "BGN", 'cours': "1.95714141",
               'date': "4/12/2016", 'abreviation': "BGN", 'nom': "lev (4e)"}
data["BHD"] = {'code': "BHD", 'cours': "0.401925904",
               'date': "4/12/2016", 'abreviation': "BHD", 'nom': "dinar"}
data["BIF"] = {'code': "BIF", 'cours': "1780.630999",
               'date': "4/12/2016", 'abreviation': "BIF", 'nom': "franc burundais"}
data["BMD"] = {'code': "BMD", 'cours': "1.066399356",
               'date': "4/12/2016", 'abreviation': "BMD", 'nom': "dollar des Bermudes"}
data["BND"] = {'code': "BND", 'cours': "1.513540606",
               'date': "4/12/2016", 'abreviation': "BND", 'nom': "dollar de Brunei"}
data["BOB"] = {'code': "BOB", 'cours': "7.315499724",
               'date': "4/12/2016", 'abreviation': "BOB", 'nom': "boliviano"}
data["BSD"] = {'code': "BSD", 'cours': "1.066399356",
               'date': "4/12/2016", 'abreviation': "BSD", 'nom': u"dollar bahaméen"}
data["BTN"] = {'code': "BTN", 'cours': "72.53808379",
               'date': "4/12/2016", 'abreviation': "BTN", 'nom': "ngultrum"}
data["BWP"] = {'code': "BWP", 'cours': "11.80951652",
               'date': "4/12/2016", 'abreviation': "BWP", 'nom': "pula"}
data["BYR"] = {'code': "BYR", 'cours': "",
               'date': "", 'abreviation': "BYR", 'nom': "rouble"}
data["BZD"] = {'code': "BZD", 'cours': "2.142218139",
               'date': "4/12/2016", 'abreviation': "BZD", 'nom': "dollar du Belize"}
data["CDF"] = {'code': "CDF", 'cours': "1071.731353",
               'date': "4/12/2016", 'abreviation': "CDF", 'nom': "franc congolais"}
data["CLP"] = {'code': "CLP", 'cours': "714.2742886",
               'date': "4/12/2016", 'abreviation': "CLP", 'nom': "peso"}
data["COP"] = {'code': "COP", 'cours': "3272.299744",
               'date': "4/12/2016", 'abreviation': "COP", 'nom': "peso"}
data["CRC"] = {'code': "CRC", 'cours': "581.3689186",
               'date': "4/12/2016", 'abreviation': "CRC", 'nom': "colon"}
data["CUC"] = {'code': "CUC", 'cours': "1.066399356",
               'date': "4/12/2016", 'abreviation': "CUC", 'nom': "peso convertible"}
data["CUP"] = {'code': "CUP", 'cours': "28.25958293",
               'date': "4/12/2016", 'abreviation': "CUP", 'nom': "peso"}
data["CVE"] = {'code': "CVE", 'cours': "110.3190101",
               'date': "4/12/2016", 'abreviation': "CVE", 'nom': "escudo"}
data["CZK"] = {'code': "CZK", 'cours': "27.04548726",
               'date': "4/12/2016", 'abreviation': "CZK", 'nom': u"couronne tchèque"}
data["DJF"] = {'code': "DJF", 'cours': "189.7124389",
               'date': "4/12/2016", 'abreviation': "DJF", 'nom': "franc"}
data["DKK"] = {'code': "DKK", 'cours': "7.437708948",
               'date': "4/12/2016", 'abreviation': "DKK", 'nom': "couronne danoise"}
data["DOP"] = {'code': "DOP", 'cours': "49.16100868",
               'date': "4/12/2016", 'abreviation': "DOP", 'nom': "peso"}
data["DZD"] = {'code': "DZD", 'cours': "117.8051381",
               'date': "4/12/2016", 'abreviation': "DZD", 'nom': "dinar"}
data["EGP"] = {'code': "EGP", 'cours': "18.98190772",
               'date': "4/12/2016", 'abreviation': "EGP", 'nom': "livre"}
data["ERN"] = {'code': "ERN", 'cours': "11.16519819",
               'date': "4/12/2016", 'abreviation': "ERN", 'nom': "nakfa"}
data["ETB"] = {'code': "ETB", 'cours': "23.99398551",
               'date': "4/12/2016", 'abreviation': "ETB", 'nom': "birr"}
data["FJD"] = {'code': "FJD", 'cours': "2.236346089",
               'date': "4/12/2016", 'abreviation': "FJD", 'nom': "dollar de Fidji"}
data["FKP"] = {'code': "FKP", 'cours': "0.837903163",
               'date': "4/12/2016", 'abreviation': "FKP", 'nom': "livre"}
data["GEL"] = {'code': "GEL", 'cours': "2.758348574",
               'date': "4/12/2016", 'abreviation': "GEL", 'nom': "lari"}
data["GHS"] = {'code': "GHS", 'cours': "4.56952124",
               'date': "4/12/2016", 'abreviation': "GHS", 'nom': "cedi"}
data["GIP"] = {'code': "GIP", 'cours': "0.837903163",
               'date': "4/12/2016", 'abreviation': "GIP", 'nom': "livre de Gibraltar"}
data["GMD"] = {'code': "GMD", 'cours': "46.12177214",
               'date': "4/12/2016", 'abreviation': "GMD", 'nom': "dalasi"}
data["GNF"] = {'code': "GNF", 'cours': "9741.558116",
               'date': "4/12/2016", 'abreviation': "GNF", 'nom': "franc"}
data["GTQ"] = {'code': "GTQ", 'cours': "8.028387636",
               'date': "4/12/2016", 'abreviation': "GTQ", 'nom': "quetzal"}
data["GYD"] = {'code': "GYD", 'cours': "216.6923459",
               'date': "4/12/2016", 'abreviation': "GYD", 'nom': "dollar guyanien"}
data["HNL"] = {'code': "HNL", 'cours': "24.92175295",
               'date': "4/12/2016", 'abreviation': "HNL", 'nom': "lempira"}
data["HRK"] = {'code': "HRK", 'cours': "7.530698975",
               'date': "4/12/2016", 'abreviation': "HRK", 'nom': "kuna"}
data["HTG"] = {'code': "HTG", 'cours': "70.93688157",
               'date': "4/12/2016", 'abreviation': "HTG", 'nom': "gourde"}
data["HUF"] = {'code': "HUF", 'cours': "313.2121548",
               'date': "4/12/2016", 'abreviation': "HUF", 'nom': "forint"}
data["IDR"] = {'code': "IDR", 'cours': "14347.65685", 'date': "4/12/2016",
               'abreviation': "IDR", 'nom': u"roupie indonésienne"}
data["ILS"] = {'code': "ILS", 'cours': "4.070179742",
               'date': "4/12/2016", 'abreviation': "ILS", 'nom': "shekel (nouveau)"}
data["IQD"] = {'code': "IQD", 'cours': "1238.089652",
               'date': "4/12/2016", 'abreviation': "IQD", 'nom': "dinar"}
data["IRR"] = {'code': "IRR", 'cours': "34263.4113",
               'date': "4/12/2016", 'abreviation': "IRR", 'nom': "rial"}
data["ISK"] = {'code': "ISK", 'cours': "118.8502082",
               'date': "4/12/2016", 'abreviation': "ISK", 'nom': "couronne islandaise"}
data["ITL"] = {'code': "ITL", 'cours': "",
               'date': "", 'abreviation': "ITL", 'nom': "lire"}
data["JMD"] = {'code': "JMD", 'cours': "137.4055635",
               'date': "4/12/2016", 'abreviation': "JMD", 'nom': u"dollar jamaïcain"}
data["JOD"] = {'code': "JOD", 'cours': "0.755543973",
               'date': "4/12/2016", 'abreviation': "JOD", 'nom': "dinar"}
data["KES"] = {'code': "KES", 'cours': "108.6767584",
               'date': "4/12/2016", 'abreviation': "KES", 'nom': u"shilling kényan"}
data["KGS"] = {'code': "KGS", 'cours': "73.65087412",
               'date': "4/12/2016", 'abreviation': "KGS", 'nom': "som"}
data["KHR"] = {'code': "KHR", 'cours': "4299.722203",
               'date': "4/12/2016", 'abreviation': "KHR", 'nom': "riel"}
data["KMF"] = {'code': "KMF", 'cours': "491.96775",
               'date': "4/12/2016", 'abreviation': "KMF", 'nom': "franc"}
data["KPW"] = {'code': "KPW", 'cours': "138.5056559",
               'date': "4/12/2016", 'abreviation': "KPW", 'nom': "won"}
data["KRW"] = {'code': "KRW", 'cours': "1246.140967",
               'date': "4/12/2016", 'abreviation': "KRW", 'nom': "won"}
data["KWD"] = {'code': "KWD", 'cours': "0.325198484",
               'date': "4/12/2016", 'abreviation': "KWD", 'nom': "dinar"}
data["KYD"] = {'code': "KYD", 'cours': "0.873882306", 'date': "4/12/2016",
               'abreviation': "KYD", 'nom': u"dollar des îles Caïmans"}
data["KZT"] = {'code': "KZT", 'cours': "360.2296894",
               'date': "4/12/2016", 'abreviation': "KZT", 'nom': "tenge"}
data["LAK"] = {'code': "LAK", 'cours': "8737.009923",
               'date': "4/12/2016", 'abreviation': "LAK", 'nom': "kip"}
data["LBP"] = {'code': "LBP", 'cours': "1610.796227",
               'date': "4/12/2016", 'abreviation': "LBP", 'nom': "livre"}
data["LKR"] = {'code': "LKR", 'cours': "158.200351",
               'date': "4/12/2016", 'abreviation': "LKR", 'nom': "roupie srilankaise"}
data["LRD"] = {'code': "LRD", 'cours': "99.70833978",
               'date': "4/12/2016", 'abreviation': "LRD", 'nom': u"dollar libérien"}
data["LSL"] = {'code': "LSL", 'cours': "14.72644191",
               'date': "4/12/2016", 'abreviation': "LSL", 'nom': "loti"}
data["LYD"] = {'code': "LYD", 'cours': "1.518019421",
               'date': "4/12/2016", 'abreviation': "LYD", 'nom': "dinar"}
data["MAD"] = {'code': "MAD", 'cours': "10.65866156",
               'date': "4/12/2016", 'abreviation': "MAD", 'nom': "dirham"}
data["MDL"] = {'code': "MDL", 'cours': "21.48794661",
               'date': "4/12/2016", 'abreviation': "MDL", 'nom': "leu"}
data["MGA"] = {'code': "MGA", 'cours': "3545.777858",
               'date': "4/12/2016", 'abreviation': "MGA", 'nom': "ariary"}
data["MKD"] = {'code': "MKD", 'cours': "61.34995364",
               'date': "4/12/2016", 'abreviation': "MKD", 'nom': "denar"}
data["MMK"] = {'code': "MMK", 'cours': "1405.514351",
               'date': "4/12/2016", 'abreviation': "MMK", 'nom': "kyat"}
data["MNT"] = {'code': "MNT", 'cours': "2625.475214",
               'date': "4/12/2016", 'abreviation': "MNT", 'nom': "tugrik"}
data["MOP"] = {'code': "MOP", 'cours': "8.518848609",
               'date': "4/12/2016", 'abreviation': "MOP", 'nom': "pataca"}
data["MRO"] = {'code': "MRO", 'cours': "378.5717713",
               'date': "4/12/2016", 'abreviation': "MRO", 'nom': "ouguiya"}
data["MUR"] = {'code': "MUR", 'cours': "38.33705684",
               'date': "4/12/2016", 'abreviation': "MUR", 'nom': "roupie mauricienne"}
data["MVR"] = {'code': "MVR", 'cours': "16.04931051",
               'date': "4/12/2016", 'abreviation': "MVR", 'nom': "rufiyaa"}
data["MWK"] = {'code': "MWK", 'cours': "763.8511712",
               'date': "4/12/2016", 'abreviation': "MWK", 'nom': "kwacha"}
data["MYR"] = {'code': "MYR", 'cours': "4.737479139",
               'date': "4/12/2016", 'abreviation': "MYR", 'nom': "ringgit"}
data["MZN"] = {'code': "MZN", 'cours': "78.87089539",
               'date': "4/12/2016", 'abreviation': "MZN", 'nom': "metical (nouveau)"}
data["NAD"] = {'code': "NAD", 'cours': "14.72644191",
               'date': "4/12/2016", 'abreviation': "NAD", 'nom': "dollar namibien"}
data["NGN"] = {'code': "NGN", 'cours': "337.5153961",
               'date': "4/12/2016", 'abreviation': "NGN", 'nom': "naira"}
data["NIO"] = {'code': "NIO", 'cours': "31.00022928",
               'date': "4/12/2016", 'abreviation': "NIO", 'nom': u"cordoba d’or"}
data["NOK"] = {'code': "NOK", 'cours': "8.987715079", 'date': "4/12/2016",
               'abreviation': "NOK", 'nom': u"couronne norvégienne"}
data["NPR"] = {'code': "NPR", 'cours': "116.290853",
               'date': "4/12/2016", 'abreviation': "NPR", 'nom': u"roupie népalaise"}
data["NZD"] = {'code': "NZD", 'cours': "1.493347369", 'date': "4/12/2016",
               'abreviation': "NZD", 'nom': u"dollar néo-zélandais"}
data["OMR"] = {'code': "OMR", 'cours': "0.410137207",
               'date': "4/12/2016", 'abreviation': "OMR", 'nom': "rial"}
data["PAB"] = {'code': "PAB", 'cours': "1.066399356",
               'date': "4/12/2016", 'abreviation': "PAB", 'nom': "balboa"}
data["PEN"] = {'code': "PEN", 'cours': "3.639621116",
               'date': "4/12/2016", 'abreviation': "PEN", 'nom': "sol (nouveau)"}
data["PGK"] = {'code': "PGK", 'cours': "3.385284755",
               'date': "4/12/2016", 'abreviation': "PGK", 'nom': "kina"}
data["PHP"] = {'code': "PHP", 'cours': "52.91473604",
               'date': "4/12/2016", 'abreviation': "PHP", 'nom': "peso"}
data["PKR"] = {'code': "PKR", 'cours': "111.8119725",
               'date': "4/12/2016", 'abreviation': "PKR", 'nom': "roupie pakistanaise"}
data["PLN"] = {'code': "PLN", 'cours': "4.483356172",
               'date': "4/12/2016", 'abreviation': "PLN", 'nom': u"złoty"}
data["PYG"] = {'code': "PYG", 'cours': "6222.440242",
               'date': "4/12/2016", 'abreviation': "PYG", 'nom': "guarani"}
data["QAR"] = {'code': "QAR", 'cours': "3.883293255",
               'date': "4/12/2016", 'abreviation': "QAR", 'nom': "rial"}
data["RON"] = {'code': "RON", 'cours': "4.510975915",
               'date': "4/12/2016", 'abreviation': "RON", 'nom': "leu (nouveau)"}
data["RSD"] = {'code': "RSD", 'cours': "122.5193699",
               'date': "4/12/2016", 'abreviation': "RSD", 'nom': "dinar"}
data["RWF"] = {'code': "RWF", 'cours': "874.4474718",
               'date': "4/12/2016", 'abreviation': "RWF", 'nom': "franc rwandais"}
data["SAR"] = {'code': "SAR", 'cours': "4.001396983",
               'date': "4/12/2016", 'abreviation': "SAR", 'nom': "riyal"}
data["SBD"] = {'code': "SBD", 'cours': "8.332284612",
               'date': "4/12/2016", 'abreviation': "SBD", 'nom': "dollar des Salomon"}
data["SCR"] = {'code': "SCR", 'cours': "14.26095874",
               'date': "4/12/2016", 'abreviation': "SCR", 'nom': "roupie seychelloise"}
data["SDG"] = {'code': "SDG", 'cours': "6.910801262",
               'date': "4/12/2016", 'abreviation': "SDG", 'nom': "livre"}
data["SEK"] = {'code': "SEK", 'cours': "9.79142295",
               'date': "4/12/2016", 'abreviation': "SEK", 'nom': u"couronne suédoise"}
data["SGD"] = {'code': "SGD", 'cours': "1.513540606",
               'date': "4/12/2016", 'abreviation': "SGD", 'nom': "dollar de Singapour"}
data["SHP"] = {'code': "SHP", 'cours': "0.837903163",
               'date': "4/12/2016", 'abreviation': "SHP", 'nom': "livre"}
data["SLL"] = {'code': "SLL", 'cours': "5904.653234",
               'date': "4/12/2016", 'abreviation': "SLL", 'nom': "leone"}
data["SOS"] = {'code': "SOS", 'cours': "615.3124284",
               'date': "4/12/2016", 'abreviation': "SOS", 'nom': "shilling somalien"}
data["SRD"] = {'code': "SRD", 'cours': "8.243267041",
               'date': "4/12/2016", 'abreviation': "SRD", 'nom': "dollar surinamien"}
data["SSP"] = {'code': "SSP", 'cours': "",
               'date': "", 'abreviation': "SSP", 'nom': "livre"}
data["STD"] = {'code': "STD", 'cours': "24900.42496",
               'date': "4/12/2016", 'abreviation': "STD", 'nom': "dobra"}
data["SYP"] = {'code': "SYP", 'cours': "227.4629826",
               'date': "4/12/2016", 'abreviation': "SYP", 'nom': "livre"}
data["SZL"] = {'code': "SZL", 'cours': "14.72644191",
               'date': "4/12/2016", 'abreviation': "SZL", 'nom': "lilangeni"}
data["THB"] = {'code': "THB", 'cours': "37.96381707",
               'date': "4/12/2016", 'abreviation': "THB", 'nom': "baht"}
data["TJS"] = {'code': "TJS", 'cours': "8.399281096",
               'date': "4/12/2016", 'abreviation': "TJS", 'nom': "somoni"}
data["TMT"] = {'code': "TMT", 'cours': "3.732397746",
               'date': "4/12/2016", 'abreviation': "TMT", 'nom': "manat (nouveau)"}
data["TND"] = {'code': "TND", 'cours': "2.462102814",
               'date': "4/12/2016", 'abreviation': "TND", 'nom': "dinar"}
data["TOP"] = {'code': "TOP", 'cours': "2.423634913",
               'date': "4/12/2016", 'abreviation': "TOP", 'nom': u"pa’anga"}
data["TRY"] = {'code': "TRY", 'cours': "3.754685492",
               'date': "4/12/2016", 'abreviation': "TRY", 'nom': "livre turque"}
data["TTD"] = {'code': "TTD", 'cours': "7.155539719", 'date': "4/12/2016",
               'abreviation': "TTD", 'nom': u"dollar de Trinité-et-Tobago"}
data["TWD"] = {'code': "TWD", 'cours': "34.02453785", 'date': "4/12/2016",
               'abreviation': "TWD", 'nom': u"nouveau dollar de Taïwan"}
data["TZS"] = {'code': "TZS", 'cours': "2319.418599",
               'date': "4/12/2016", 'abreviation': "TZS", 'nom': "shilling tanzanien"}
data["UAH"] = {'code': "UAH", 'cours': "27.69439054",
               'date': "4/12/2016", 'abreviation': "UAH", 'nom': "hryvnia"}
data["UGX"] = {'code': "UGX", 'cours': "3865.697665",
               'date': "4/12/2016", 'abreviation': "UGX", 'nom': "shilling ougandais"}
data["UYU"] = {'code': "UYU", 'cours': "30.84026945",
               'date': "4/12/2016", 'abreviation': "UYU", 'nom': "peso"}
data["UZS"] = {'code': "UZS", 'cours': "3401.813945",
               'date': "4/12/2016", 'abreviation': "UZS", 'nom': "sum"}
data["VEF"] = {'code': "VEF", 'cours': "10.63733398",
               'date': "4/12/2016", 'abreviation': "VEF", 'nom': u"bolívar fuerté"}
data["VND"] = {'code': "VND", 'cours': "24164.6094",
               'date': "4/12/2016", 'abreviation': "VND", 'nom': "dong"}
data["VUV"] = {'code': "VUV", 'cours': "114.7232447",
               'date': "4/12/2016", 'abreviation': "VUV", 'nom': "vatu"}
data["WST"] = {'code': "WST", 'cours': "2.785787148",
               'date': "4/12/2016", 'abreviation': "WST", 'nom': "tala"}
data["XAF"] = {'code': "XAF", 'cours': "655.957", 'date': "4/12/2016",
               'abreviation': "XAF", 'nom': "franc CFA (BCEAC)"}
data["XAG"] = {'code': "XAG", 'cours': "0.063741743", 'date': "4/12/2016",
               'abreviation': "XAG", 'nom': u"argent (libellé en onces)"}
data["XAU"] = {'code': "XAU", 'cours': "0.000905578", 'date': "4/12/2016",
               'abreviation': "XAU", 'nom': u"or (libellé en onces)"}
data["XCD"] = {'code': "XCD", 'cours': "2.879278312", 'date': "4/12/2016",
               'abreviation': "XCD", 'nom': u"dollar de la Caraïbe orientale"}
data["XDR"] = {'code': "XDR", 'cours': "0.786940853", 'date': "4/12/2016",
               'abreviation': "XDR", 'nom': u"droits de tirage spéciaux (DTS)"}
data["XOF"] = {'code': "XOF", 'cours': "655.957", 'date': "4/12/2016",
               'abreviation': "XOF", 'nom': "franc CFA (BCEAO)"}
data["XPD"] = {'code': "XPD", 'cours': "0.001431428", 'date': "4/12/2016",
               'abreviation': "XPD", 'nom': u"palladium (libellé en onces)"}
data["XPF"] = {'code': "XPF", 'cours': "119.3317422",
               'date': "4/12/2016", 'abreviation': "XPF", 'nom': "franc CFP (IEOM)"}
data["XPT"] = {'code': "XPT", 'cours': "0.001147808", 'date': "4/12/2016",
               'abreviation': "XPT", 'nom': u"platine (libellé en onces)"}
data["YER"] = {'code': "YER", 'cours': "266.599839",
               'date': "4/12/2016", 'abreviation': "YER", 'nom': "rial"}
data["ZAR"] = {'code': "ZAR", 'cours': "14.72644191", 'date': "4/12/2016",
               'abreviation': "ZAR", 'nom': u"rand (compte convertible)"}
data["ZMW"] = {'code': "ZMW", 'cours': "10.42938542",
               'date': "4/12/2016", 'abreviation': "ZMW", 'nom': "kwacha"}

today = datetime.datetime.utcnow().strftime("%d/%m/%Y")

currencies = list(data.keys())
currencies.sort()

order = ['code', 'cours', 'date', 'abreviation', 'nom']

pagina = pywikibot.Page(pywikibot.Site('fr', 'wikivoyage'), 'Module:Prix/Data')
texto = pagina.get()

m = re.match('(.*)-- BOT.*-- // BOT(.*)', texto,
             flags=re.MULTILINE | re.DOTALL)

final = []

while len(currencies):
    time.sleep(3)
    currencies_upd = currencies[0:2]
    del currencies[0:2]

    url = 'http://free.currencyconverterapi.com/api/v3/convert?q=%s&compact=ultra&apiKey=' + \
        os.getenv('api_key_rate')

    currencies_ask = ",".join(map(lambda y: 'EUR_'+y, currencies_upd))

    jsonurl = requests.get(url % currencies_ask)
    text = jsonurl.json()

    llaves = map(lambda x: x.replace('EUR_', ''), text.keys())
    for llave in llaves:
        try:
            print('>>>' + llave)
            chg = []
            data[llave]['cours'] = text['EUR_'+llave]
            data[llave]['date'] = today
            for el in order:
                value = str(data[llave][el]) if type(
                    data[llave][el]) is float else data[llave][el]
                value = str(value) if type(value) is int else value
                chg.append(el+u"=\""+value+u"\"")
            string = u"\tdata[\""+llave+u"\"] = {"
            string += u",".join(chg)
            string += u"}"
            final.append(string)
        except UnicodeDecodeError:
            print(value)


page = m.group(1)
page += u"-- BOT\n"
page += "\n".join(final)
page += u'\n-- // BOT'
page += m.group(2)

pagina.put(
    page, summary=u'Bot: Misé a jour [[:es:User Talk:Superzerocool|commentes]]')
