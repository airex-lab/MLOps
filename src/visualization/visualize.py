# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from tensorflow import keras
import pickle
import matplotlib.pyplot as plt
import numpy as np


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

    with open('reports/history.pkl', 'rb') as f:
        history = pickle.load(f)

    # plot the training loss and accuracy
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, 100), history.history["loss"], label="train_loss")
    plt.plot(np.arange(0, 100), history.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, 10), history.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, 100), history.history["val_accuracy"], label="val_acc")  # noqa: E501
    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    plt.savefig(report_dirpath + '/figures/history.png')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
