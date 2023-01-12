import pandas as pd
import re
import matplotlib.pyplot as plt

file_name = 'vacancies_with_skills.csv'
vacancy = ['Web-разработчик','web develop', 'веб разработчик', 'web разработчик', 'web programmer', 'web программист', 'веб программист', 'битрикс разработчик', 'bitrix разработчик', 'drupal разработчик', 'cms разработчик', 'wordpress разработчик', 'wp разработчик', 'joomla разработчик', 'drupal developer', 'cms developer', 'wordpress developer', 'wp developer', 'joomla developer']

df = pd.read_csv(file_name, low_memory=False)
df = df.dropna(subset='key_skills')
df['Год'] = df['published_at'].str.partition('-')[0].astype(int)

df_this_job = df.loc[df['name'].str.contains(vacancy[0], flags=re.IGNORECASE, regex=True)]
for i in range(len(vacancy) - 1):
    df_t = df.loc[df['name'].str.contains(vacancy[i + 1], flags=re.IGNORECASE, regex=True)]
    df_this_job = pd.concat([df_this_job, df_t])

key_skills = df_this_job['key_skills'].tolist()
for i in range(len(key_skills)):
    key_skills[i] = key_skills[i].split('\n')

skills_dict = dict()

for skills in key_skills:
    for skill in skills:
        if skill in skills_dict:
            skills_dict[skill] = skills_dict[skill] + 1
        else:
            skills_dict[skill] = 1

skills_df = pd.DataFrame.from_dict(skills_dict, orient='index', columns=['Кол-во'])
skills_df.index.rename('Навык', inplace=True)
skills_df = skills_df.sort_values(by=['Кол-во'], ascending=False).head(10)
# print(skills_df)
top10 = skills_df.index.values.tolist()
# print(top10)
key_skillses = []
for i in range(2015, 2023):
    df = df_this_job.loc[df_this_job['Год'] == i]
    key_skills = df['key_skills'].tolist()
    key_skillses.append(key_skills)

table = pd.DataFrame()
for key_skills in key_skillses:
    for i in range(len(key_skills)):
        key_skills[i] = key_skills[i].split('\n')

    skills_dict = dict()

    for skills in key_skills:
        for skill in skills:
            if skill in skills_dict and skill in top10:
                skills_dict[skill] = skills_dict[skill] + 1
            else:
                skills_dict[skill] = 1

    df = pd.DataFrame.from_dict(skills_dict, orient='index', columns=['Кол-во'])
    df.index.rename('Навык', inplace=True)
    df = df.reset_index()
    df = df.sort_values(by=['Кол-во'], ascending=False).head(10)
    res = (df
           .assign(n=df.groupby("Навык").cumcount())
           .pivot_table(index="n", columns="Навык", values="Кол-во")
           .rename_axis(None))
    table = pd.concat([table, res])

table.reset_index()
table['Год'] = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

ax = table.plot(x='Год', y=top10)
fig = ax.get_figure()
fig.savefig('skills_graph.png', dpi=300)
for skill in top10:
    text_file = open(f"{skill}.html", "w", encoding="utf-8")
    df = pd.concat([table['Год'], table[skill]], axis=1)
    text_file.write(df.to_html())
    text_file.close()
