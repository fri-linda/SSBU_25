from matplotlib import pyplot as plt
from typing import Callable
import matplotlib
matplotlib.use('TkAgg')

class BasePlotter:
    """Abstract base class for common plotting functionality."""

    def __generic_plot(self, plot_func: Callable, *args, **kwargs):
        """
        A generic plotting function to reduce redundancy in plotting methods.

        Parameters:
        - plot_func: Callable, the plotting function to use.
        - args: Positional arguments for the plotting function.
        - kwargs: Keyword arguments for the plotting function.
        """
        general_kwargs = {key: kwargs.pop(key, None) for key in ['title', 'xlabel', 'ylabel', 'xticks_rotation', 'yticks', 'yticklabels', 'xticks']}
        plt.figure(figsize=kwargs.pop('figsize', (10, 6)))
        plot_func(*args, **kwargs)
        self.__apply_plot_labels(general_kwargs)
        plt.tight_layout()
        plt.show()

    def __apply_plot_labels(self, general_kwargs):
        """
        Applies labels and titles to a plot.

        Parameters:
        - general_kwargs: dict, containing title, xlabel, ylabel, and other label-related arguments.
        """
        if general_kwargs['title']:
            plt.title(general_kwargs['title'])
        if general_kwargs['xlabel']:
            plt.xlabel(general_kwargs['xlabel'])
        if general_kwargs['ylabel']:
            plt.ylabel(general_kwargs['ylabel'])
        if general_kwargs['xticks_rotation']:
            plt.xticks(rotation=general_kwargs['xticks_rotation'])
        if general_kwargs['xticks'] is not None:
            plt.xticks(ticks=general_kwargs['xticks'])
        if general_kwargs['yticks'] is not None and general_kwargs['yticklabels'] is not None:
            plt.yticks(ticks=general_kwargs['yticks'], labels=general_kwargs['yticklabels'])