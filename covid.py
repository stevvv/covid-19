'''
program created by steven
this program always taked the latest covid data from git
'''
import pandas as pd
import datetime
import matplotlib.pyplot as plt

try:
    date = datetime.date.today() - datetime.timedelta(days=0)
    date = date.strftime("%m-%d-%Y")
    url = 'http://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    path = '%s%s%s' %(url, date, '.csv')
    data_df= pd.read_csv(path, error_bad_lines=False)
except:
    date = datetime.date.today() - datetime.timedelta(days=1)
    date = date.strftime("%m-%d-%Y")
    url = 'http://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    path = '%s%s%s' %(url, date, '.csv')
    data_df= pd.read_csv(path, error_bad_lines=False)
data_df = data_df[['Country_Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
data_df= data_df.groupby('Country_Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()
f20_df = data_df.sort_values(['Confirmed'], ascending=True).tail(20)
f20_df=f20_df[f20_df['Country_Region'] != 'US']
fig, ax = plt.subplots()
plt.style.use('ggplot')
def make_plot(axes, x, y, color, xlabel, ylabel,label, bottom=None ):
    axes.bar(x, y, label=label, bottom=bottom, alpha=0.8, color=color, width=0.6)
    axes.set_xlabel(xlabel,fontsize = 15)
    axes.set_ylabel(ylabel,fontsize = 15)
    axes.set_xticklabels(x, rotation=90)
    axes.set_title('COVID-19 Visualization', fontsize = 18)
       
make_plot(ax,f20_df.Country_Region,f20_df['Active'], 'red', 'Top 20 Countries', 'Number of Cases', 'Active')
# ax2 = ax.twinx()
make_plot(ax,f20_df.Country_Region,f20_df['Recovered'], 'green', 'Top 20 Countries', 'Number of Cases', 'Recovered', f20_df['Active'])
# make_plot(ax,f20_df.Country_Region,f20_df['Confirmed'], 'yellow', 'Top 20 Countries', 'Number of Cases', 'Confirmed')
make_plot(ax,f20_df.Country_Region,f20_df['Deaths'], 'black', 'Top 20 Countries', 'Number of Cases', 'Deaths', f20_df['Active']+f20_df['Recovered'])
ax.legend()
ax.locator_params(tight=True, nbins=20)
plt.grid(axis = 'y', linestyle = '-')
fig.tight_layout()
plt.show()
