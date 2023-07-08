# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pickle

@click.command()
@click.argument('input_dirpath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_dirpath, output_filepath):
    """ Runs data processing scripts to turn interim data from (../../data/interim) into
        processed data ready to be analyzed (saved in ../../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('process raw data into data ready for modeling')

    labels = os.listdir(input_dirpath)
    data = {}
    for label in labels:
        data[label] = []
        label_dirpath = os.path.join(input_dirpath, label)
        if os.path.isdir(label_dirpath):
            for image_filepath in os.listdir(label_dirpath):
                image_filepath = os.path.join(label_dirpath, image_filepath)
                if os.path.isfile(image_filepath):
                    image = Image.open(image_filepath)
                    image = image.resize((128, 128))
                    image = image.convert('L')
                    data[label].append(np.array(image))

    fig, ax = plt.subplots(2, 4, figsize=(10, 5))
    for i, label in enumerate(labels):
        data[label] = np.array(data[label])
        ax[i // 4, i % 4].imshow(data[label][0])
        ax[i // 4, i % 4].set_title(label)
        ax[i // 4, i % 4].axis('off')
    plt.show()

    Path(os.path.dirname(output_filepath)).mkdir(parents=True, exist_ok=True)

    with open(output_filepath, 'wb') as f:
        pickle.dump(data, f)
        print('data saved to %s' % output_filepath)

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
