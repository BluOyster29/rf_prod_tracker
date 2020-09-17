import argparse
import os
import pandas as pd
import datetime

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('start_tag', type=int, help="Amount tagged when at start of session")
    p.add_argument('end_tag', type=int, help = "Amount tagged by end of session")
    p.add_argument('hours', type=int, help= "Total number of hours overall")
    p.add_argument('sesh_hours', type=int, help="Hours spent this session")
    p.add_argument('--data_path', type=str, help="Path to csv file",  default='tracked_prod.csv')
    p.add_argument('--total_frags', type=int, help="Total fragments in dataset", default=10981) 
    p.add_argument('--update_csv', type=bool, help="Update CSV file", default=False) 
    
    return p.parse_args()

def check_csv(path):
    date = datetime.datetime.now()
    date = date.strftime("%x")
    
    data = {'date' : date,
            'hrs_sesh' : [],
            'total_hours' : [],
            'tagged_this_session' : [],
            'tagged_total' : [],
            'left_to_tag' : [],
            'avg_tag_hr_session' : [],
            'avg_tag_hr_total' : []}
    
    if os.path.exists(path):
        df = pd.read_csv(path)

    else:

        df = pd.DataFrame(data)
    return df, data

def stats(tagged_start, tagged_end, sesh_hours, total_hours, 
          total_fragments, data):
    
    tagged = tagged_end - tagged_start
    data['tagged_this_session'].append(int(tagged))
    
    sesh_avg = round(tagged / sesh_hours)
    data['avg_tag_hr_session'].append(int(sesh_avg))
    
    over_avg = round(tagged_end / total_hours)
    data['avg_tag_hr_total'].append(int(over_avg))
    left2tag = round(total_fragments-tagged_end)
    data['left_to_tag'].append(left2tag)
    data['total_hours'].append(int(total_hours))
    data['hrs_sesh'].append(int(sesh_hours))
    data['tagged_total'].append(int(tagged_end))
    
    print(data)
    return data

def update_df(df, the_data, path):

    df2 = pd.DataFrame(data=the_data)
    df = df.append(df2)
    df = df.drop_duplicates()
    df.to_csv(path, index=False)
    print('df updated')
    
if __name__ == '__main__':
    p = get_args()
    df, data = check_csv(p.data_path)
    
    data = stats(p.start_tag, p.end_tag, p.sesh_hours, p.hours, p.total_frags, data)
    
    print('{} tagged'.format(data['tagged_this_session'][0]))
    print('{} tagged an hour this sesh'.format(data['avg_tag_hr_session'][0]))
    print('{} tagged an hour overall on average'.format(data['avg_tag_hr_total'][0]))
    print('{} fragments left to tag'.format(data['left_to_tag'][0]))
    print('{} hours to go on dataset'.format(round(data['left_to_tag'][0] / data['avg_tag_hr_total'][0])))
    if p.update_csv == True:
        update_df(df, data, p.data_path)




