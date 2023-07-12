# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from zipfile import ZipFile


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_dirpath', type=click.Path())
def main(input_filepath, output_dirpath):
    """ Runs data scripts to turn raw data from (../../data/raw) into
        cleaned data ready to be processed (saved in ../../data/interim).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    with ZipFile(input_filepath, 'r') as zipObj:
        zipObj.extractall(output_dirpath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
