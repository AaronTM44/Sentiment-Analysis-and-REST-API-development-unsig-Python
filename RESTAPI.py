import requests_with_caching
import json
def get_movies_from_tastedive(movie):
    baseurl = 'https://tastedive.com/api/similar'
    params_dic = {}
    params_dic['q'] = movie
    params_dic['type'] = 'movies'
    params_dic['limit'] = 5
    resp = requests_with_caching.get(baseurl,params = params_dic)
    #print(resp.url)
    movie_ds = resp.json()
    #print(movie_d)
    return movie_ds
def extract_movie_titles(fun):
    dict1 = fun
    movie_name = []
    movie = dict1['Similar']['Results']
    for dic in movie:
        movie_name.append(dic['Name'])
    return movie_name

def get_related_titles(lst):
    name = []
    for c in lst:
        related_movie = extract_movie_titles(get_movies_from_tastedive(c))
        for i in related_movie:
            if i not in name:
                name.append(i)
        #print(name)
        #print(related_movie)
    return name
def get_movie_data(movie):
    baseurl = 'http://www.omdbapi.com/'
    params_dic = {}
    params_dic['apikey'] = ''
    params_dic['t'] = movie
    params_dic['r'] = 'json'
    
    resp = requests_with_caching.get(baseurl,params = params_dic)
    #print(resp.url)
    movie_ds = resp.json()
    #print(movie_ds)
    return movie_ds
def get_movie_rating(omdb):
    for dic in omdb['Ratings']:
        #print(dic['Source'])
        if dic['Source']=='Rotten Tomatoes':
            rate = dic['Value']
            return int(rate[:2])
        
    return 0
def get_sorted_recommendations(lst):
    movie_lst = get_related_titles(lst)
    #print(movie_lst)
    final_lst = []
    rate = []
    for movie in movie_lst:
        rate.append(get_movie_rating(get_movie_data(movie)))
        final_lst.append(movie)
    #print(final_lst)
    
    return [x for _, x in sorted(zip(rate,final_lst), reverse = True)] #sorted(final_lst, reverse= True, key = lambda )    
    
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

