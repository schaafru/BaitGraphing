import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bait_data = 'BAIT_Abbrev_Bottle_Data_13July2021.xlsx'  # do not change this unless you are using a new file
df = pd.read_excel(bait_data)  # initiates Dataframe

column_names = []  # creates empty list
for column in df:  # grabs all column names and populates column_names variable
    column_names.append(column)
plot_values = df[column_names]  # creates variable with all column names available


class BaitGraphing:
    """
    graph data for bait graph
    """

    @staticmethod
    def graph_separate(value_1, value_2, title):
        """
        :param value_1: first value to graph
        :param value_2: second value to graph
        :param title: title of the graph
        :return: separate graphs with first and second value for baits 1-4
        """

        """
        ['Cruise', 'Cast #', 'Sample ID', 'Pressure (dbar)', 'Depth (m)', 'Long (°E)', 'Lat (°N)', 'Date (Z, mm/dd/yy) ', 
         'Time (Z)', 'DFe (nM)', 'DFe SD (nM)', 'sFe (nM)', 'sFe SD (nM)', 'DMn (nM)', 'DMn SD (nM)', 'sMn (nM)', 'sMn SD (nM)',
         'DNi', 'DNi SD (nM)', 'DCu (nM)', 'DCu SD (nM)', 'DZn (nM)', 'DZn SD (nM)', 'DAl (nM)', 'DAl SD (nM)', 'T (°C)',
         'Fluor (uncal, mg/m3)', 'S', 'Oxygen (µmol/kg)', 'Sigma-theta', 'Potential Temp. (°C)', 'NO3+NO2 (µmol/L)', 
         'NO2 (µmol/L)', 'PO4', 'Si (µmol/L)']
        """
        # BAITs (PO4/ DNi)
        bait_1 = df.iloc[1:36].plot(kind='scatter', x=value_1, y=value_2, rot=0, title=title, color='gold',
                                    legend=True, label='BAIT 1', grid=True)
        bait_1.set_xlabel('PO4 (µM)')
        bait_1.set_ylabel('DNi (nM)')
        bait_1.legend(loc='upper left')

        # BAIT 2
        bait_2 = df.iloc[37:72].plot(kind='scatter', x=value_1, y=value_2, title=title, rot=0, color='forestgreen',
                                     label='BAIT 2', grid=True)
        bait_2.set_xlabel('PO4 (µM)')
        bait_2.set_ylabel('DNi (nM)')
        bait_2.legend(loc='upper left')

        # BAIT 3
        bait_3 = df.iloc[74:111].plot(kind='scatter', x=value_1, y=value_2, title=title, rot=0, color='deepskyblue',
                                      label='BAIT 3', grid=True)
        bait_3.set_xlabel('PO4 (µM)')
        bait_3.set_ylabel('DNi (nM)')
        bait_3.legend(loc='upper left')

        # BAIT 4
        bait_4 = df.iloc[112:147].plot(kind='scatter', x=value_1, y=value_2, title=title, rot=0, color='indigo',
                                       label='BAIT 4', grid=True)
        bait_4.set_xlabel('PO4 (µM)')
        bait_4.set_ylabel('DNi (nM)')
        bait_4.legend(loc='upper left')

        plt.title("Average Dni Inventory In Upper 200m")
        plt.xlabel("Cruise #")
        plt.ylabel("nmol/m2")

        plt.show()

    @staticmethod
    def graph_together(value_1, value_2, title):
        """
        :param value_1: first value to graph
        :param value_2: second value to graph
        :param title: title of the graph
        :return: a single graph with first and second value for baits 1-4
        """

        # BAIT 1-4 together (PO4/DNi)
        axis_1 = df.iloc[1:36].plot(kind='scatter', x=value_1, y=value_2, rot=0, title=title, color='gold',
                                    legend=True, label='BAIT 1', grid=True)
        axis_1.set_xlabel('PO4 (µM)')
        axis_1.set_ylabel('DNi (nM)')

        bait_2 = df.iloc[37:72].plot(kind='scatter', x=value_1, y=value_2, rot=0, color='forestgreen',
                                     label='BAIT 2', grid=True, ax=axis_1)
        bait_2.set_xlabel('PO4 (µM)')
        bait_2.set_ylabel('DNi (nM)')

        bait_3 = df.iloc[74:111].plot(kind='scatter', x=value_1, y=value_2, rot=0, color='deepskyblue',
                                      label='BAIT 3', grid=True, ax=axis_1)
        bait_3.set_xlabel('PO4 (µM)')
        bait_3.set_ylabel('DNi (nM)')

        bait_4 = df.iloc[112:147].plot(kind='scatter', x=value_1, y=value_2, rot=0, color='indigo',
                                       label='BAIT 4', grid=True, ax=axis_1)
        bait_4.set_xlabel('PO4 (µM)')
        bait_4.set_ylabel('DNi (nM)')
        bait_4.legend(loc='upper left')

        plt.show()


graph = BaitGraphing()

graph.graph_together('PO4', 'DNi', 'test')


# # BAITs (NO3+NO2 (µmol/L)/ DNi)
# bait_1 = df.iloc[1:36].plot(kind='scatter', x='NO3+NO2 (µmol/L)', y='DNi', rot=0, title='Bait 1: Nickel vs Nitrate + Nitrite', color='gold',
#                             legend=True, label='BAIT 1', grid=True)
# bait_1.set_xlabel('NO3+NO2 (µmol/L)')
# bait_1.set_ylabel('DNi (nM)')
# bait_1.legend(loc='upper left')
#
# # BAIT 2
# bait_2 = df.iloc[37:72].plot(kind='scatter', x='NO3+NO2 (µmol/L)', y='DNi', title='Bait 2: Nickel vs Nitrate + Nitrite', rot=0, color='forestgreen',
#                              label='BAIT 2', grid=True)
# bait_2.set_xlabel('NO3+NO2 (µmol/L)')
# bait_2.set_ylabel('DNi (nM)')
# bait_2.legend(loc='upper left')
#
# # BAIT 3
# bait_3 = df.iloc[74:111].plot(kind='scatter', x='NO3+NO2 (µmol/L)', y='DNi', title='Bait 3: Nickel vs Nitrate + Nitrite', rot=0, color='deepskyblue',
#                               label='BAIT 3', grid=True)
# bait_3.set_xlabel('NO3+NO2 (µmol/L)')
# bait_3.set_ylabel('DNi (nM)')
# bait_3.legend(loc='upper left')
#
# # BAIT 4
# bait_4 = df.iloc[112:147].plot(kind='scatter', x='PO4', y='DNi', title='Bait 4: Nickel vs Nitrate + Nitrite', rot=0, color='indigo',
#                                label='BAIT 4', grid=True)
# bait_4.set_xlabel('NO3+NO2 (µmol/L)')
# bait_4.set_ylabel('DNi (nM)')
# bait_4.legend(loc='upper left')
#
#
# # BAIT 1-4 together (NO3+NO2 (µmol/L)/DNi)
# axis_1 = df.iloc[1:36].plot(kind='scatter', x='NO3+NO2 (µmol/L)', y='DNi', rot=0, title='Baits 1-4: Nickel vs Nitrate + Nitrite Baits', color='gold',
#                             legend=True, label='BAIT 1', grid=True)
# axis_1.set_xlabel('NO3+NO2 (µmol/L)')
# axis_1.set_ylabel('DNi (nM)')
#
#
# bait_2 = df.iloc[37:72].plot(kind='scatter', x='NO3+NO2 (µmol/L)', y='DNi', rot=0, color='forestgreen',
#                              label='BAIT 2', grid=True, ax=axis_1)
# bait_2.set_xlabel('NO3+NO2 (µmol/L)')
# bait_2.set_ylabel('DNi (nM)')
#
#
# bait_3 = df.iloc[74:111].plot(kind='scatter', x='NO3+NO2 (µmol/L)', y='DNi', rot=0, color='deepskyblue',
#                               label='BAIT 3', grid=True, ax=axis_1)
# bait_3.set_xlabel('NO3+NO2 (µmol/L)')
# bait_3.set_ylabel('DNi (nM)')
#
#
# bait_4 = df.iloc[112:147].plot(kind='scatter', x='NO3+NO2 (µmol/L)', y='DNi', rot=0, color='indigo',
#                                label='BAIT 4', grid=True, ax=axis_1)
# bait_4.set_xlabel('NO3+NO2 (µmol/L)')
# bait_4.set_ylabel('DNi (nM)')
# bait_4.legend(loc='upper left')
#
# # bar graph of average DNi inventory in upper 200 m
#
# sns.set_theme(style="darkgrid")
#
# plotdata = pd.DataFrame({
#     "Bait 1": [387940.46, 379050.26, 383568.33],
#     "Bait 2": [456425.34, 475777.54, 490218.15],
#     "Bait 3": [440492.40, 433507.13, 421130.47],
#     "Bait 4": [495205.93, 504417.93, 499089.70]
#      },
#     index=["Cast 1", "Cast 2", "Cast 3"]
# )
#
# plotdata.plot(kind="bar", grid=True).legend(loc='upper left', title="Bait #")
# plt.title("Average Dni Inventory In Upper 200m")
# plt.xlabel("Cruise #")
# plt.ylabel("nmol/m2")

#plt.show()  # this shows the graph
