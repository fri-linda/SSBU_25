# base_plotter.py

import os  #NEW
from matplotlib import pyplot as plt
from typing import Callable

class BasePlotter:
    """Abstract base class for common plotting functionality."""

    def __generic_plot(self, plot_func: Callable, *args, **kwargs):
        """
        A generic plotting function to reduce redundancy in plotting methods.
        """
        general_kwargs = {key: kwargs.pop(key, None)
                          for key in ['title', 'xlabel', 'ylabel',
                                      'xticks_rotation', 'yticks', 'yticklabels', 'xticks']}
        figsize = kwargs.pop('figsize', (10, 6))
        plt.figure(figsize=figsize)
        plot_func(*args, **kwargs)
        self.__apply_plot_labels(general_kwargs)
        plt.tight_layout()

        # Uloženie grafu do adresára "machine_learning_rumisek_matus"  #NEW
        output_folder = "machine_learning_rumisek_matus"  #NEW
        os.makedirs(output_folder, exist_ok=True)  #NEW

        # Vytvorenie názvu súboru na základe title (ak je k dispozícii)  #NEW
        if general_kwargs.get('title'):
            safe_title = general_kwargs['title'].replace(":", "-")
            safe_title = safe_title.replace(" ", "_").lower()
            filename = f"{safe_title}.png"
        else:
            filename = "plot.png"

        # Uloženie grafu do PNG súboru  #NEW
        plt.savefig(os.path.join(output_folder, filename))  #NEW

        plt.show()
        #plt.close()

    def __apply_plot_labels(self, general_kwargs):
        """
        Applies labels and titles to a plot.
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
