import pandas as pd
import re
import matplotlib.pyplot as plt


currency_to_rub = {
    "AZN": 35.68,
    "BYR": 23.91,
    "EUR": 59.90,
    "GEL": 21.74,
    "KGS": 0.76,
    "KZT": 0.13,
    "RUR": 1,
    "UAH": 1.64,
    "USD": 60.66,
    "UZS": 0.0055,
}

# file_name = input('Введите название файла: ')
# vacancy = input('Введите название профессии: ')
file_name = 'vacancies_with_skills.csv'
vacancy = ['Web-разработчик','web develop', 'веб разработчик', 'web разработчик', 'web programmer', 'web программист', 'веб программист', 'битрикс разработчик', 'bitrix разработчик', 'drupal разработчик', 'cms разработчик', 'wordpress разработчик', 'wp разработчик', 'joomla разработчик', 'drupal developer', 'cms developer', 'wordpress developer', 'wp developer', 'joomla developer']

df = pd.read_csv(file_name, low_memory=False)
df = df.query("salary_currency in @currency_to_rub.keys()") \
    .assign(salary_currency=lambda x: x["salary_currency"].replace(currency_to_rub))
df['Средняя зарплата'] = (df.salary_from + df.salary_to) * df.salary_currency / 2
df = df.dropna(subset='Средняя зарплата')
df['Год'] = df['published_at'].str.partition('-')[0].astype(int)
df['Город'] = df['area_name']

df_this_job = df.loc[df['name'].str.contains(vacancy[0], flags=re.IGNORECASE, regex=True)]
for i in range(len(vacancy)-1):
    df_t = df.loc[df['name'].str.contains(vacancy[i+1], flags=re.IGNORECASE, regex=True)]
    df_this_job = pd.concat([df_this_job, df_t])

sal_year = df.groupby('Год').aggregate({'Средняя зарплата': "mean"})
sal_year['Средняя зарплата'] = sal_year['Средняя зарплата'].astype(int)
sal_count = df.groupby('Год').aggregate({'name': "count"}) \
    .rename(columns={"name": "Количество вакансий"})

sal_year_job = df_this_job.groupby('Год').aggregate({'Средняя зарплата': "mean"})
sal_year_job['Средняя зарплата'] = sal_year_job['Средняя зарплата'].astype(int)
sal_year_job = sal_year_job.rename(columns={"Средняя зарплата": f"Средняя зарплата - {vacancy[0]} "})

sal_count_job = df_this_job.groupby('Год').aggregate({'name': "count"}) \
    .rename(columns={"name": f"Количество вакансий - {vacancy[0]} "})

sal_vrate_city = df.groupby('Город').aggregate({'Средняя зарплата': "mean", 'name': 'count'}) \
    .rename(columns={'name': 'Доля вакансий'}) \
    .sort_values('Доля вакансий', ascending=False)
sal_vrate_city['Доля вакансий'] = (sal_vrate_city['Доля вакансий'] / (df['salary_currency'].count())).round(4)

vacancyRate_city = sal_vrate_city.loc[sal_vrate_city['Доля вакансий'] > 0.01] \
    .drop(['Средняя зарплата'], axis=1)

sal_vrate_city = sal_vrate_city.dropna(subset='Средняя зарплата')
sal_vrate_city['Средняя зарплата'] = sal_vrate_city['Средняя зарплата'].astype(int)

sal_city = sal_vrate_city.loc[sal_vrate_city['Доля вакансий'] > 0.01] \
    .drop(['Доля вакансий'], axis=1).rename(columns={'Средняя зарплата': 'Уровень зарплат'}) \
    .sort_values('Уровень зарплат', ascending=False)

sal_city_to_plot = sal_city.head(10)
sal_city_to_plot.reset_index(inplace=True)

vac_rate_to_plot = vacancyRate_city.head(10)
vac_rate_to_plot.reset_index(inplace=True)
vac_rate_to_plot.loc[len(vac_rate_to_plot.index)] = ['Другие',
                                                     1 - vac_rate_to_plot['Доля вакансий'].sum()]
vac_rate_to_plot.reset_index()








plt.pie(x=vac_rate_to_plot['Доля вакансий'], labels=vac_rate_to_plot['Город'], textprops={'fontsize': 14})
plt.tight_layout()
plt.savefig('4.png', dpi=300)

##### Таблички для востребованности
text_file = open(f"зп.html", "w")
text_file.write(sal_year.to_html())
text_file.close()
text_file = open(f"зпWebDev.html", "w")
text_file.write(sal_year_job.to_html())
text_file.close()
text_file = open(f"кол-воВакансий.html", "w")
text_file.write(sal_count.to_html())
text_file.close()
text_file = open(f"Кол-воВакWeb.html", "w")
text_file.write(sal_count_job.to_html())
text_file.close()




##### Таблички для /geography

text_file = open(f"geography1.html", "w")
text_file.write(sal_city.to_html())
text_file.close()
text_file = open(f"geography2.html", "w")
text_file.write(vacancyRate_city.to_html())
text_file.close()