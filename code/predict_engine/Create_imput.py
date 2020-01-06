__author__      = "Jérôme Dewandre"


'''This function is aimed to select the data from the 'worktbl' and the 'tbl' after a certain date
Input : 
        Worktbl: The table in which the features are added
        Tbl: A talbe with the worktbl + the features 
        date: a date under the format : '2018-11-3'
Output : imput_data_work: the worktbl with data after date
         imput_data_tbl: the tbl with data after date
#Exemple of use:
#getimput(worktbl,tbl,'2018-11-3')
'''
def getimput(Worktbl,Tbl,date):

    indexes = Worktbl['date'] >= date
    imput_data_work = Worktbl.loc[indexes]
    imput_data_tbl = Tbl.loc[indexes]
    return imput_data_work.reset_index().drop('index', axis=1),imput_data_tbl.reset_index().drop('index', axis=1)



'''This function is aimed to select the data from the 'worktbl' and the 'tbl' after a certain date
Input : 
        Worktbl: The table in which the features are added
        Tbl: A talbe with the worktbl + the features 
        date: a date under the format : '2018-11-3'
Output : imput_data_work: the worktbl with data after date
         imput_data_tbl: the tbl with data after date
#Exemple of use:
#getimput(worktbl,tbl,'2018-11-3')
'''
def getexercise_Of_yesterday(Worktbl,Tbl,date):

    indexes = Worktbl['date'] == date
    imput_data_tbl = Tbl.loc[indexes]
    imput_data_tbl = imput_data_tbl.apply(lambda column: column.notnull().astype(int).to_frame() if ('_frequency' in column.name) else column, axis=0)
    return imput_data_tbl.reset_index().drop('index', axis=1)