"""
Alimentar roles
"""
import click

from plataforma_web.blueprints.roles.models import Rol


def alimentar_roles():
    """Alimentar roles"""
    cantidad = Rol.insert_roles()
    click.echo(f"  {cantidad} roles alimentados.")
