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
    "1631700341-4645448802152089",
    "1631700341-4645448802152089",
    "1636916401-4830887576941543",
    "1640166220-4971991472831152",
    "1645001283-5176713842358913",
    "1645619438-5199697393393891",
    "1647788400-5264196373610659",
    "1648458914-5282163895147240",
    "1650431263-5349902698373359",
    "1651060830-5369314033098892",
    "1651060830-5369314033098892",
    "1652198403-5405281482835480",
    "1654628421-5487942134569414",
    "1654628421-5487942134569414",
    "1654785942-5494264190603875",
    "1658307787-5609792922384334",
    "1661455328-5709896192374006",
    "1661842805-5720513767978915",
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
df.loc[(2021, 10), :] = int(0)
df.loc[(2022, 1), :] = int(0)
df.sort_index(inplace=True)
df["count"] = df["count"].astype(int)

ax = df.plot(
    kind="barh",
    figsize=(10, 5),
    # title='Verteilung der Beitrage "National Independence Frame"',
    xlabel="Anzahl an Beiträgen",
    ylabel="Monat",
)


ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.locator_params(axis="y", nbins=num_months)
ax.set_yticklabels(list_months)

# ax.set_xlabel("Monat")
# ax.set_ylabel("Anzahl an Beiträgen")
# ax.set_title("Anzahl an gefilterten Beiträgen pro Monat")

# ax.legend(["Gefilterte Beiträge"])
ax.get_legend().remove()
ax.invert_yaxis()
plt.bar_label(ax.containers[0], fmt=" (%d)", label_type="edge")

# TODO: add title
# TODO: change legend
# plt.subplots_adjust(bottom=0.2)
plt.show()
