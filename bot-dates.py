from pywikibot import Site, Page
import datetime

site = Site('es', 'wikinews')

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

def generate_days(start, days=7):
    """Genera una secuencia de días, incluyendo el día anterior y el posterior al día actual.

    Args:
        start (datetime.date): Fecha de inicio.
        days (int): Número de días a generar. Por defecto, 7.

    Yields:
        list: Una lista de tres fechas: el día anterior, el día actual y el día siguiente.
    """
    counter = 0
    while counter < days:
        yield [start + datetime.timedelta(days=counter-1), start + datetime.timedelta(days=counter), start + datetime.timedelta(days=counter+1)]
        counter += 1

def get_month(date: datetime.date) -> str :
    """
    Obtiene el nombre del mes a partir de un objeto fecha.

    Args:
        date (datetime.date): Objeto fecha.

    Returns:
        str: Nombre del mes en español.
    """
    return meses[date.month - 1]

def format_day(date: datetime.date) -> str:
    """
    Formatea la fecha en estilo español (DD de MM).

    Args:
        date (datetime.date): Objeto fecha.

    Returns:
        str: Fecha formateada.
    """
    return "{day} de {month}".format(day=date.day, month=get_month(date))

def format_date(date: datetime.date) -> str:
    """
    Formatea la fecha completa en estilo español (DD de MM de YYYY).

    Args:
        date (datetime.date): Objeto fecha.

    Returns:
        str: Fecha formateada.
    """
    return "{day} de {year}".format(day=format_day(date), year=date.year)

def format_month(date: datetime.date) -> str:
    """
    Formatea el mes y el año en estilo español (MM de YYYY).

    Args:
        date (datetime.date): Objeto fecha.

    Returns:
        str: Mes y año formateados.
    """
    return "{month} de {year}".format(month=get_month(date), year=date.year)

def create_category(yesterday: datetime.date, today: datetime.date, tomorrow: datetime.date) -> str:
    """
    Crea el texto para la categoría diaria.

    Args:
        yesterday (datetime.date): Fecha de ayer.
        today (datetime.date): Fecha de hoy.
        tomorrow (datetime.date): Fecha de mañana.

    Returns:
        str: Texto para la categoría diaria.
    """
    current_month = format_month(today)
    yesterday_formatted = format_date(yesterday)
    tommorrow_formatted = format_date(tomorrow)
    current_day = format_day(today)

    return "{{{{categoríaFecha|{month}|{yesterday}|{tomorrow}}}}}\n\n[[Categoría:{current_day}]]".format(month=current_month, yesterday=yesterday_formatted, tomorrow=tommorrow_formatted,current_day=current_day)

def create_month(today: datetime.date) -> str:
    """
    Crea el texto para la categoría mensual.

    Args:
        today (datetime.date): Fecha actual.

    Returns:
        str: Texto para la categoría mensual.
    """
    return "{{{{CategoríaMes|{month:02}|{year}}}}}".format(month=today.month, year=today.year)

# Obtiene la fecha actual
start = datetime.date.today()

for [yesterday, today, tomorrow] in generate_days(start, 365):
    print(today)
    # Crea la página de la categoría diaria
    category_day = Page(site, title="Category:{today}".format(today=format_date(today)))
    text = create_category(yesterday, today, tomorrow)
    category_day.put(text, summary="Creando categoría de fechas")

    # Verifica si es el primer día del mes para crear la categoría mensual
    if (today.day == 1):
        category_month = Page(site, title="Category:{month}".format(month=format_month(today)))
        category_month.put(create_month(today), summary="Creando categoría de mes")
