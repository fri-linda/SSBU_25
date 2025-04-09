import os
from matplotlib import pyplot as plt


class PlotSaver:
    @staticmethod
    def save_plot(plot_name: str, folder: str = "outputs/plots"):
        """
        Save the current plot to a file.
        Args:
            plot_name: Name of the plot (used for filename)
            folder: Destination folder
        """
        os.makedirs(folder, exist_ok=True)
        filename = f"{folder}/{plot_name.lower().replace(' ', '_')}.png"
        plt.savefig(filename)
        plt.close()