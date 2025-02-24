"""
Alimentar modulos
"""
from pathlib import Path
import csv
import click

from plataforma_web.blueprints.modulos.models import Modulo

MODULOS_CSV = "seed/modulos.csv"


def alimentar_modulos():
    """Alimentar modulos"""
    ruta = Path(MODULOS_CSV)
    if not ruta.exists():
        click.echo(f"AVISO: {ruta.name} no se encontró.")
        return
    if not ruta.is_file():
        click.echo(f"AVISO: {ruta.name} no es un archivo.")
        return
    click.echo("Alimentando módulos...")
    contador = 0
    with open(ruta, encoding="utf8") as puntero:
        rows = csv.DictReader(puntero)
        for row in rows:
            Modulo(
                nombre=row["nombre"],
                estatus=row["estatus"],
            ).save()
            contador += 1
    click.echo(f"  {contador} módulos alimentadas.")
