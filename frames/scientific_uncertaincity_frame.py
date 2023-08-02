import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from datetime import datetime, timedelta
import pandas as pd
from matplotlib.ticker import MaxNLocator

with open("scraped_3000.json", "r") as f:
    data = json.load(f)
    posts = data["data"]

filtered_posts = [
    "1631004126-4620151484681821",
    "1632056444-4652380351458934",
    "1633708515-4719001288130173",
    "1634542955-4742134615816840",
    "1636705813-4827374707292830",
    "1651302000-5374708425892786",
    "1651302000-5374708425892786",
    "1651302000-5374708425892786",
    "1651939201-5393723207324641",
    "1652900400-5422554701108158",
    "1654608178-5487801004583527",
    "1655487731-5516914365005524",
    "1660225969-5669653369731622",
]

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
    and f"{str(post['timestamp'])}-{str(post['post_id'])}" in filtered_posts
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

# months_string = [f"{date.month}. {date.year}" for date in dates]
# list_months = sorted(set(months_string), key=months_string.index)
# num_months = len(list_months)
num_months = 12
list_months = [
    "9.2021",
    "10.2021",
    "11.2021",
    "12.2021",
    "1.2022",
    "2.2022",
    "3.2022",
    "4.2022",
    "5.2022",
    "6.2022",
    "7.2022",
    "8.2022",
]

df = pd.DataFrame(dates, columns=["date"])

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df = df.groupby([df["year"], df["month"]]).count()
df.columns = ["count"]
df.loc[(2021, 12), :] = int(0)
df.loc[(2022, 1), :] = int(0)
df.loc[(2022, 1), :] = int(0)
df.loc[(2022, 2), :] = int(0)
df.loc[(2022, 3), :] = int(0)
df.loc[(2022, 7), :] = int(0)
df.sort_index(inplace=True)
df["count"] = df["count"].astype(int)

ax = df.plot(
    kind="barh",
    figsize=(10, 5),
    # title='Verteilung der Beitrage "Scientific Uncertainty Frame"',
    xlabel="Anzahl an Beiträgen",
    ylabel="Monat",
)

ax.yaxis.set_major_locator(MaxNLocator(integer=True))

ax.locator_params(axis="y", nbins=num_months)
ax.set_yticklabels(list_months)
ax.invert_yaxis()
# ax.set_xlabel("Monat")
# ax.set_ylabel("Anzahl an Beiträgen")
# ax.set_title("Anzahl an gefilterten Beiträgen pro Monat")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.bar_label(ax.containers[0], fmt=" (%d)", label_type="edge")

# ax.legend(["Gefilterte Beiträge"])
ax.get_legend().remove()
# TODO: add title
# TODO: change legend
# plt.subplots_adjust(bottom=0.2)
plt.show()
