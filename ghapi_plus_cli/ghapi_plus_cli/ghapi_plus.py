import click


def __init__():
    click.echo("ghapi_plus_cli Copyright (C) 2022 osfanbuff63\nThis program comes with ABSOLUTELY NO WARRANTY; for details type 'gh_api --warranty'. \nThis is free software, and you are welcome to redistribute it\n under certain conditions; type 'gh_api --redistribute' for details.")


@click.group
@click.option("--warranty", "warranty", is_flag=True, help="Shows information about how this program has no warranty.")
@click.option("--redistributing", "redistribute", is_flag=True, help="Shows information about how you can redistribute this program.")
def gh_api(warranty, redistribute):
    if warranty is True:
        click.echo("From the GNU General Public License, section 15:\n\nTHERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.\nEXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES\nPROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER\nEXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF\nMERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE\nQUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE\nDEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.")
    if redistribute is True:
        click.echo("Please read the GNU General Public License section 6 for more details.")


@gh_api.command()
@click.option("--extended/--no-extended", default=False)
def about(extended):
    from sys import platform
    if extended is True:
        click.echo(f"ghapi_plus_cli v0.1.0 running on {platform}\nLast updated: 9/26/2022\n\nCopyright (C) 2022 osfanbuff63\nThis program comes with ABSOLUTELY NO WARRANTY; for details type 'ghapi_plus --warranty'.\nThis is free software, and you are welcome to redistribute it under certain conditions; type 'ghapi_plus --redistributing' for details.")
    else:
        click.echo(f"ghapi_plus_cli v0.1.0 running on {platform}")

if __name__ == '__main__':
    gh_api()
