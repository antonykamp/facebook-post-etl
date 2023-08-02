import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from datetime import datetime, timedelta
import pandas as pd

with open("scraped_3000.json", "r") as f:
    data = json.load(f)
    posts = data["data"]

filtered_posts = [
    "1630669193-4608152389215064",
    "1632056444-4652380351458934",
    "1632990901-4652162628147373",
    "1634814916-4760532993977002",
    "1635588118-4788991944464440",
    "1636446648-4798864030143898",
    "1636916401-4830887576941543",
    "1637433004-4854223637941270",
    "1639317300-4923471191016514",
    "1641216202-5017389054958060",
    "1641216202-5017389054958060",
    "1641494145-5027361217294177",
    "1644649201-5129036290460002",
    "1646071214-5214459301917700",
    "1646927702-5242433202453643",
    "1646927702-5242433202453643",
    "1648120215-5279292625434367",
    "1650639602-5355950941101868",
    "1651071600-5369353426428286",
    "1653228000-5422765814420380",
    "1655364600-5510103969019897",
    "1655364600-5510103969019897",
    "1656074975-5536301663066794",
    "1657000500-5564581840238776",
    "1657028517-5567021459994814",
    "1657613160-5585137771516516",
    "1657623901-5585449738151986",
    "1659276631-5639508836079409",
    "1661455328-5709896192374006",
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
        # title='Verteilung der Beitrage "New Frames"',
        xlabel="Anzahl an Beiträgen",
        ylabel="Monat",
    )
)


ax.locator_params(axis="y", nbins=num_months)
ax.set_yticklabels(list_months)
plt.bar_label(ax.containers[0], fmt=" (%d)", label_type="edge")

# ax.set_xlabel("Monat")
# ax.set_ylabel("Anzahl an Beiträgen")
# ax.set_title("Anzahl an gefilterten Beiträgen pro Monat")

# ax.legend(["Gefilterte Beiträge"])
ax.invert_yaxis()
ax.get_legend().remove()
# TODO: add title
# TODO: change legend
# plt.subplots_adjust(bottom=0.2)
plt.show()
