""" Search for good hyperparameters for embedding sequences of audio and MIDI
spectrograms into a common space. """
import pse
import os
import sys
sys.path.append(os.path.join('..', '..'))
import experiment_utils

RESULTS_PATH = '../../results'


if __name__ == '__main__':
    # Define hyperparameter space
    space = {
        'momentum': {'type': 'float', 'min': 0., 'max': 1.},
        'negative_threshold': {'type': 'int', 'min': 1, 'max': 16},
        'dropout': {'type': 'int', 'min': 0, 'max': 1},
        'learning_rate': {'type': 'float', 'min': .0001, 'max': .01},
        'negative_importance': {'type': 'float', 'min': 0.01, 'max': 1.},
        'entropy_importance': {'type': 'float', 'min': 0.0, 'max': 1.},
        'n_conv': {'type': 'int', 'min': 0, 'max': 3},
        'network': {'type': 'enum',
                    'options': ['pse_big_filter', 'pse_small_filters']}
    }

    # Construct paths
    trial_directory = os.path.join(RESULTS_PATH, 'pse_parameter_trials')
    model_directory = os.path.join(RESULTS_PATH, 'pse_model')
    data_directory = os.path.join(RESULTS_PATH, 'training_dataset_unaligned')

    # Run parameter optimization forever
    experiment_utils.parameter_search(
        space, trial_directory, model_directory, data_directory, pse.train)
