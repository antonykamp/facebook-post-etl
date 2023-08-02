import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from datetime import datetime, timedelta
import pandas as pd

plt.rcParams.update({"font.size": 15})

frames = [
    *["Grüne Ideologie"] * 60,
    *["Klimaaktivismus (FFF)"] * 15,
    # *["Arnthal Flutkatastrophe"] * 8,
    *["Anpassung der \nErnährung wegen Klima"] * 2,
]
df = pd.DataFrame({"frame": frames, "count": [1] * len(frames)})
ax = (
    df.groupby(df["frame"])
    .count()
    .sort_values(by="count", ascending=True)
    .plot(
        kind="barh",
        figsize=(10, 5),
        # title="Verteilung der Beitrage ohne falsche Posts",
        xlabel="Anzahl an Beiträgen",
        ylabel="",
    )
)
plt.bar_label(ax.containers[0], fmt=" (%d)", label_type="edge")
ax.margins(x=0.1)

# ax.set_xlabel("Monat")
# ax.set_ylabel("Anzahl an Beiträgen")
# ax.set_title("Anzahl an gefilterten Beiträgen pro Monat")
# ax.legend(["Gefilterte Beiträge"])
ax.get_legend().remove()
# TODO: add title
# TODO: change legend
plt.subplots_adjust(left=0.25)
plt.show()
