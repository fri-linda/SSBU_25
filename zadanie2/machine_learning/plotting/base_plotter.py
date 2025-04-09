from matplotlib import pyplot as plt
from typing import Callable
import os
import datetime

class BasePlotter:
    """Abstract base class for common plotting functionality."""
    # pridanie konstruktora kvoli ziskavaniu info o pocte replikacii
    def __init__(self, output_dir='plots', replications:int=None):
        self.output_dir = output_dir
        self.replications = replications
        os.makedirs(self.output_dir, exist_ok=True)

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


        # Uloženie grafov do podadresára 'machine_learning' s dátumom alebo typom
        base_dir = 'plots'
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        # Vytvorenie podadresára s timestampom
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
        plot_type = kwargs.get('title', 'plot').replace(" ", "_").lower()  # Názov typu grafu
        plot_type = plot_type[:50]  # Zabezpečíme, že názov nebude príliš dlhý

        replications_str = f"_replications-{self.replications}" if self.replications else ""
        timestamped_dir = os.path.join(base_dir, f"{plot_type}_{timestamp}{replications_str}")
        if not os.path.exists(timestamped_dir):
            os.makedirs(timestamped_dir)

        # Dynamický názov súboru pre každý graf (podľa názvu metriky alebo typu grafu)
        file_name = f"{plot_type}.png"
        file_path = os.path.join(timestamped_dir, file_name)

        # Ak súbor už existuje, pridať index pre jedinečný názov
        index = 1
        while os.path.exists(file_path):
            file_path = os.path.join(timestamped_dir, f"{plot_type}_{index}.png")
            index += 1


        plt.savefig(file_path)  # Uloží do podadresára
        plt.show()
        plt.close()  # Zavrie aktuálny graf, aby sa nezobrazoval
        print(f"Graph saved as '{file_path}'")

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