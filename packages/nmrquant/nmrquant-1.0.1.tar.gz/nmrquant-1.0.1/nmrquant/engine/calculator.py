"""Module containing the main Data Analyzer"""
import logging
from datetime import datetime
import sys

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import colorcet as cc
from natsort import natsort_keygen
import nmrquant.logger

from nmrquant.engine.utilities import read_data, is_empty, append_value

mod_logger = logging.getLogger("RMNQ_logger.engine.calculator")


# noinspection PyBroadException
class Quantifier:
    """
    RMNQ main class to quantify and visualize data
    """

    def __init__(self, verbose=False):

        self.verbose = verbose
        # When True, TSP concentration will be used to calculate concentration
        self.use_tsp = False

        # Initialize child logger for class instances
        self.logger = logging.getLogger(f"RMNQ_logger.engine.calculator.Quantifier")
        # fh = logging.FileHandler(f"{self.run_name}.log")
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)

        # For debugging purposes
        if verbose:
            handler.setLevel(logging.DEBUG)
        else:
            handler.setLevel(logging.INFO)

        if not self.logger.hasHandlers():
            self.logger.addHandler(handler)

        # Data attributes (future DataFrames)
        self.data = None
        self.mdata = None
        self.database = None
        self.metadata = None
        self.cor_data = None
        self.calc_data = None
        self.conc_data = None
        self.mean_data = None
        self.std_data = None
        self.plot_data = None
        self.ind_plot_data = None
        self.mean_plot_data = None

        # Lists with template info
        self.metabolites = []
        self.conditions = []
        self.time_points = []

        # Dictionary that will contain H+ count for each metabolite
        self.proton_dict = {}

        # List for missing metabolites in db
        self.missing_metabolites = []

        # For generating template
        self.spectrum_count = 0
        # Should be over 1
        self.dilution_factor = None

    def __len__(self):
        """ Length of object is equal to number of
        metabolites in dataset"""

        return f" There are {len(self.metabolites)} metabolites in data set"

    def __repr__(self):
        return "Quantifier object to calculate concentrations from 1D " \
               "NMR data and visualize results"

    def display(self, *args):
        """
        Display different attribute values (for debugging purposes)

        :param args: list of attribute values to return
        :return: attribute value
        """

        if "database" in args:
            try:
                return self.database
            except AttributeError:
                self.logger.error("The database is not loaded."
                                  " Please load and try again")

        if "proton_dict" in args:
            try:
                return self.proton_dict
            except AttributeError:
                self.logger.error("The proton dictionary is not loaded. "
                                  "Please load and try again")

        if "data" in args:
            try:
                return f"Data: {print(self.data)}"
            except AttributeError:
                self.logger.error("Data not loaded. Please load and try again")

        if "merge_data" in args:
            try:
                return f"Merged Data: {print(self.mdata)}"
            except AttributeError:
                self.logger.error("Data not merged. Please merge and try again")

        if "dilution_factor" in args:
            try:
                return f"Dilution factor: {self.dilution_factor}"
            except AttributeError:
                self.logger.error("No dilution factor registered")

        elif is_empty(args):
            self.logger.error("No attribute to check. Please enter"
                              "the attribute")

        else:
            self.logger.error(f"The attributes: {args} do not exist")

    def get_data(self, data, excel_sheet=0):
        """Get data from path or excel file"""

        if isinstance(data, str):
            try:
                self.data = read_data(data, excel_sheet)
            except TypeError as tperr:
                self.logger.error(f"Error while reading data:{tperr}")
        else:
            self.data = data
        try:
            if self.data.at[1, "TSP"] == 9:
                self.use_tsp = True
            self.data.drop("TSP", axis=1, inplace=True)
        except KeyError:
            self.logger.error("TSP not found in columns")
        except Exception:
            self.logger.exception(f"Unexpected error")

        self.spectrum_count = self.data["# Spectrum#"].max()

        self.logger.info("Data has been loaded")

    def get_db(self, database):
        """
        Get database from file or path

        :param database: Can be a file directly or a str containing the path to the file
        """

        if isinstance(database, str):
            self.database = read_data(database)

            if "Metabolite" not in self.database.columns or "Heq" not in self.database.columns:
                self.logger.error("'Metabolite' and/or 'Heq' columns not found in file. Please check your database "
                                  "file headers")
        else:
            self.database = database

        try:
            self.database.sort_values(by="Metabolite", inplace=True)

            self.database["Heq"] = self.database["Heq"].apply(
                lambda x: x.replace(',', '.'))

            self.database["Heq"] = pd.to_numeric(self.database["Heq"])

            for _, met, H in self.database[["Metabolite", "Heq"]].itertuples():
                self.proton_dict.update({met: H})

        except KeyError:
            self.logger.exception('DataFrame error, are you sure you imported the right file?')

        except Exception:
            self.logger.exception(f'Unexpected error')

        else:
            self.logger.info("Database has been loaded")

    def generate_metadata(self, path):
        """Generate template in excel format"""

        self.logger.info("Generating Template...")

        md = pd.DataFrame(columns=["Conditions", "Time_Points", "Replicates"])
        md["# Spectrum#"] = range(1, self.spectrum_count + 1)
        md.Conditions = ""
        md.Time_Points = ""
        md.Replicates = ""

        md.to_excel(r'{}/RMNQ_Template.xlsx'.format(path), index=False)

        self.logger.info("Template generated")

    def import_md(self, md):
        """Import metadata file after modification from path or file

        :param md: Can be a file directly or a str containing the path to the file
        """

        self.logger.info("Reading metadata...")

        if isinstance(md, str):
            try:
                self.metadata = read_data(md)
                headers = ["Conditions", "Time_Points", "Replicates", "# Spectrum#"]
                for head in headers:
                    if head not in self.metadata.columns:
                        raise RuntimeError(f'The column "{head}" was not found in file. Please check your template '
                                           f'file headers')
            except Exception:
                self.logger.exception(f"Error while reading template")
            else:
                self.conditions = self.metadata["Conditions"].unique()
                self.time_points = self.metadata["Time_Points"].unique()
        else:
            self.metadata = md

        self.logger.info("Metadata has been loaded")

    def merge_md_data(self):
        """Merge user-defined metadata with dataset"""

        self.logger.info("Merging...")

        self.mdata = self.metadata.merge(self.data, on="# Spectrum#")
        self.mdata.set_index(["Conditions", "Time_Points",
                              "Replicates", "# Spectrum#"], inplace=True)
        self.mdata.replace(0, np.nan, inplace=True)

        self.logger.info("Merge done!")

    def clean_cols(self):
        """Sum up double metabolite columns"""

        self.logger.info("Cleaning up columns...")

        tmp_dict = {}

        # Get rid of columns containing + sign because only
        # useful to calculate other cols (ex: LEU+ILE)
        cols = [c for c in self.mdata.columns if "+" not in c]
        self.mdata = self.mdata[cols]
        del cols  # cleanup

        # Sort index so that numbered metabolites are together
        # which helps with the n_counting
        self.cor_data = self.mdata
        self.cor_data.sort_index(axis=1, inplace=True)

        self.logger.debug(f"Beginning cor_data = {self.cor_data}")

        # Get indices where metabolites are double
        for ind, col in enumerate(self.cor_data.columns):

            split = col.split(" ")

            if len(split) > 1:  # Else there is no double met

                append_value(tmp_dict, split[0], ind)

        self.logger.debug(f"Temp dict = {tmp_dict}")

        ncount = 0  # Counter for substracting from indices
        if is_empty(tmp_dict):
            return self.logger.info("No double metabolites in data set. Columns are clean")

        else:
            for key, val in tmp_dict.items():
                dropval = [x - ncount for x in val]  # Real indices after drops
                self.logger.debug(f"Dropvals = {dropval}")

                self.cor_data[key] = self.cor_data.iloc[:, dropval[0]] + self.cor_data.iloc[:, dropval[1]]

                self.cor_data.drop(self.cor_data.columns[dropval],
                                   axis=1, inplace=True)

                ncount += 2  # Not 1 because the new cols are added at the end of df

            self.logger.debug(f"End cor_data = {self.cor_data}")

        self.metabolites = list(self.cor_data.columns)

        return self.logger.info("Data columns have been cleaned")

    def prep_db(self):
        """Prepare database for concentration calculations"""

        tmp_dict = {}
        removed_values = []

        # Prepare to split on spaces for where there are
        # spaces there are numbers after (as for clean_cols).
        for key, val in self.proton_dict.items():

            split = key.split("_")
            self.logger.debug(f"Split = {split}")

            # Here we check the len of the split. If it is
            # over 1, we get the name of the metabolite
            # and put it in the tmp_dict. The Key is then
            # put in list to remove later
            if len(split) > 1:
                append_value(tmp_dict, split[0], val)
                removed_values.append(key)

        self.logger.debug(f"Temp dict = {tmp_dict}")
        self.logger.debug(f"Removed values = {removed_values}")

        if is_empty(tmp_dict):
            return self.logger.info(
                "No double metabolites in data set. Database entries are clean")

        else:
            self.logger.debug(tmp_dict)

            # We sum up the values for keys in the tmp dict because they
            # are the total protons for the concerned metabolite.
            tmp_dict = {key: sum(vals) for key, vals in tmp_dict.items()}

            self.logger.debug(f"Summed temp dict = {tmp_dict}")
            self.logger.debug(f"Proton dict before del = {self.proton_dict}")

            # We remove the keys with numbers in the original proton dict
            for key in removed_values:
                del self.proton_dict[key]

            # We merge the dicts to have the final proton dict (thank you
            # python 3.9)
            if sys.version_info[0] >= 3.9:
                self.proton_dict = self.proton_dict | tmp_dict
            else:
                self.logger.warning("Python version different from 3.9. Please consider"
                                    "upgrading for compatibility reasons in the future")
                self.proton_dict = {**self.proton_dict, **tmp_dict}

            self.logger.debug(f"Proton dict after del = {self.proton_dict}")

        return self.logger.info("Database ready!")

    def calculate_concentrations(self, tsp_conc=1):
        """
        Calculate concentrations using number of
        protons and dilution factor

        :param tsp_conc: TSP concentration for external calibration. If calibration is internal, concentration
                         is equal to one.
        :return self.conc_data: Dataframe containing calculated concentrations
        """

        self.logger.info("Calculating concentrations...")

        # Check for NA and prepare dataframe
        self.cor_data.fillna(0, inplace=True)
        self.conc_data = pd.DataFrame(columns=self.cor_data.columns)

        # Multiply areas by dilution factor and TSP concentration (equal to 1 if internal calibration)
        self.conc_data = self.cor_data.apply(lambda x: (x * self.dilution_factor * tsp_conc))

        self.logger.debug(f"Proton dict before del = {self.proton_dict}")

        # Divide for each metabolite the values by proton number to get concentrations
        for col in self.conc_data.columns:

            missing_from_db = False  # To check if value is missing. If true then add a star in front of met name

            if col not in self.proton_dict.keys():
                self.missing_metabolites.append(col)
                proton_val = 1
                missing_from_db = True
                self.conc_data.rename(columns={col: col + "_Area"}, inplace=True)

            else:
                for key, val in self.proton_dict.items():
                    if key == col:
                        proton_val = val
                        break

            if missing_from_db:
                self.conc_data[col + "_Area"] = self.conc_data[col + "_Area"].apply(lambda x: x / proton_val)
                self.metabolites = list(self.conc_data.columns)
            else:
                self.conc_data[col] = self.conc_data[col].apply(lambda x: x / proton_val)

        self.logger.info("Concentrations have been calculated")

    def get_mean(self):
        """Make dataframe meaned on replicates"""

        self.mean_data = self.conc_data.droplevel("# Spectrum#")

        self.mean_data = self.conc_data.groupby(
            ["Conditions", "Time_Points"]).mean()
        self.std_data = self.conc_data.groupby(
            ["Conditions", "Time_Points"]).std()

        return self.logger.info("Means and standard deviations have been calculated")

    def export_data(self, destination, file_name='', fmt="excel", export_mean=False):
        """Export final data in desired format"""

        # Get current date & time
        date_time = datetime.now().strftime("%d%m%Y %Hh%Mmn")
        name = file_name + '_' + date_time

        # Output to multi-page excel file
        if fmt == "excel":
            with pd.ExcelWriter(r"{}/{}.xlsx".format(destination, name)) as writer:
                self.mdata.to_excel(writer, sheet_name='Raw Data')
                self.conc_data.to_excel(writer, sheet_name='Concentrations Data')

                if export_mean:
                    self.mean_data.to_excel(writer, sheet_name='Meaned Data')
                    self.std_data.to_excel(writer, sheet_name='Stds')

        return self.logger.info("Data Exported")

    # Visualization part of the quantifier starts here

    def prep_plots(self):
        """Prepare data for plotting"""

        self.plot_data = self.conc_data.reset_index()
        self.plot_data["Times"] = self.plot_data["Time_Points"]
        self.plot_data["Time_Points"] = self.plot_data["Time_Points"].astype(str)
        # Make IDs for indexing
        self.plot_data["long_ID"] = self.plot_data["Conditions"] + "_" + self.plot_data["Time_Points"] + "_" \
                                    + self.plot_data["Replicates"].astype(str)
        self.plot_data["short_ID"] = self.plot_data["Conditions"] + "_" + self.plot_data["Time_Points"]

        self.ind_plot_data = self.plot_data.copy()
        self.mean_plot_data = self.plot_data.copy()

        self.ind_plot_data.sort_values(by=["Conditions", "Time_Points", "Replicates"], key=natsort_keygen(),
                                       inplace=True)

        self.mean_plot_data.sort_values(by=["Conditions", "Time_Points"], key=natsort_keygen(), inplace=True)

        self.logger.info("Ready for plotting")

    def get_colors(self, metabolite):
        """
        Generate colormap for individual histograms

        :param metabolite: chosen metabolite to plot
        :return: colormap
        """

        colors = cc.glasbey_bw[:len(self.plot_data[metabolite])]
        cmap = []

        # Make cmap
        if len(self.ind_plot_data.Replicates.unique()) > 1:
            for ind, ids in enumerate(self.ind_plot_data["short_ID"].unique()):

                view = self.ind_plot_data[self.ind_plot_data["short_ID"] == ids]
                self.logger.debug(f"View of colormap generation df: {view}")
                rep_num = len(view.Replicates.unique())

                for i in range(1, rep_num + 1):
                    cmap.append(colors[ind])

            self.logger.debug(f"Colormap values: {cmap}")

        else:
            cmap = colors

        return cmap

    def make_hist(self, metabolite, mean=False, display=False):
        """
        Make histograms with quantification data

        :param display: Should plot be displayed on creation
        :param metabolite: Metabolite to plot
        :param mean: Should means with Stds be plotted or only individual data
        :return: Histogram
        """

        # Initiate figure and axes
        fig, ax = plt.subplots()

        # Get y limits and create colormap for barplots
        max_ylim = max(self.ind_plot_data[metabolite]) + (max(self.ind_plot_data[metabolite] / 10))
        cmap = self.get_colors(metabolite)

        # Plot individual or meaned data
        if mean:
            sns.barplot(data=self.mean_plot_data, x="short_ID", y=metabolite, ci="sd",
                        capsize=.1, errwidth=.6, ax=ax, palette=cc.glasbey_bw[:])
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                               horizontalalignment='right')
            ax.set_xlabel("Condition & Time")
            ax.set_ylabel("Concentration in mM")
            ax.set_title(f"{metabolite}")
            ax.set_ylim(0, max_ylim)

            fig.tight_layout()
            if display is True:
                plt.show()

            else:
                plt.savefig(f"{metabolite}.svg")
                plt.close()

        else:
            sns.barplot(data=self.ind_plot_data, x="long_ID", y=metabolite, ax=ax, palette=cmap)
            ax.set_xlabel("Condition & Time")
            ax.set_ylabel("Concentration in mM")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                               horizontalalignment='right')
            ax.set_title(f"{metabolite}")
            ax.set_ylim(0, max_ylim)

            fig.tight_layout()
            if display is True:
                plt.show()

            else:
                plt.savefig(f"{metabolite}.svg")
                plt.close()

        return self.logger.info(f"{metabolite} has been plotted")

    def make_lineplot(self, metabolite, plot_type, display=False):
        """
        Make line plot of given metabolite

        :param plot_type: Individual plots show all replicates. Summary plots show all conditions with meaned replicates
        :param metabolite: Metabolite to plot
        :param display: Should plot be displayed on creation
        :return: LinePlot
        """

        # No need to instantiate figures and axes because seaborn FacetGrid does it for us
        # Get y limits

        for condition in self.mean_plot_data.Conditions.unique():
            tmp_data = self.mean_plot_data[self.mean_plot_data["Conditions"] == condition]
            max_ylim = max(tmp_data[metabolite]) + (max(tmp_data[metabolite] / 10))
            max_xlim = max(tmp_data["Times"]) + (max(tmp_data["Times"]) / 20)

            # Make individual or summary plots
            if plot_type == "individual":
                plot = sns.relplot(x="Times", y=metabolite, hue="Replicates",
                                   data=tmp_data, kind="line",
                                   palette=cc.glasbey_bw[0: len(
                                       tmp_data.Replicates.unique())])

                plot.fig.suptitle(f"{metabolite}\n{condition} ")
                plot.set_axis_labels("Times in hours", "Concentration in mM")
                plot.set_xticklabels(rotation=45, horizontalalignment="right")
                plot.set(ylim=(0, max_ylim))
                plot.set(xlim=(0, max_xlim))
                leg = plot.legend
                leg.set_bbox_to_anchor([1, 0.7])

                plot.fig.subplots_adjust(bottom=0.1)

                if display is True:
                    plt.show()
                else:
                    plt.savefig(f"{metabolite}_{condition}.svg")
                    plt.close()

                self.logger.info(f"{metabolite} {condition} has been plotted")

        if plot_type == "summary":
            max_ylim = max(self.mean_plot_data[metabolite]) + (max(self.mean_plot_data[metabolite] / 10))
            max_xlim = max(self.mean_plot_data["Times"]) + (max(self.mean_plot_data["Times"]) / 20)

            plot = sns.relplot(data=self.mean_plot_data, x="Times",
                               y=metabolite, hue="Conditions", kind="line",
                               palette=cc.glasbey_bw[0:len(self.mean_plot_data.Conditions.unique())],
                               ci="sd", err_style="bars", err_kws={"capsize": 5})

            plot.fig.suptitle(f"{metabolite}")
            plot.set_axis_labels("Times in hours", "Concentration in mM")
            plot.set_xticklabels(rotation=45, horizontalalignment="right")
            plot.set(ylim=(0, max_ylim))
            plot.set(xlim=(0, max_xlim))
            leg = plot.legend
            leg.set_bbox_to_anchor([1, 0.7])
            plot.fig.subplots_adjust(bottom=0.1)
            if display is True:
                plt.show()
            else:
                plt.savefig(f"{metabolite}.svg")
                plt.close()

            self.logger.info(f"{metabolite} has been plotted")
