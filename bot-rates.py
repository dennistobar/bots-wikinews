# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import pywikibot
import datetime
import os
import re
import requests

load_dotenv()

data = {}

data["AED"] = {'code': "AED", 'cours': "3.558257",
               'date': "29/09/2022", 'abreviation': "AED", 'nom': "dirham"}
data["AFN"] = {'code': "AFN", 'cours': "84.524076",
               'date': "29/09/2022", 'abreviation': "AFN", 'nom': "afghani (nouvel)"}
data["ALL"] = {'code': "ALL", 'cours': "116.222554",
               'date': "29/09/2022", 'abreviation': "ALL", 'nom': "lek"}
data["AMD"] = {'code': "AMD", 'cours': "392.245646",
               'date': "29/09/2022", 'abreviation': "AMD", 'nom': "dram"}
data["ANG"] = {'code': "ANG", 'cours': "1.724926",
               'date': "29/09/2022", 'abreviation': "ANG", 'nom': "florin"}
data["AOA"] = {'code': "AOA", 'cours': "419.340618", 'date': "29/09/2022",
               'abreviation': "AOA", 'nom': "kwanza (ajusté) (2000-)"}
data["ARS"] = {'code': "ARS", 'cours': "142.283222",
               'date': "29/09/2022", 'abreviation': "ARS", 'nom': "peso (nouveau)"}
data["AUD"] = {'code': "AUD", 'cours': "1.491962", 'date': "29/09/2022",
               'abreviation': "$ AUD'", 'nom': "dollar australien"}
data["AWG"] = {'code': "AWG", 'cours': "1.743755",
               'date': "29/09/2022", 'abreviation': "AWG", 'nom': "florin"}
data["AZN"] = {'code': "AZN", 'cours': "1.642095",
               'date': "29/09/2022", 'abreviation': "AZN", 'nom': "manat (nouveau)"}
data["BAM"] = {'code': "BAM", 'cours': "1.95525", 'date': "29/09/2022",
               'abreviation': "BAM", 'nom': "mark convertible (ou marka)"}
data["BBD"] = {'code': "BBD", 'cours': "1.932527", 'date': "29/09/2022",
               'abreviation': "BBD", 'nom': "dollar de la Barbade,"}
data["BDT"] = {'code': "BDT", 'cours': "98.131415",
               'date': "29/09/2022", 'abreviation': "BDT", 'nom': "taka"}
data["BGN"] = {'code': "BGN", 'cours': "1.955619",
               'date': "29/09/2022", 'abreviation': "BGN", 'nom': "lev (4e)"}
data["BHD"] = {'code': "BHD", 'cours': "0.365267",
               'date': "29/09/2022", 'abreviation': "BHD", 'nom': "dinar"}
data["BIF"] = {'code': "BIF", 'cours': "1976.984051",
               'date': "29/09/2022", 'abreviation': "BIF", 'nom': "franc burundais"}
data["BMD"] = {'code': "BMD", 'cours': "0.968753", 'date': "29/09/2022",
               'abreviation': "BMD", 'nom': "dollar des Bermudes"}
data["BND"] = {'code': "BND", 'cours': "1.384168",
               'date': "29/09/2022", 'abreviation': "BND", 'nom': "dollar de Brunei"}
data["BOB"] = {'code': "BOB", 'cours': "6.613772",
               'date': "29/09/2022", 'abreviation': "BOB", 'nom': "boliviano"}
data["BRL"] = {'code': "BRL", 'cours': "5.208308",
               'date': "29/09/2022", 'abreviation': "BRL", 'nom': "réal (nouveau)"}
data["BSD"] = {'code': "BSD", 'cours': "0.957092",
               'date': "29/09/2022", 'abreviation': "BSD", 'nom': "dollar bahaméen"}
data["BTN"] = {'code': "BTN", 'cours': "78.412739",
               'date': "29/09/2022", 'abreviation': "BTN", 'nom': "ngultrum"}
data["BWP"] = {'code': "BWP", 'cours': "12.830265",
               'date': "29/09/2022", 'abreviation': "BWP", 'nom': "pula"}
data["BYR"] = {'code': "BYR", 'cours': "18987.556369",
               'date': "29/09/2022", 'abreviation': "BYR", 'nom': "rouble"}
data["BZD"] = {'code': "BZD", 'cours': "1.929328",
               'date': "29/09/2022", 'abreviation': "BZD", 'nom': "dollar du Belize"}
data["CAD"] = {'code': "CAD", 'cours': "1.322055",
               'date': "29/09/2022", 'abreviation': "$C", 'nom': "dollar canadien"}
data["CDF"] = {'code': "CDF", 'cours': "1984.005586",
               'date': "29/09/2022", 'abreviation': "CDF", 'nom': "franc congolais"}
data["CHF"] = {'code': "CHF", 'cours': "0.947536",
               'date': "29/09/2022", 'abreviation': "Fr.", 'nom': "franc suisse"}
data["CLP"] = {'code': "CLP", 'cours': "926.641381",
               'date': "29/09/2022", 'abreviation': "CLP", 'nom': "peso"}
data["CNY"] = {'code': "CNY", 'cours': "6.957489",
               'date': "29/09/2022", 'abreviation': "CNY", 'nom': "yuan renminbi"}
data["COP"] = {'code': "COP", 'cours': "4349.710101",
               'date': "29/09/2022", 'abreviation': "COP", 'nom': "peso"}
data["CRC"] = {'code': "CRC", 'cours': "606.154088",
               'date': "29/09/2022", 'abreviation': "CRC", 'nom': "colon"}
data["CUC"] = {'code': "CUC", 'cours': "0.968753",
               'date': "29/09/2022", 'abreviation': "CUC", 'nom': "peso convertible"}
data["CUP"] = {'code': "CUP", 'cours': "25.671951",
               'date': "29/09/2022", 'abreviation': "CUP", 'nom': "peso"}
data["CVE"] = {'code': "CVE", 'cours': "110.231191",
               'date': "29/09/2022", 'abreviation': "CVE", 'nom': "escudo"}
data["CZK"] = {'code': "CZK", 'cours': "24.644302",
               'date': "29/09/2022", 'abreviation': "CZK", 'nom': "couronne tchèque"}
data["DJF"] = {'code': "DJF", 'cours': "170.3951",
               'date': "29/09/2022", 'abreviation': "DJF", 'nom': "franc"}
data["DKK"] = {'code': "DKK", 'cours': "7.436787",
               'date': "29/09/2022", 'abreviation': "DKK", 'nom': "couronne danoise"}
data["DOP"] = {'code': "DOP", 'cours': "51.010355",
               'date': "29/09/2022", 'abreviation': "DOP", 'nom': "peso"}
data["DZD"] = {'code': "DZD", 'cours': "137.91261",
               'date': "29/09/2022", 'abreviation': "DZD", 'nom': "dinar"}
data["EGP"] = {'code': "EGP", 'cours': "18.921721",
               'date': "29/09/2022", 'abreviation': "EGP", 'nom': "livre"}
data["ERN"] = {'code': "ERN", 'cours': "14.531293",
               'date': "29/09/2022", 'abreviation': "ERN", 'nom': "nakfa"}
data["ETB"] = {'code': "ETB", 'cours': "50.571311",
               'date': "29/09/2022", 'abreviation': "ETB", 'nom': "birr"}
data["FJD"] = {'code': "FJD", 'cours': "2.222464",
               'date': "29/09/2022", 'abreviation': "FJD", 'nom': "dollar de Fidji"}
data["FKP"] = {'code': "FKP", 'cours': "0.83758",
               'date': "29/09/2022", 'abreviation': "FKP", 'nom': "livre"}
data["GBP"] = {'code': "GBP", 'cours': "0.896092",
               'date': "29/09/2022", 'abreviation': "GBP", 'nom': "livre sterling"}
data["GEL"] = {'code': "GEL", 'cours': "2.741252",
               'date': "29/09/2022", 'abreviation': "GEL", 'nom': "lari"}
data["GHS"] = {'code': "GHS", 'cours': "9.906464",
               'date': "29/09/2022", 'abreviation': "GHS", 'nom': "cedi"}
data["GIP"] = {'code': "GIP", 'cours': "0.83758", 'date': "29/09/2022",
               'abreviation': "GIP", 'nom': "livre de Gibraltar"}
data["GMD"] = {'code': "GMD", 'cours': "53.639815",
               'date': "29/09/2022", 'abreviation': "GMD", 'nom': "dalasi"}
data["GNF"] = {'code': "GNF", 'cours': "8272.062894",
               'date': "29/09/2022", 'abreviation': "GNF", 'nom': "franc"}
data["GTQ"] = {'code': "GTQ", 'cours': "7.510119",
               'date': "29/09/2022", 'abreviation': "GTQ", 'nom': "quetzal"}
data["GYD"] = {'code': "GYD", 'cours': "200.250649",
               'date': "29/09/2022", 'abreviation': "GYD", 'nom': "dollar guyanien"}
data["HKD"] = {'code': "HKD", 'cours': "7.604405", 'date': "29/09/2022",
               'abreviation': "HKD", 'nom': "dollar de Hong Kong"}
data["HNL"] = {'code': "HNL", 'cours': "23.631996",
               'date': "29/09/2022", 'abreviation': "HNL", 'nom': "lempira"}
data["HRK"] = {'code': "HRK", 'cours': "7.526728",
               'date': "29/09/2022", 'abreviation': "HRK", 'nom': "kuna"}
data["HTG"] = {'code': "HTG", 'cours': "116.299533",
               'date': "29/09/2022", 'abreviation': "HTG", 'nom': "gourde"}
data["HUF"] = {'code': "HUF", 'cours': "413.991665",
               'date': "29/09/2022", 'abreviation': "HUF", 'nom': "forint"}
data["IDR"] = {'code': "IDR", 'cours': "14732.503112",
               'date': "29/09/2022", 'abreviation': "IDR", 'nom': "roupie indonésienne"}
data["ILS"] = {'code': "ILS", 'cours': "3.41792", 'date': "29/09/2022",
               'abreviation': "ILS", 'nom': "shekel (nouveau)"}
data["INR"] = {'code': "INR", 'cours': "78.988212",
               'date': "29/09/2022", 'abreviation': "INR", 'nom': "roupie indienne"}
data["IQD"] = {'code': "IQD", 'cours': "1396.961541",
               'date': "29/09/2022", 'abreviation': "IQD", 'nom': "dinar"}
data["IRR"] = {'code': "IRR", 'cours': "41026.684503",
               'date': "29/09/2022", 'abreviation': "IRR", 'nom': "rial"}
data["ISK"] = {'code': "ISK", 'cours': "140.110699", 'date': "29/09/2022",
               'abreviation': "ISK", 'nom': "couronne islandaise"}
data["ITL"] = {'code': "ITL", 'cours': "2010.491",
               'date': "29/09/2022", 'abreviation': "ITL", 'nom': "lire"}
data["JMD"] = {'code': "JMD", 'cours': "145.229208",
               'date': "29/09/2022", 'abreviation': "JMD", 'nom': "dollar jamaïcain"}
data["JOD"] = {'code': "JOD", 'cours': "0.686854",
               'date': "29/09/2022", 'abreviation': "JOD", 'nom': "dinar"}
data["JPY"] = {'code': "JPY", 'cours': "139.818154",
               'date': "29/09/2022", 'abreviation': "JPY", 'nom': "yen"}
data["KES"] = {'code': "KES", 'cours': "116.97658",
               'date': "29/09/2022", 'abreviation': "KES", 'nom': "shilling kényan"}
data["KGS"] = {'code': "KGS", 'cours': "77.758791",
               'date': "29/09/2022", 'abreviation': "KGS", 'nom': "som"}
data["KHR"] = {'code': "KHR", 'cours': "3943.634707",
               'date': "29/09/2022", 'abreviation': "KHR", 'nom': "riel"}
data["KMF"] = {'code': "KMF", 'cours': "493.871825",
               'date': "29/09/2022", 'abreviation': "KMF", 'nom': "franc"}
data["KPW"] = {'code': "KPW", 'cours': "871.877632",
               'date': "29/09/2022", 'abreviation': "KPW", 'nom': "won"}
data["KRW"] = {'code': "KRW", 'cours': "1387.956485",
               'date': "29/09/2022", 'abreviation': "KRW", 'nom': "won"}
data["KWD"] = {'code': "KWD", 'cours': "0.30071",
               'date': "29/09/2022", 'abreviation': "KWD", 'nom': "dinar"}
data["KYD"] = {'code': "KYD", 'cours': "0.797555", 'date': "29/09/2022",
               'abreviation': "KYD", 'nom': "dollar des îles Caïmans"}
data["KZT"] = {'code': "KZT", 'cours': "456.699927",
               'date': "29/09/2022", 'abreviation': "KZT", 'nom': "tenge"}
data["LAK"] = {'code': "LAK", 'cours': "15806.152131",
               'date': "29/09/2022", 'abreviation': "LAK", 'nom': "kip"}
data["LBP"] = {'code': "LBP", 'cours': "1447.156146",
               'date': "29/09/2022", 'abreviation': "LBP", 'nom': "livre"}
data["LKR"] = {'code': "LKR", 'cours': "348.397844",
               'date': "29/09/2022", 'abreviation': "LKR", 'nom': "roupie srilankaise"}
data["LRD"] = {'code': "LRD", 'cours': "148.727796",
               'date': "29/09/2022", 'abreviation': "LRD", 'nom': "dollar libérien"}
data["LSL"] = {'code': "LSL", 'cours': "17.273119",
               'date': "29/09/2022", 'abreviation': "LSL", 'nom': "loti"}
data["LYD"] = {'code': "LYD", 'cours': "4.830744",
               'date': "29/09/2022", 'abreviation': "LYD", 'nom': "dinar"}
data["MAD"] = {'code': "MAD", 'cours': "10.610746",
               'date': "29/09/2022", 'abreviation': "MAD", 'nom': "dirham"}
data["MDL"] = {'code': "MDL", 'cours': "18.712061",
               'date': "29/09/2022", 'abreviation': "MDL", 'nom': "leu"}
data["MGA"] = {'code': "MGA", 'cours': "4058.870368",
               'date': "29/09/2022", 'abreviation': "MGA", 'nom': "ariary"}
data["MKD"] = {'code': "MKD", 'cours': "61.596744",
               'date': "29/09/2022", 'abreviation': "MKD", 'nom': "denar"}
data["MMK"] = {'code': "MMK", 'cours': "2009.955609",
               'date': "29/09/2022", 'abreviation': "MMK", 'nom': "kyat"}
data["MNT"] = {'code': "MNT", 'cours': "3123.687515",
               'date': "29/09/2022", 'abreviation': "MNT", 'nom': "tugrik"}
data["MOP"] = {'code': "MOP", 'cours': "7.738726",
               'date': "29/09/2022", 'abreviation': "MOP", 'nom': "pataca"}
data["MRO"] = {'code': "MRO", 'cours': "345.84461",
               'date': "29/09/2022", 'abreviation': "MRO", 'nom': "ouguiya"}
data["MUR"] = {'code': "MUR", 'cours': "43.936049", 'date': "29/09/2022",
               'abreviation': "MUR", 'nom': "roupie mauricienne"}
data["MVR"] = {'code': "MVR", 'cours': "14.967288",
               'date': "29/09/2022", 'abreviation': "MVR", 'nom': "rufiyaa"}
data["MWK"] = {'code': "MWK", 'cours': "982.413334",
               'date': "29/09/2022", 'abreviation': "MWK", 'nom': "kwacha"}
data["MXN"] = {'code': "MXN", 'cours': "19.56532",
               'date': "29/09/2022", 'abreviation': "MXN", 'nom': "peso"}
data["MYR"] = {'code': "MYR", 'cours': "4.502277",
               'date': "29/09/2022", 'abreviation': "MYR", 'nom': "ringgit"}
data["MZN"] = {'code': "MZN", 'cours': "61.834998",
               'date': "29/09/2022", 'abreviation': "MZN", 'nom': "metical (nouveau)"}
data["NAD"] = {'code': "NAD", 'cours': "17.263702",
               'date': "29/09/2022", 'abreviation': "NAD", 'nom': "dollar namibien"}
data["NGN"] = {'code': "NGN", 'cours': "417.851642",
               'date': "29/09/2022", 'abreviation': "NGN", 'nom': "naira"}
data["NIO"] = {'code': "NIO", 'cours': "34.399449",
               'date': "29/09/2022", 'abreviation': "NIO", 'nom': "cordoba d’or"}
data["NOK"] = {'code': "NOK", 'cours': "10.387554", 'date': "29/09/2022",
               'abreviation': "NOK", 'nom': "couronne norvégienne"}
data["NPR"] = {'code': "NPR", 'cours': "125.434528",
               'date': "29/09/2022", 'abreviation': "NPR", 'nom': "roupie népalaise"}
data["NZD"] = {'code': "NZD", 'cours': "1.699522", 'date': "29/09/2022",
               'abreviation': "NZD", 'nom': "dollar néo-zélandais"}
data["OMR"] = {'code': "OMR", 'cours': "0.37296",
               'date': "29/09/2022", 'abreviation': "OMR", 'nom': "rial"}
data["PAB"] = {'code': "PAB", 'cours': "0.957106",
               'date': "29/09/2022", 'abreviation': "PAB", 'nom': "balboa"}
data["PEN"] = {'code': "PEN", 'cours': "3.78018",
               'date': "29/09/2022", 'abreviation': "PEN", 'nom': "sol (nouveau)"}
data["PGK"] = {'code': "PGK", 'cours': "3.372566",
               'date': "29/09/2022", 'abreviation': "PGK", 'nom': "kina"}
data["PHP"] = {'code': "PHP", 'cours': "57.088349",
               'date': "29/09/2022", 'abreviation': "PHP", 'nom': "peso"}
data["PKR"] = {'code': "PKR", 'cours': "221.812934", 'date': "29/09/2022",
               'abreviation': "PKR", 'nom': "roupie pakistanaise"}
data["PLN"] = {'code': "PLN", 'cours': "4.814244",
               'date': "29/09/2022", 'abreviation': "PLN", 'nom': "złoty"}
data["PYG"] = {'code': "PYG", 'cours': "6725.53309",
               'date': "29/09/2022", 'abreviation': "PYG", 'nom': "guarani"}
data["QAR"] = {'code': "QAR", 'cours': "3.527213",
               'date': "29/09/2022", 'abreviation': "QAR", 'nom': "rial"}
data["RON"] = {'code': "RON", 'cours': "4.947422",
               'date': "29/09/2022", 'abreviation': "RON", 'nom': "leu (nouveau)"}
data["RSD"] = {'code': "RSD", 'cours': "117.330516",
               'date': "29/09/2022", 'abreviation': "RSD", 'nom': "dinar"}
data["RUB"] = {'code': "RUB", 'cours': "56.089682",
               'date': "29/09/2022", 'abreviation': "RUB", 'nom': "rouble russe"}
data["RWF"] = {'code': "RWF", 'cours': "1013.073596",
               'date': "29/09/2022", 'abreviation': "RWF", 'nom': "franc rwandais"}
data["SAR"] = {'code': "SAR", 'cours': "3.648919",
               'date': "29/09/2022", 'abreviation': "SAR", 'nom': "riyal"}
data["SBD"] = {'code': "SBD", 'cours': "7.888998", 'date': "29/09/2022",
               'abreviation': "SBD", 'nom': "dollar des Salomon"}
data["SCR"] = {'code': "SCR", 'cours': "12.653939", 'date': "29/09/2022",
               'abreviation': "SCR", 'nom': "roupie seychelloise"}
data["SDG"] = {'code': "SDG", 'cours': "559.446374",
               'date': "29/09/2022", 'abreviation': "SDG", 'nom': "livre"}
data["SEK"] = {'code': "SEK", 'cours': "10.912691",
               'date': "29/09/2022", 'abreviation': "SEK", 'nom': "couronne suédoise"}
data["SGD"] = {'code': "SGD", 'cours': "1.393178", 'date': "29/09/2022",
               'abreviation': "SGD", 'nom': "dollar de Singapour"}
data["SHP"] = {'code': "SHP", 'cours': "1.334362",
               'date': "29/09/2022", 'abreviation': "SHP", 'nom': "livre"}
data["SLL"] = {'code': "SLL", 'cours': "15010.825676",
               'date': "29/09/2022", 'abreviation': "SLL", 'nom': "leone"}
data["SOS"] = {'code': "SOS", 'cours': "550.251813",
               'date': "29/09/2022", 'abreviation': "SOS", 'nom': "shilling somalien"}
data["SRD"] = {'code': "SRD", 'cours': "27.39294", 'date': "29/09/2022",
               'abreviation': "SRD", 'nom': "dollar surinamien"}
data["STD"] = {'code': "STD", 'cours': "20051.228629",
               'date': "29/09/2022", 'abreviation': "STD", 'nom': "dobra"}
data["SYP"] = {'code': "SYP", 'cours': "2434.020971",
               'date': "29/09/2022", 'abreviation': "SYP", 'nom': "livre"}
data["SZL"] = {'code': "SZL", 'cours': "17.271235",
               'date': "29/09/2022", 'abreviation': "SZL", 'nom': "lilangeni"}
data["THB"] = {'code': "THB", 'cours': "36.781122",
               'date': "29/09/2022", 'abreviation': "THB", 'nom': "baht"}
data["TJS"] = {'code': "TJS", 'cours': "9.405857",
               'date': "29/09/2022", 'abreviation': "TJS", 'nom': "somoni"}
data["TMT"] = {'code': "TMT", 'cours': "3.400323",
               'date': "29/09/2022", 'abreviation': "TMT", 'nom': "manat (nouveau)"}
data["TND"] = {'code': "TND", 'cours': "3.189619",
               'date': "29/09/2022", 'abreviation': "TND", 'nom': "dinar"}
data["TOP"] = {'code': "TOP", 'cours': "2.358721",
               'date': "29/09/2022", 'abreviation': "TOP", 'nom': "pa’anga"}
data["TRY"] = {'code': "TRY", 'cours': "17.950604",
               'date': "29/09/2022", 'abreviation': "TRY", 'nom': "livre turque"}
data["TTD"] = {'code': "TTD", 'cours': "6.496707", 'date': "29/09/2022",
               'abreviation': "TTD", 'nom': "dollar de Trinité-et-Tobago"}
data["TWD"] = {'code': "TWD", 'cours': "30.803245", 'date': "29/09/2022",
               'abreviation': "TWD", 'nom': "nouveau dollar de Taïwan"}
data["TZS"] = {'code': "TZS", 'cours': "2257.194206",
               'date': "29/09/2022", 'abreviation': "TZS", 'nom': "shilling tanzanien"}
data["UAH"] = {'code': "UAH", 'cours': "35.175204",
               'date': "29/09/2022", 'abreviation': "UAH", 'nom': "hryvnia"}
data["UGX"] = {'code': "UGX", 'cours': "3709.90044",
               'date': "29/09/2022", 'abreviation': "UGX", 'nom': "shilling ougandais"}
data["USD"] = {'code': "USD", 'cours': "0.968753",
               'date': "29/09/2022", 'abreviation': "$", 'nom': "dollar"}
data["UYU"] = {'code': "UYU", 'cours': "39.437046",
               'date': "29/09/2022", 'abreviation': "UYU", 'nom': "peso"}
data["UZS"] = {'code': "UZS", 'cours': "10552.353511",
               'date': "29/09/2022", 'abreviation': "UZS", 'nom': "sum"}
data["VEF"] = {'code': "VEF", 'cours': "217805073818.5945",
               'date': "29/09/2022", 'abreviation': "VEF", 'nom': "bolívar fuerté"}
data["VND"] = {'code': "VND", 'cours': "22998.193276",
               'date': "29/09/2022", 'abreviation': "VND", 'nom': "dong"}
data["VUV"] = {'code': "VUV", 'cours': "115.24466",
               'date': "29/09/2022", 'abreviation': "VUV", 'nom': "vatu"}
data["WST"] = {'code': "WST", 'cours': "2.640412",
               'date': "29/09/2022", 'abreviation': "WST", 'nom': "tala"}
data["XAF"] = {'code': "XAF", 'cours': "655.745724",
               'date': "29/09/2022", 'abreviation': "XAF", 'nom': "franc CFA (BCEAC)"}
data["XAG"] = {'code': "XAG", 'cours': "0.051468", 'date': "29/09/2022",
               'abreviation': "XAG", 'nom': "argent (libellé en onces)"}
data["XAU"] = {'code': "XAU", 'cours': "0.000585", 'date': "29/09/2022",
               'abreviation': "XAU", 'nom': "or (libellé en onces)"}
data["XCD"] = {'code': "XCD", 'cours': "2.618103", 'date': "29/09/2022",
               'abreviation': "XCD", 'nom': "dollar de la Caraïbe orientale"}
data["XDR"] = {'code': "XDR", 'cours': "0.752569", 'date': "29/09/2022",
               'abreviation': "XDR", 'nom': "droits de tirage spéciaux (DTS)"}
data["XOF"] = {'code': "XOF", 'cours': "655.745724",
               'date': "29/09/2022", 'abreviation': "XOF", 'nom': "franc CFA (BCEAO)"}
data["XPD"] = {'code': "XPD", 'cours': "0.0013", 'date': "29/09/2022",
               'abreviation': "XPD", 'nom': "palladium (libellé en onces)"}
data["XPF"] = {'code': "XPF", 'cours': "119.798681",
               'date': "29/09/2022", 'abreviation': "XPF", 'nom': "franc CFP (IEOM)"}
data["XPT"] = {'code': "XPT", 'cours': "0.0013", 'date': "29/09/2022",
               'abreviation': "XPT", 'nom': "platine (libellé en onces)"}
data["YER"] = {'code': "YER", 'cours': "242.430293",
               'date': "29/09/2022", 'abreviation': "YER", 'nom': "rial"}
data["ZAR"] = {'code': "ZAR", 'cours': "17.366998", 'date': "29/09/2022",
               'abreviation': "ZAR", 'nom': "rand (compte convertible)"}
data["ZMW"] = {'code': "ZMW", 'cours': "15.075032",
               'date': "29/09/2022", 'abreviation': "ZMW", 'nom': "kwacha"}

today = datetime.datetime.utcnow().strftime("%d/%m/%Y")

currencies = list(data.keys())
currencies.sort()

order = ['code', 'cours', 'date', 'abreviation', 'nom']

pagina = pywikibot.Page(pywikibot.Site('fr', 'wikivoyage'), 'Module:Prix/Data')
texto = pagina.get()

m = re.match('(.*)-- BOT.*-- // BOT(.*)', texto,
             flags=re.MULTILINE | re.DOTALL)

final = []

google = requests.get(
    os.getenv('google_docs_rates'))
google = google.text.splitlines()
for line in google:
    row = line.split("\t")
    if row[0] == 'Google' or row[2] == '#N/A':
        continue
    data.get(row[1])['cours'] = row[2]
    data.get(row[1])['date'] = today

strings = []
for key, elements in data.items():
    element = []
    for key_element in elements:
        element.append("{}=\"{}\"".format(
            key_element, elements.get(key_element)))
    local = '\tdata["{}"] = {{{}}}'.format(key, ",".join(element))
    strings.append(local)

page = m.group(1)
page += u"-- BOT\n"
page += "\n".join(strings)
page += u'\n-- // BOT'
page += m.group(2)

# print(page)

pagina.put(
    page, summary=u'Bot: Misé a jour [[:es:User Talk:Superzerocool|commentes]]')
