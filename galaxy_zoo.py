#import pandas as pd
#import requests
#import webbrowser
#from multiprocessing import Pool

num_of_galaxy = 3000
possitions = []
table = pd.read_csv('GalaxyZoo1_DR_table2.csv', delimiter=',')
link = "http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx?"

def find_galaxy(i):
    if table.iat[i, 7] == max((table.loc[i])[4:13]):
        par = {'ra': table.iat[i, 1], 'dec': table.iat[i, 2], 'width':'600', 'height':'600','opt':'G'}
        response = requests.get(link, params = par)
            #webbrowser.open(response.url)
        with open('galaxy' + str(i) + '.jpeg', 'wb') as file: 
            file.write(response.content)
        
for i in range(num_of_galaxy):
    if table.iat[i, 7] == max((table.loc[i])[4:13]):
        possitions.append(i)

if __name__ == '__main__':
    pool = Pool(4)
    pool.map(find_galaxy, possitions)

