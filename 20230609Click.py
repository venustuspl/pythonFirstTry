import click
@click.command()
@click.option('-i', required=True)
def witacz(i):
    print(f'Witaj {i}')
witacz()