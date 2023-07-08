# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from tensorflow import keras

@click.command()
@click.argument('model_filepath', type=click.Path(exists=True))
@click.argument('report_dirpath', type=click.Path())
def main(model_filepath, report_dirpath):
    """ Visualizes the trained model from (../models)
        and saves the visualization to (../reports/figures)
    """
    logger = logging.getLogger(__name__)
    logger.info('visualize the model and save the visualizations')

    model = keras.models.load_model(model_filepath)
    print(model.summary())

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
