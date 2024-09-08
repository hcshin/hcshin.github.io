import click
import arrow
from datetime import datetime
from pathlib import Path
from setup_logger import setup_logger

ROOT_PATH = Path(__file__).parents[2]
POST_PATH = ROOT_PATH.joinpath('_posts')

@click.command()
@click.option(
    '--logging-level',
    type=click.Choice(['DEBUG', 'INFO', 'WARNING'], case_sensitive=False),
    default='INFO',
    show_default=True,
    help='logging level for logger'
)
@click.argument(
    'post-title',
    type=click.STRING,
    nargs=1,
)
@click.argument(
    'post-tags',
    type=click.STRING,
    nargs=-1
)
def main(
    logging_level,
    post_title,
    post_tags
):
    logger = setup_logger('create-post-logger', logging_level)
    logger.debug('program started')

    with open(
        ROOT_PATH.joinpath(POST_PATH.\
                           joinpath(f'{arrow.now().format("YYYY-MM-DD")}-'+post_title+'.markdown').\
                           resolve().\
                           relative_to(ROOT_PATH)),
        'w'
    ) as post_f:
        logger.debug('file pointer created')
        posthead = (\
            '---\n'
            'layout: post\n'
            f'title: \"{post_title}\"\n'
            f'date: {arrow.now().format("YYYY-MM-DD HH:mm:ss ZZ")}\n'
            f'tags: {" ".join(post_tags)}\n'
            '---\n'
            '\n'
            'Put abstract and contents here\n'
        )
        logger.debug(f'file content to be written:\n{posthead}')
        post_f.write(posthead)
    logger.debug('program terminating')


if __name__ == '__main__':
    main()
