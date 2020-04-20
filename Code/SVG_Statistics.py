import pandas as pd 
data = pd.read_csv(r'C:\Users\admin\Documents\consumption.csv')
data
progress = data.drop(columns = ['Explanations', 'Unnamed: 6', 'Unnamed: 8', 'Unnamed: 9'])
progress
new_data = progress.dropna()
new_data
import matplotlib.pyplot as plt
new_data = new_data.rename(index ={'0.0': 'unemployed', '1.0':'Managers', '2.0': 'Professionals', '3.0':'Technicians', '4.0':'Clerical Workers', '5.0':'Service Workers', '6.0':'Agriculture, forestry, fisheries workers', '7.0':'Craft and trade workers', '8.0':'Plant and machine operators', '9.0':'Elementary occupations', '10.0':'Military', '11.0': 'Students', '12.0':'Retired'})
new_data.rename(index={'M':'Male', 'F':'Female'})
new_data['Gender'] = new_data.Gender.str.strip()
males = (new_data['Gender']=='M').sum()
females = (new_data['Gender']=='F').sum()
genders = [males, females]
plt.pie(genders, labels= ['Males', 'Females'], colors= ['royalblue', 'red'], shadow = True, autopct= '%1.1f%%'); plt.title('Frequency of Males and Females');
unemployed = (new_data['Occupational category']==0.0).sum()
managers = (new_data['Occupational category']==1.0).sum()
professionals = (new_data['Occupational category']==2.0).sum()
technicians = (new_data['Occupational category']==3.0).sum()
clerical_workers = (new_data['Occupational category']==4.0).sum()
service_workers = (new_data['Occupational category']==5.0).sum()
AFF = (new_data['Occupational category']==6.0).sum()
craft_and_trade = (new_data['Occupational category']==7.0).sum()
plant_and_machine = (new_data['Occupational category']==8.0).sum()
elementary_occ = (new_data['Occupational category']==9.0).sum()
military = (new_data['Occupational category']==10.0).sum()
students = (new_data['Occupational category']==11.0).sum()
retired = (new_data['Occupational category']==12.0).sum()
occupational_category = [unemployed, managers,professionals,technicians, clerical_workers, service_workers, AFF, craft_and_trade, plant_and_machine, elementary_occ, military, students, retired]  
print(occupational_category)
print(genders)
occ_gen_stat = pd.DataFrame(new_data.groupby('Occupational category')['Gender'].value_counts())
occ_gen_stat.loc[0.0]
occ_gen_stat.columns = ['Sum of Genders']
occ_gen_stat= occ_gen_stat.reset_index(level=['Occupational category', 'Gender'])
occ_gen_stat
occ_gen_stat = occ_gen_stat.sort_values(by= ['Gender', 'Occupational category'],ascending=True)
occ_gen_stat
occ_gen_stat= occ_gen_stat.reset_index(drop=True)
occ_gen_stat
occ_gen_stat['Occupational category'] = occ_gen_stat['Occupational category'].replace(to_replace= [0.0, 1.0, 2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0], value= ['unemployed', 'Managers', 'Professionals', 'Technicians', 'Clerical Workers', 'Service Workers', 'Agriculture, forestry, fisheries workers', 'Craft and trade workers', 'Plant and machine operators', 'Elementary occupations', 'Military', 'Students', 'Retired'])
occ_gen_stat
male_occ = occ_gen_stat['Occupational category'].iloc[12:26]
male_occ = occ_gen_stat['Occupational category'].iloc[12:26]
male_occ_char = plt.barh(male_occ, male_sum, color= 'royalblue'); plt.ylabel(''); plt.xlabel('Sum of Male Workers'); plt.title('Number of Male Workers based on Occupation');plt.xticks(rotation= 0);
male_evolve = occ_gen_stat[['Occupational category', 'Sum of Genders']].iloc[12:26]
male_evolution = pd.DataFrame(male_evolve)
male_evolution = male_evolution.rename(columns={"Sum of Genders": "Sum of Males"})
male_evolution = male_evolution.reset_index().drop(columns= 'index')
male_evolution
fem_evolve = occ_gen_stat[['Occupational category', 'Sum of Genders']].iloc[0:12]
fem_evolution = pd.DataFrame(fem_evolve)
fem_evolution = fem_evolution.rename(columns = {'Sum of Genders': 'Sum of Females'})
fem_evolution
ultra_sync = pd.DataFrame({'Occupational category': ['Military'], 'Sum of Females': [0]})
fem_evolution = fem_evolution.append(ultra_sync).reset_index().drop(columns= 'index')
male_evolution = male_evolution.reset_index().drop(columns='index')
evolution = pd.merge(male_evolution, fem_evolution)
evolution
import numpy as np
fig= plt.figure()
ax= fig.add_subplot(111)
ax2 = ax.twinx()
width=0.4

ultra_chart = evolution['Sum of Males'].plot(kind='bar', color='blue', ax= ax, width= width, position=1); evolution['Sum of Females'].plot(kind= 'bar', color='red', ax= ax, width=width, position=0);
plt.xticks(range(13),['unemployed', 'Managers', 'Professionals', 'Technicians', 'Clerical Workers', 'Service Workers', 'Agriculture, forestry, fisheries workers', 'Craft and trade workers', 'Plant and machine operators', 'Elementary occupations', 'Military', 'Students', 'Retired']); 
plt.yticks([], []);
plt.title("Male and Female Workers based on Occupation");
plt.show()
########################
fem_occ= occ_gen_stat['Occupational category'].iloc[0:12]
fem_sum= occ_gen_stat['Sum of Genders'].iloc[0:12]
fem_occ_char = plt.barh(fem_occ, fem_sum, color= 'red'); plt.ylabel(''); plt.xlabel('Sum of Female Workers'); plt.title('Number of Female Workers based on Occupation');plt.xticks(rotation= 0); plt.show()
#################################################
#Now to examine the results of male and female workers and their occupation based on the foods that they eat:
occ_gen_scon = pd.DataFrame(new_data.groupby(['Gender', 'Occupational category'])['SC consume'].value_counts())
occ_gen_scon.columns = ['Sum of  SC Consumptions']
occ_gen_scon= occ_gen_scon.reset_index(level=['Gender', 'SC consume', 'Occupational category'])
occ_gen_scon = occ_gen_scon.sort_values(by= ['SC consume', 'Gender', 'Occupational category'],ascending=True)
occ_gen_scon= occ_gen_scon.reset_index(drop=True)
occ_gen_scon['Occupational category'] = occ_gen_scon['Occupational category'].replace(to_replace= [0.0, 1.0, 2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0], value= ['unemployed', 'Managers', 'Professionals', 'Technicians', 'Clerical Workers', 'Service Workers', 'Agriculture, forestry, fisheries workers', 'Craft and trade workers', 'Plant and machine operators', 'Elementary occupations', 'Military', 'Students', 'Retired'])
occ_gen_scon['SC consume'] = occ_gen_scon['SC consume'].replace(to_replace= [0,1], value= ['No','Yes'])
print(occ_gen_scon)
######################################################
occ_gen_hcon = pd.DataFrame(new_data.groupby(['Gender', 'Occupational category'])['HW consume'].value_counts())
occ_gen_hcon.columns = ['Sum of  HW Consumptions']
occ_gen_hcon= occ_gen_hcon.reset_index(level=['Gender', 'HW consume', 'Occupational category'])
occ_gen_hcon = occ_gen_hcon.sort_values(by= ['HW consume', 'Gender', 'Occupational category'],ascending=True)
occ_gen_hcon= occ_gen_hcon.reset_index(drop=True)
occ_gen_hcon['Occupational category'] = occ_gen_hcon['Occupational category'].replace(to_replace= [0.0, 1.0, 2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0], value= ['unemployed', 'Managers', 'Professionals', 'Technicians', 'Clerical Workers', 'Service Workers', 'Agriculture, forestry, fisheries workers', 'Craft and trade workers', 'Plant and machine operators', 'Elementary occupations', 'Military', 'Students', 'Retired'])
occ_gen_hcon['HW consume'] = occ_gen_hcon['HW consume'].replace(to_replace= [0,1], value= ['No','Yes'])
print(occ_gen_hcon)
#########################################################
sc_gen_zoom = pd.merge(right= occ_gen_scon, left= occ_gen_stat)
sc_gen_zoom = sc_gen_zoom.sort_values(['SC consume','Gender']).reset_index().drop(columns= 'index')
print(sc_gen_zoom)
##############################################################
fem_con_nosc = sc_gen_zoom[0:12]
fem_con_nosc = fem_con_nosc.reset_index().drop(columns= ['index'])
yin_sync = pd.DataFrame({'Occupational category': ['Military'], 'Gender': ['F'], 'Sum of Genders':[0], 'SC consume': ['No'], 'Sum of  SC Consumptions': [0]})
fem_con_nosc = fem_con_nosc.append(yin_sync).reset_index().drop(columns= 'index')
print(fem_con_nosc)
####################################################################
fem_con_nosc = fem_con_nosc.reindex([0,1,2,3,4,5,6,7,8,9,12,10,11])
fem_con_nosc = fem_con_nosc.reset_index().drop(columns= ['index'])
fem_con_nosc
plt.bar(fem_con_nosc['Occupational category'], fem_con_nosc['Sum of  SC Consumptions'], color= 'darkred'); plt.xticks(rotation=90); plt.title('Negative consumption of Small Cetaceans (F)');
plt.show()
##########################################################################
fem_con_yessc = sc_gen_zoom[24:35]
fem_con_yessc = fem_con_yessc.reset_index().drop(columns= ['index'])
yinny_sync = pd.DataFrame({'Occupational category': ['Military', 'Craft and trade workers'], 'Gender': ['F', 'F'], 'Sum of Genders':[0,0], 'SC consume': ['Yes','Yes'], 'Sum of  SC Consumptions': [0,0]})
fem_con_yessc = fem_con_yessc.append(yinny_sync).reset_index().drop(columns= 'index')
fem_con_yessc
fem_con_yessc = fem_con_yessc.reindex([0,1,2,3,4,5,6,12, 7,8, 11, 9, 10])
fem_con_yessc= fem_con_yessc.reset_index().drop(columns= ['index'])
fem_con_yessc
plt.bar(fem_con_yessc['Occupational category'], fem_con_yessc['Sum of  SC Consumptions'], color= 'red'); plt.xticks(rotation=90); plt.title('Positive consumption of Small Cetaceans (F)');
plt.show()
########################################################################
fig= plt.figure()
ax= fig.add_subplot(111)
ax2 = ax.twinx()
width=0.4

yin_chart = fem_con_yessc['Sum of  SC Consumptions'].plot(kind='bar', color='red', ax= ax, width= width, position=1); fem_con_nosc['Sum of  SC Consumptions'].plot(kind= 'bar', color='darkred', ax= ax, width=width, position=0);
plt.xticks(range(13),['unemployed', 'Managers', 'Professionals', 'Technicians', 'Clerical Workers', 'Service Workers', 'Agriculture, forestry, fisheries workers', 'Craft and trade workers', 'Plant and machine operators', 'Elementary occupations', 'Military', 'Students', 'Retired']); 
plt.yticks([], []);
plt.title("Positive and Negative Consumption of Small Cetaceans (F)");
plt.show()
####################################################################
male_con_nosc = sc_gen_zoom[12:24]
male_con_nosc = male_con_nosc.reset_index().drop(columns=['index'])
yangy_sync = pd.DataFrame({'Occupational category': ['Military'], 'Gender': ['M'], 'Sum of Genders':[0], 'SC consume': ['No'], 'Sum of  SC Consumptions': [0]})
male_con_nosc = male_con_nosc.append(yangy_sync).reset_index().drop(columns= 'index')
male_con_nosc
male_con_nosc = male_con_nosc.reindex([0,1,2,3,4,5,6,7,8, 9, 12, 10,11])
male_con_nosc= male_con_nosc.reset_index().drop(columns= ['index'])
male_con_nosc
plt.bar(male_con_nosc['Occupational category'], male_con_nosc['Sum of  SC Consumptions'], color= 'darkblue'); plt.xticks(rotation=90); plt.title('Negative consumption of Small Cetaceans (M)');
plt.plot()
##################################################################
male_con_yessc = sc_gen_zoom[35:48]
male_con_yessc = male_con_yessc.reset_index().drop(columns=['index'])
male_con_yessc
male_yes_consc= plt.bar(male_con_yessc['Occupational category'], male_con_yessc['Sum of  SC Consumptions'], color= 'blue'); plt.xticks(rotation=90); plt.title('Positive consumption of Small Cetaceans (M)');
fig= plt.figure()
ax= fig.add_subplot(111)
ax2 = ax.twinx()
width=0.4

yang_chart = male_con_yessc['Sum of  SC Consumptions'].plot(kind='bar', color='blue', ax= ax, width= width, position=1); male_con_nosc['Sum of  SC Consumptions'].plot(kind= 'bar', color='darkblue', ax= ax, width=width, position=0);
plt.xticks(range(13),['unemployed', 'Managers', 'Professionals', 'Technicians', 'Clerical Workers', 'Service Workers', 'Agriculture, forestry, fisheries workers', 'Craft and trade workers', 'Plant and machine operators', 'Elementary occupations', 'Military', 'Students', 'Retired']); 
plt.yticks([], []);
plt.title("Positive and Negative Consumption of Small Cetaceans (M)");
plt.show()
############################################################################
hw_gen_consume = pd.merge(right= occ_gen_hcon, left= occ_gen_stat)
hw_gen_consume = hw_gen_consume.sort_values(['HW consume','Gender']).reset_index().drop(columns= 'index')
fem_con_nohw = hw_gen_consume[0:12]
fem_con_nohw = fem_con_nohw.reset_index().drop(columns= ['index'])
light_sync = pd.DataFrame({'Occupational category': ['Military'], 'Gender': ['F'], 'Sum of Genders':[0], 'HW consume': ['No'], 'Sum of  HW Consumptions': [0]})
fem_con_nohw = fem_con_nohw.append(light_sync).reset_index().drop(columns= 'index')
fem_con_nohw 
fem_con_nohw = fem_con_nohw.reindex([0,1,2,3,4,5,6,7,8,9,12,10,11])
fem_con_nohw = fem_con_nohw.reset_index().drop(columns= ['index'])
fem_con_nohw
plt.bar(fem_con_nohw['Occupational category'], fem_con_nohw['Sum of  HW Consumptions'], color= 'darkred'); plt.xticks(rotation=90); plt.title('Negative consumption of Humpback Whale (F)');
plt.show()
############################################################################
fem_con_yeshw = hw_gen_consume[25:35]
fem_con_yeshw = fem_con_yeshw.reset_index().drop(columns= ['index'])
lightness_sync = pd.DataFrame({'Occupational category': ['Military', 'Clerical Workers', 'Craft and trade workers'], 'Gender': ['F', 'F', 'F'], 'Sum of Genders':[0,0,0], 'HW consume': ['Yes','Yes', 'Yes'], 'Sum of  HW Consumptions': [0,0, 0]})
fem_con_yeshw = fem_con_yeshw.append(lightness_sync).reset_index().drop(columns= 'index')
fem_con_yeshw 
fem_con_yeshw = fem_con_yeshw.reindex([0,1,2,3,11,4,5,12,6,7,10,8,9])
fem_con_yeshw= fem_con_yeshw.reset_index().drop(columns= ['index'])
fem_con_yeshw
plt.bar(fem_con_yeshw['Occupational category'], fem_con_yeshw['Sum of  HW Consumptions'], color= 'red'); plt.xticks(rotation=90); plt.title('Positive consumption of Humpback Whale (F)');
plt.show()
###############################################################################
fig= plt.figure()
ax= fig.add_subplot(111)
ax2 = ax.twinx()
width=0.4

light_chart = fem_con_yeshw['Sum of  HW Consumptions'].plot(kind='bar', color='red', ax= ax, width= width, position=1); fem_con_nohw['Sum of  HW Consumptions'].plot(kind= 'bar', color='darkred', ax= ax, width=width, position=0);
plt.xticks(range(13),['unemployed', 'Managers', 'Professionals', 'Technicians', 'Clerical Workers', 'Service Workers', 'Agriculture, forestry, fisheries workers', 'Craft and trade workers', 'Plant and machine operators', 'Elementary occupations', 'Military', 'Students', 'Retired']); 
plt.yticks([], []);
plt.title("Positive and Negative Consumption of Humpback Whale (F)");
plt.show()
###############################################################################
male_con_nohw = hw_gen_consume[12:25]
male_con_nohw = male_con_nohw.reset_index().drop(columns=['index'])
male_con_nohw
male_no_conhw = plt.bar(male_con_nohw['Occupational category'], male_con_nohw['Sum of  HW Consumptions'], color= 'darkblue'); plt.xticks(rotation=90); plt.title('Negative consumption of Humpback Whale (M)');
male_con_yeshw = hw_gen_consume[35:48]
male_con_yeshw = male_con_yeshw.reset_index().drop(columns=['index'])
male_con_yeshw
male_yes_conhw= plt.bar(male_con_yeshw['Occupational category'], male_con_yeshw['Sum of  HW Consumptions'], color= 'blue'); plt.xticks(rotation=90); plt.title('Positive consumption of Humpback Whale (M)');
plt.show()
################################################################################
fig= plt.figure()
ax= fig.add_subplot(111)
ax2 = ax.twinx()
width=0.4

dark_chart = male_con_yeshw['Sum of  HW Consumptions'].plot(kind='bar', color='blue', ax= ax, width= width, position=1); male_con_nohw['Sum of  HW Consumptions'].plot(kind= 'bar', color='darkblue', ax= ax, width=width, position=0);
plt.xticks(range(13),['unemployed', 'Managers', 'Professionals', 'Technicians', 'Clerical Workers', 'Service Workers', 'Agriculture, forestry, fisheries workers', 'Craft and trade workers', 'Plant and machine operators', 'Elementary occupations', 'Military', 'Students', 'Retired']); 
plt.yticks([], []);
plt.title("Positive and Negative Consumption of Humpback Whale (M)");
plt.show()
###########################################################################
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)






