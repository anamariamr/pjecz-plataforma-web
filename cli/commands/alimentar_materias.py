"""
Alimentar materias
"""
from pathlib import Path
import csv
import click

from plataforma_web.blueprints.materias.models import Materia

MATERIAS_CSV = "seed/materias.csv"


def alimentar_materias():
    """Alimentar materias"""
    ruta = Path(MATERIAS_CSV)
    if not ruta.exists():
        click.echo(f"AVISO: {ruta.name} no se encontró.")
        return
    if not ruta.is_file():
        click.echo(f"AVISO: {ruta.name} no es un archivo.")
        return
    click.echo("Alimentando materias...")
    contador = 0
    with open(ruta, encoding="utf8") as puntero:
        rows = csv.DictReader(puntero)
        for row in rows:
            Materia(
                nombre=row["nombre"],
                estatus=row["estatus"],
            ).save()
            contador += 1
    click.echo(f"  {contador} materias alimentadas.")
