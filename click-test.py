import click


@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.argument('a', type=click.INT, required=True)
@click.argument('b', type=click.INT, required=True)
def main(verbose, a, b):
    if verbose:
        print('The answer is {}'.format(a + b))
    else:
        print(a + b)


if __name__ == '__main__':
    main(["-v", '1', '2'])
