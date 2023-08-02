import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from datetime import datetime, timedelta
import pandas as pd

with open("scraped_3000.json", "r") as f:
    data = json.load(f)
    posts = data["data"]

plt.rcParams.update({"font.size": 15})


filtered_posts = [
    "1630511642-4602261543137482",
    "1630491206-4601634526533517",
    "1630579823-4604859036211066",
    "1630913433-4608638082499828",
    "1630931697-4617613244935645",
    "1631186626-4626708274026142",
    "1631375930-4633774959986140",
    "1631430026-4629723507057952",
    "1631559603-4639424432754526",
    "1631612889-4642269909136645",
    "1631633430-4642645659099070",
    "1631646002-4639663306063972",
    "1631799647-4649159748447661",
    "1631887216-4652143804815922",
    "1631898038-4652254848138151",
    "1631977205-4652205928143043",
    "1632294095-4667707126592923",
    "1632391257-4671375629559406",
    "1632426320-4668812103149092",
    "1632565608-4678497628847206",
    "1632672041-4682831081747194",
    "1633240859-4702219119808390",
    "1633355070-4708131769217125",
    "1633445730-4710237805673188",
    "1633618802-4716382468392055",
    "1633697497-4719654928064809",
    "1633784442-4719470334749935",
    "1634201461-4738456119518023",
    "1634715019-4756954817668153",
    "1634727614-4757297444300557",
    "1635257903-4776254165738218",
    "1635332495-4779075798789388",
    "1635528600-4786355651394736",
    "1635579031-4785951884768446",
    "1635611401-4786463154717319",
    "1635701401-4786438674719767",
    "1635706812-4785586534804981",
    "1635781744-4795814437115524",
    "1635861602-4798232566873711",
    "1636210802-4810966892266945",
    "1636272922-4813848701978764",
    "1636282500-4812218545475113",
    "1636293602-4814301818600119",
    "1636399481-4818653314831636",
    "1636468120-4820818101281824",
    "1636480801-4821413074555660",
    "1636717640-4830525663644401",
    "1637066247-4843401659023468",
    "1637147343-4846516438711990",
    "1637172018-5319016048115683",
    "1637321401-4853538424676458",
    "1637483458-4847167461980221",
    "1637496784-4859949304035370",
    "1637508609-4850751251621842",
    "1637523001-4854236361273331",
    "1637591405-4863285593701741",
    "1637656240-4843773968986237",
    "1637932405-4876660639030903",
    "1638205228-4886449794718654",
    "1638257123-4888847464478887",
    "1638343640-4892204027476564",
    "1638364769-4893075200722780",
    "1638386880-4892757934087840",
    "1638463090-4897088296988137",
    "1638471301-4897152356981731",
    "1638543302-4899971543366479",
    "1638716402-4899431413420492",
    "1638798901-4910022755694691",
    "1639040775-4919420461421587",
    "1639074602-4920314051332228",
    "1639137307-4923113534385613",
    "1639147962-4923704957659804",
    "1639162500-4923677347662565",
    "1639397188-4932869070076726",
    "1639407302-4933207086709591",
    "1639559412-4938961316134168",
    "1639581055-4939838126046487",
    "1639666892-4944940418869591",
    "1639740600-4949159635114336",
    "1640092914-4968133999883566",
    "1640252449-4976537762376523",
    "1640697929-4998714730158826",
    "1640766602-4998767986820167",
    "1640803020-5002044629825836",
    "1641372797-5020631511300481",
    "1641639663-5032160833480882",
    "1641715200-5029383997091899",
    "1641754254-5029610870402545",
    "1642000613-5044148865615412",
    "1642142698-5050936558269976",
    "1642418918-5065334683496830",
    "1642442404-5065369323493366",
    "1642601736-5074949492535349",
    "1642622104-5074431622587136",
    "1642688817-5079557322074566",
    "1642772472-5083875721642726",
    "1642860000-5043526375677661",
    "1643029031-5097395383624093",
    "1643094000-5079372085426423",
    "1643131819-507888500765293",
    "1643188834-5105964466100518",
    "1643200200-5106306259399672",
    "1643288100-5110846088945689",
    "1643298901-5110982792265352",
    "1643372629-5115770771786554",
    "1643388900-5115564475140517",
    "1643529601-5115847068445591",
    "1643745602-5128915903805374",
    "1643894273-5135973263099638",
    "1643907602-5129027813794183",
    "1644226555-5128968343800130",
    "1644312324-5151760734854224",
    "1644415201-5155274057836225",
    "1644484986-5157937760903188",
    "1644583829-5161586187205012",
    "1644931346-5174170062613291",
    "1645020683-5177476495615981",
    "1645117202-5180479051982392",
    "1645551007-5196770540353243",
    "1645607755-5199202123443418",
    "1645632010-5199910800039217",
    "1645642822-5199238186773145",
    "1645726688-5203640372999593",
    "1645788059-5205630659467231",
    "1645808913-5206430289387268",
    "1645884006-5206523609377936",
    "1646148601-5217278458302451",
    "1646236804-5220222411341389",
    "1646331469-5223699167660380",
    "1646397000-5225713604125603",
    "1646564401-5206383632725267",
    "1646661601-5219779201385710",
    "1646761427-5236896933007270",
    "1646991983-5244666788896951",
    "1647072007-5244876005542696",
    "1647252781-5252780428085587",
    "1647333210-5255279357835694",
    "1647369000-5255983207765309",
    "1647432030-5258349567528673",
    "1647442801-5258501684180128",
    "1647505159-5260806000616363",
    "1647538201-5261068693923427",
    "1647592181-5263625243667772",
    "1647613843-5261664880530475",
    "1647673200-5264019776961652",
    "1647687833-5266536293376667",
    "1647936002-5264199053610391",
    "1647973977-5275054825858147",
    "1648022400-5274471522583144",
    "1648108801-5271935602836736",
    "1648204417-5281930948503868",
    "1648310402-5274427899254173",
    "1648324083-5285690964794533",
    "1648360801-5279336942096602",
    "1648386904-5279306478766315",
    "1648466100-5289935701036726",
    "1648548040-5292503344113295",
    "1648623600-5290270314336598",
    "1648654204-5295573980472898",
    "1648740607-5298240846872878",
    "1648822937-5301139009916395",
    "1648879201-5276822829014680",
    "1648901197-5279367928760170",
    "1650099635-5335125469851082",
    "1650279601-5300537279976568",
    "1650351601-5332389363458026",
    "1650375141-5348167501880212",
    "1650380400-5348132265217069",
    "1650477602-5350756844954611",
    "1650553201-5353373078026321",
    "1650564005-5353743857989243",
    "1650610801-5319756071388022",
    "1650628801-5355707594459536",
    "1650883630-5363666220330340",
    "1650892088-5363948953635400",
    "1650914666-5355747234455572",
    "1650978001-5366578616705767",
    "1650988800-5366707966692832",
    "1651138885-5371814082848887",
    "1651327200-5369260749770887",
    "1651413600-5374660742564221",
    "1651485601-5382380338458928",
    "1651507238-5382925441737751",
    "1651518025-5382917865071842",
    "1651593601-5385659384797690",
    "1651647600-5385639924799636",
    "1651672703-5388659751164320",
    "1651424401-5380431635320465",
    "1651820400-5391212730909022",
    "1651834800-5391244067572555",
    "1651914057-1024259534851348",
    "1652000400-5394179257279036",
    "1652119231-5403322476364714",
    "1652174492-5405076076189354",
    "1652283937-5408791305817831",
    "1652371496-5410971382266490",
    "1652450400-5413380928692202",
    "1652508000-5410696528960642",
    "1652533201-5410811505615811",
    "1652608502-5413796595317302",
    "1652619600-5405418912821737",
    "1652694901-5413817718648523",
    "1652799602-5425587040804924",
    "1652854111-5427713633925598",
    "1652870328-5428212927209002",
    "1652886000-5428453813851580",
    "1652965203-5431284776901817",
    "1652986800-5425261010837527",
    "1653156002-5434161863280775",
    "1653314404-5444372592259702",
    "1653328801-5434145913282370",
    "1653476401-5449502248413403",
    "1653505200-5444406638922964",
    "1653577201-5446789998684628",
    "1653717603-5446933595336935",
    "1653631200-5428014807228814",
    "1653731406-5458424320854529",
    "1653746402-5444389828924645",
    "1653822001-5431351000228528",
    "1653836400-5434255089938119",
    "1653894000-5431381400225488",
    "1653906997-5464747603555534",
    "1653925160-5465536850143276",
    "1653984688-5467493403280954",
    "1654012800-5470449379652023",
    "1654062973-5470189103011384",
    "1654322400-5473709565992671",
    "1654336500-5487699767926984",
    "1654351664-5479916902038604",
    "1654365602-5476626255701002",
    "1654452005-5476691345694493",
    "1654527602-5476812952348999",
    "1654592863-5487726121257682",
    "1654686098-5490512607645700",
    "1654763456-5491168657580095",
    "1654776007-5490635457633415",
    "1654882231-5490629444300683",
    "1654943453-5493852390645055",
    "1654954260-5496927210337573",
    "1654968659-5493412230689071",
    "1654973619-5500324773331150",
    "1655053217-5493840620646232",
    "1655105424-5496314490398845",
    "1655139601-5505212239509070",
    "1655194070-5507059735990987",
    "1655215202-5507706955926265",
    "1655235691-5508516485845312",
    "1655290661-5510200625676898",
    "1655391601-5507144705982490",
    "1655469773-5516147575082203",
    "1655547319-5518791464817814",
    "1655550778-5518909221472705",
    "1655559441-5519229444774016",
    "1655578701-5519964824700478",
    "1655625609-741436417278133",
    "1655643919-5522040581159569",
    "1655649691-5522281797802114",
    "1655734277-5524996214197339",
    "1655796565-5525135820850045",
    "1655834419-5527837460579881",
    "1655920859-5527831107247183",
    "1655976582-5530401433656817",
    "1656010807-5533522466678047",
    "1656062858-5530349326995361",
    "1656091859-5536159859747641",
    "1656142205-5533014043395556",
    "1656174602-5536718103025150",
    "1656319338-5544616058902021",
    "1656770401-5547594355270858",
    "1656828000-5556425147721112",
    "1656842100-5545037098859917",
    "1656856680-5556348274395466",
    "1656918001-5551047378258889",
    "1657014904-5556450421051918",
    "1657042279-5567771263253167",
    "1657130700-5570213243008969",
    "1657267624-5574638765899750",
    "1657279802-5574746919222268",
    "1657350005-5575268419170118",
    "1657360861-5577574512272842",
    "1657375082-5574960592534234",
    "1657436401-5574797852550508",
    "1657450801-5574931575870469",
    "1657638276-5586064464757180",
    "1657879819-5595241130506180",
    "1657897129-5596017693761857",
    "1657980002-5595528107144149",
    "1658148213-5604645646232395",
    "1658488855-5615581701805456",
    "1658566621-5617949624901997",
    "1658667300-5618630991500527",
    "1658736827-5622991681064458",
    "1658911471-5628230943873865",
    "1658988001-5628400600523566",
    "1659160833-5635905629773063",
    "1659261304-5633827176647575",
    "1659292411-5640100362686923",
    "1659434496-5644403932256566",
    "1659449048-5644936792203280",
    "1659515555-5647182285312064",
    "1659542557-5648233375206955",
    "1659765692-5655259037837722",
    "1659962304-5661248073905485",
    "1660114805-5666042383426054",
    "1660142609-5666961150000844",
    "1660374752-5674405795923046",
    "1660829084-5689356221094670",
    "1660891728-5691439574219668",
    "1660981384-5694480720582220",
    "1661328049-5705641096132849",
    "1661351745-5706447949385497",
    "1661413351-5708445355852423",
    "1661497202-5709248239105468",
    "1661670003-5712063358823956",
    "1661853544-5722715277758764",
    "1661866218-5723242524372706",
    "1661925603-5723985240965101",
    "1661931685-5725367694160189",
    "1662012000-5725743424122616",
    "1650454598-5350354721661490",
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
irrelevant_posts = [
    post
    for post in posts
    if post["text"] is not None
    and any(word.lower() in post["text"].lower() for word in search_token)
    and post["timestamp"] > datetime(2021, 9, 1).timestamp()
    and post["timestamp"] < datetime(2022, 8, 31).timestamp()
]
print(len(irrelevant_posts))
relevant_posts = [
    post
    for post in posts
    if post["text"] is not None
    and f"{str(post['timestamp'])}-{str(post['post_id'])}" not in filtered_posts
    and any(word.lower() in post["text"].lower() for word in search_token)
    and post["timestamp"] >= datetime(2021, 9, 1).timestamp()
    and post["timestamp"] <= datetime(2022, 8, 31).timestamp()
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
ax.margins(x=0.1)

# ax.legend(["Gefilterte Beiträge"])
ax.get_legend().remove()
# TODO: add title
# TODO: change legend
# plt.subplots_adjust(bottom=0.2)
plt.show()