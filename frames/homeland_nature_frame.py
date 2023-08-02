import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from datetime import datetime, timedelta
import pandas as pd

plt.rcParams.update({"font.size": 15})

with open("scraped_3000.json", "r") as f:
    data = json.load(f)
    posts = data["data"]

filtered_posts = [
    "1630836060-4614769001886736",
    "1631004126-4620151484681821",
    "1631192400-4626827824014187",
    "1631688990-4645066212190348",
    "1631700341-4645448802152089",
    "1635503770-4785797744783860",
    "1635503770-4785797744783860",
    "1641978382-5043290192367946",
    "1650031200-5332122233484739",
    "1650117600-5332340606796235",
    "1650958055-5355689497794679",
    "1650958055-5355689497794679",
    "1651060830-5369314033098892",
    "1651060830-5369314033098892",
    "1651060830-5369314033098892",
    "1651060830-5369314033098892",
    "1651082401-5369415929755369",
    "1651082401-5369415929755369",
    "1651989603-5391219534241675",
    "1652108400-5402442919786003",
    "1652382000-5410976215599340",
    "1652900400-5422554701108158",
    "1653040800-5431470190216609",
    "1653213600-5431570986873196",
    "1654608178-5487801004583527",
    "1654846208-5493847973978830",
    "1657613160-5585137771516516",
    "1661583538-5714065778623714",
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
# list_months = sorted(set(months_string), key=months_string.index)
# num_months = len(list_months)

df = pd.DataFrame(dates, columns=["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df = df.groupby([df["year"], df["month"]]).count()
df.columns = ["count"]
df.loc[(2021, 11), :] = int(0)
df.loc[(2021, 12), :] = int(0)
df.loc[(2022, 2), :] = int(0)
df.loc[(2022, 3), :] = int(0)
df.sort_index(inplace=True)
df["count"] = df["count"].astype(int)

ax = df.plot(
    kind="barh",
    figsize=(10, 5),
    # title='Verteilung der Beitrage "Homeland Nature Frame"',
    xlabel="Anzahl an Beiträgen",
    ylabel="Monat",
)


ax.locator_params(axis="y", nbins=num_months)
ax.set_yticklabels(list_months)

# ax.set_xlabel("Monat")
# ax.set_ylabel("Anzahl an Beiträgen")
# ax.set_title("Anzahl an gefilterten Beiträgen pro Monat")

# ax.legend(["Gefilterte Beiträge"])
ax.invert_yaxis()
plt.bar_label(ax.containers[0], fmt=" (%d)", label_type="edge")

ax.get_legend().remove()
# TODO: add title
# TODO: change legend
# plt.subplots_adjust(bottom=0.2)
plt.show()
