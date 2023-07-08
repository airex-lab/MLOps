# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import numpy as np
from tensorflow import keras
import os
from PIL import Image

@click.command()
@click.argument('image_filepath', type=click.Path(exists=True))
@click.argument('model_filepath', type=click.Path())
def main(image_filepath, model_filepath):
    """ Predicts the label of an image using a model from (../models)
    """
    logger = logging.getLogger(__name__)
    logger.info('predict the label of the image')

    if not os.path.isfile(image_filepath):
        logger.error('image_filepath does not exist')
        return

    image = np.array([Image.open(image_filepath).resize((128, 128)).convert('L')])
    model = keras.models.load_model(model_filepath)
    predictions = np.argmax(model.predict(image), axis=1)
    
    labels = map(lambda x: model.labels[x], predictions)
    print(labels)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
