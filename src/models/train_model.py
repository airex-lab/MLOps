# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import numpy as np
import pickle
import tensorflow as tf
from tensorflow import keras


def split_data(data, ratio=0.8):
    train_images = []
    train_labels = []
    test_images = []
    test_labels = []
    for index, label in enumerate(data.keys()):
        one_hot_label = np.zeros(len(data.keys()))
        one_hot_label[index] = 1
        for i in range(len(data[label])):
            if i < len(data[label]) * ratio:
                train_images.append(data[label][i])
                train_labels.append(one_hot_label)
            else:
                test_images.append(data[label][i])
                test_labels.append(one_hot_label)

    return np.array(train_images), \
        np.array(train_labels), \
        np.array(test_images), \
        np.array(test_labels)


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Trains a model on processed data from (../processed)
        and saves it into (../models).
    """
    logger = logging.getLogger(__name__)
    logger.info('train model on processed data')

    (train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()  # noqa: E501
    train_images = train_images.reshape(
        (50000, 32 * 32 * 3)).astype('float32') / 255
    test_images = test_images.reshape(
        (10000, 32 * 32 * 3)).astype('float32') / 255
    train_labels = keras.utils.to_categorical(train_labels, 10)
    test_labels = keras.utils.to_categorical(test_labels, 10)
    # data = {}
    # with open(input_filepath, 'rb') as f:
    #     data = pickle.load(f)

    # train_images, train_labels, test_labels, test_images = split_data(data)

    # print(train_images.shape, train_labels.shape)

    model = keras.Sequential([
        keras.layers.Dense(1024, input_shape=(3072,), activation=tf.nn.relu),
        keras.layers.Dense(512, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy', 'loss', 'val_accuracy', 'val_loss'])
    model.summary()
    history = model.fit(train_images, train_labels,
                        epochs=10, batch_size=32,
                        validation_split=0.2)

    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Test Accuracy:', test_acc)
    print('Test Loss:', test_loss)

    with open("reports/history.pkl", 'wb') as f:
        pickle.dump(history, f)

    # model.labels = data.keys()
    model.save(output_filepath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
