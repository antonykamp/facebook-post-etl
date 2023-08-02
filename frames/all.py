import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from datetime import datetime, timedelta
import pandas as pd

plt.rcParams.update({"font.size": 15})


with open("scraped_3000.json", "r") as f:
    data = json.load(f)
    posts = data["data"]


search_token = [
    "klima",
    "umwelt",
    "natur",
    "heimat",
    "energie",
    "solar",
    "auto",
    "wirtschaft",
    "bio",
    "Windrad",
    "windräder",
    "wasserstoff",
    "kernkraft",
    "atomkraft",
    "erwärmung",
    "eike",
    "fridays for future",
    "fff",
    "e-auto",
    "verbrennermotor",
    "nahverkehr",
    "heinzung",
    "pariser klimaabkommen",
    "strom",
    "bio",
    "tier",
]
relevant_posts = [
    post
    for post in posts
    if post["text"] is not None
    and any(word.lower() in post["text"].lower() for word in search_token)
    and post["timestamp"] > datetime(2021, 9, 1).timestamp()
    and post["timestamp"] < datetime(2022, 8, 31).timestamp()
]
relevant_posts.reverse()
print(len(relevant_posts))
with open("relevant_posts.json", "w") as f:
    json.dump(relevant_posts, f)


timestamps = [post["timestamp"] for post in relevant_posts]
dates = [datetime.fromtimestamp(ts) for ts in timestamps]

months_string = [f"{date.month}. {date.year}" for date in dates]
list_months = sorted(set(months_string), key=months_string.index)
num_months = len(list_months)

df = pd.DataFrame(dates, columns=["date"])

ax = (
    df.groupby([df["date"].dt.year, df["date"].dt.month])
    .count()
    .plot(
        kind="barh",
        figsize=(10, 5),
        # title="Verteilung der Beitrage ohne falsche Posts",
        xlabel="Anzahl an Beiträgen",
        ylabel="Monat",
    )
)


ax.locator_params(axis="y", nbins=num_months)
ax.set_yticklabels(list_months)

# ax.set_xlabel("Monat")
# ax.set_ylabel("Anzahl an Beiträgen")
# ax.set_title("Anzahl an gefilterten Beiträgen pro Monat")
ax.invert_yaxis()
plt.bar_label(ax.containers[0], fmt=" (%d)", label_type="edge")

# ax.legend(["Gefilterte Beiträge"])
ax.get_legend().remove()
# TODO: add title
# TODO: change legend
# plt.subplots_adjust(bottom=0.2)
ax.margins(x=0.1)
plt.show()
