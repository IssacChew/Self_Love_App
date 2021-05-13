import pandas as pd
def data_cleaning(df):
    del df['Timestamp']
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('yoga','Yoga')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Following idols and internet personalities','Following idols')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('listening to music','Listening to music')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Searching for new music','Listening to music')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Listening to songs / music','Listening to music')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Drawing/sketching','Drawing')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('watching dramas','Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('watching movies/TV shows','Watching movies;Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Watching anime, youtube videos','Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Watching movies / Netflix','Watching movies;Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Bingewatching','Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('youtube/ netflix','Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Watching movies/ Netflix','Watching movies;Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Watching anime, drama, movies, youtube','Watching movies;Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Watching Tv shows','Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace(';sex','')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('none','Sleeping')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Take a nap','Sleeping')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Basketball ans Sleeping','Basketball;Sleeping')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('sleeping','Sleeping')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('sleep','Sleeping')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Take a nap','Sleeping')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Filming ','Vlogging')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('walking in nature (jungle)','Hiking')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Exercising, Playing musical instrument (Piano)','Playing a musical instrument')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Colouring, sudoku','Drawing;Puzzles')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Surfing the web, watching YouTube videos, scrolling through social media','Web surfing')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('taking a stroll, skateboarding, ','Exercising;')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Playing guitar','Playing a musical instrument')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Exercising, Playing musical instrument (Piano)','Playing a musical instrument')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].replace({'Swimming;Dancing;Playing computer games;Singing;Exercising, Playing musical instrument (Piano)':'Swimming;Dancing;Playing computer games;Singing;Playing a musical instrument'})
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].replace({'Painting;walking in nature (jungle)':'Painting;Hiking'})
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].replace({'Dancing;Writing;Puzzles;Playing a musical instrument (guitar), watching films ':'Dancing;Writing;Puzzles;Playing a musical instrument;Watching movies'})
    #Further grouping
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Baking','Cooking')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Football','Team sports')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Volleyball ','Team sports')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Basketball','Team sports')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Drawing','Painting')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Yoga','Exercising')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Jogging','Exercising')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Cycling','Exercising')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Hiking','Exercising')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Swimming','Exercising')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Typing','Writing')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Web surfing','Reading')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Following idols','Watching TV series')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Photography','Photography and Videography')
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.replace('Vlogging','Photography and Videography')
    return df
 def hobby_count(df):
    df['What are your hobbies? (You may select more than 1)']=df['What are your hobbies? (You may select more than 1)'].str.split(";")
    dict_hobby={}
    for hobbies in df['What are your hobbies? (You may select more than 1)']:
        for hobby in hobbies:
            if hobby not in dict_hobby.keys():
                dict_hobby[hobby]=1
            else:
                dict_hobby[hobby]=dict_hobby[hobby]+1
    print(dict_hobby)
    
if __name__ == '__main__':
  df=pd.read_csv("WID3006 ML Questionnaire.csv")
  df=data_cleaning(df)
