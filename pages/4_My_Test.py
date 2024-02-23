import streamlit as st

# nice!
st.markdown("""
    <style>
    .stDateInput, .stSlider, .stTextInput {
        display: inline-flex;
    }
    </style>
""", unsafe_allow_html=True)

st.write("## Marketing Cloud Data Integration")

data_extension_key = st.text_input("Data Extension External Key", placeholder="Enter from pre created marketing cloud data extension")

companies = st.multiselect(
    'What companies are you targeting?',
    ['All', 'All EAP', 'All HPI', '1884','4thdistricthealthfund','7-11','8451','aag','abbvie','accenture','accompanyhealth','aci','advantest','affirm','ahern','ahn','airbnb','airproducts','akamai','altec','alteryx','altria','amazon','amentum','amerihealthcaritas','amesconstruction','amex','amgen','amys','anaplan','anduril','apache','apogee','apple','appliedintuition','aps','aristocrat','arm','arnoldporter','arthrex','asurion','att','attunion','autodesk','avalonbay','axaxl','babson','bah','bain','bbh','bbins','bcg','beaconhill','belmont','benesch','biomarin','bitly','bloomenergy','bluepearlvet','bluepearlvet-2','bmc','bms','boa','bolthouse','bounteous','bri','brookfield','brunswick','bswqa','businessgrouponhealth','caes','campos','capitalgroup','caresource-employee','cargill','carhartt','carlisle','carpenterbenefits','celanese','cgi','cgsh','chanel','childrensmn','chk','choiceplus','chr','citadel','cityofnh','clancytheys','clow','cmebenefits','cmegroup','cmg','cmsu','cnhindustrial','cocmeap','coeurmining','coh','comcast','comingsoon','commonspirit','coned','confluent','connection','continentalresources','convoy','corcept','corelogic','coterra','cottagehealth','cowen','cozen','cpi','crain','crosby','crowncastle','cruise','crystald','csl','cummins','curia','currangroup','davita','dci','dell','devon','devoted','discovery','dominos','draftkings','drizly','dupont','ebay','efe','eighteleven','elastic','electronicarts','emihealth','empower','enterprisebenefits','enviroserve','eog','epc','etsy','evercore','everi','everlyhealth','evolent','expediagroup','experience','eyassist','facebook','faegredrinker','faithtechinc','fenwick','fidelity','firstbank','fivebelow','flywire','foc','ford','fordhourly','foundationmedicine','freenome','frontgrade','frost','gap','gartner','genesys','genuine','gfo','ghd','gilead','godaddy','goodwillky','google','gray','greylock','greystone','harcros','harrisassoc','harristeeter','haynesboone','hdfowler','healthyreyes','heb','heffgroup','hfsinclair','higginbotham','hilton','hingehealth','hklaw','hmnam','holman','hologic','hosparushealth','hrblock','hudson','humaninterest','hunt','ibm','icumedical','igs','iheartmedia','illumina','indg','indivior','informatica','inmar','inova','internationalpaper','intuit','intuitive','intuit-seasonal','irhythm','iss','ivp','jazz','jedunn','juullabs','kbr','keysighttechnologies','kippnorcal','kpncal','kroger','kyrene','landolakes','lendingclub','lendlease','levi','lilly','linde','linkedin','livent','local4funds','lockton','lpl','lululemon','lyft','lyra','lyrians-2','manna','mapbox','marriott','marvell','masterbrand','mathworks','maxar','mcdonalds','mckinsey','medtronic','mentallyfit','merck','mercury','merrick','mfs','mgb','mgbhealthplan','milliman','mimeo','momentive','monday','morganstanley','mosaic','motiva','motive','mtb','musd','mycmscommunity','myucship','nationwidechildrens','natixiscib','natixisim','nclh','neibenefits','netapp','netflix','netskope','newport','nextera','niagara','nike','nikeathletehealth','northwesternmutual','ntec','nuro','nus','oaktree','oceanspray','ohiohealth','onedigital','oneok','onsemi','organon','orix','osu','otsuka','overlake','ovintiv','ovivowater','oxy','page','palantir','paloaltonetworks','patientpoint','paulweiss','pb','pcl','pelican','peloton','pennmutual','peraton','perkinscoie','phelpshealth','philasd','phoenixcontact','pillsburylaw','pimco','pinterest','pjm','pjtpartners','plastipak','plug','portmadisonenterprises','prologis','prudential','psjh','psych','purestorage','qualcomm','qualcomm-16eap','quanterix','rangeresources','ravago','rbfcu','recology','redbull','reddit','redventures','reedsmith','refactor219','renesas','rhbarringer','riteaid','rjet','roblox','roche','rogersbh','roseburg','rvohealth','ryanspecialty','saif','salesforce','salk','savage','schaeffler','schnitzer','schrodinger','sea','seismic','sempra','sequoia','servicenow','shell','sheppardmullin','shure','sibanyestillwater','skadden','skywater','smartsheet','smiths','snap','snowflake','solari','spacex','sparktx','specialized','square','sra','srp','ssfcu','ssi','stanfordchildrens','starbucks','stripe','stryker','suffolk','sunopta','superior','superradiatorcoils','sutrobio','swinomish','swn','symetra','synopsys','talosenergy','tap','terray','tesla','thc','thehartford','thoughtworks','thrive','tiktok','toasttab','towersemi','trace3','tronox','tti','twe','twilio','ualocal469','uber','uberfreight','umn','unity','urbn','usc','ussteel','vanderbilt','vanguard','vca','vca-2','velaw','vericast','veritas','veteransunited','vf','vimeo','virginiamason','vituity','vizient','vmware','voya','vytalogywellness','walmart','wasteconnections','wbd','welbe','wellington','westlake','wework','wex','weyerhaeuser','woodstream','workday-global','wpcu','wtw','yelp','zillow','ziprecruiter','zoetis','zoom','zscaler'],
    [])

source = st.radio(
    "What source of email addresses?",
    ["Eligibility", "Registration", "Eligibility and Registration"])

st.write("#### Target cohort options:")

min_age = st.slider("Minimum age", min_value=0, max_value=100, value=18)

on_latest_elig = st.checkbox("On Latest Eligibility File", value = True)
only_employees = st.checkbox("Only Employees", value = True)

hp_options = ['All']
# wow, this is cool... dynamic options
if "att" in companies:
    hp_options.append('ATT Anthem')
if "attunion" in companies:
    hp_options.append("ATT Union BCBS")
health_plans = st.multiselect(
    'Health Plans',
    hp_options,
    ['All'])

min_reg_date = st.date_input("Min Registration Date", value=None)
max_reg_date = st.date_input("Max Registration Date", value=None)

include_in_care = st.checkbox("Include members in care", value = True)
include_not_in_care = st.checkbox("Include members not in care", value = True)
exclude_future_appt = st.checkbox("Include members with future appointment", value = True)

st.write("  ")
st.write("  ")
submit = st.button("Submit")