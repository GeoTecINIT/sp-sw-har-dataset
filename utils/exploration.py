# Copyright 2023 Miguel Matey Sanz
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pandas as pd
    

def subjects_age_range(info):
    '''
    Computes age range statisitcs from the subjects of the data collection.
    
    Args:
        info(pandas.DataFrame): dataframe with the information of the subjects. See: `data_loading.load_subjects_info`.
    
    Returns:
        pandas.DataFrame: dataframe with age range statistics.
    '''
    
    return info['age'].describe().to_frame().transpose()


def subjects_age_range_by_gender(info):
    '''
    Computes age range statisitcs grouped by gender from the subjects of the data collection.
    
    Args:
        info(pandas.DataFrame): dataframe with the information of the subjects. See: `data_loading.load_subjects_info`.
    
    Returns:
        pandas.DataFrame: dataframe with age range statistics grouped by gender.
    '''
    
    return info[['age', 'gender']].groupby(['gender']).describe()


def executions_by_gender(info):
    '''
    Counts the number of executions grouped by gender.
    
    Args:
        info(pandas.DataFrame): dataframe with the information of the subjects. See: `data_loading.load_subjects_info`.
    
    Returns:
        pandas.DataFrame: dataframe with executions count grouped by gender.
    '''
    
    df = info[['executions', 'gender']].groupby(['gender']).sum().transpose()
    df['Total'] = df.sum(axis=1)
    return df


def count_samples(data_collection):   
    '''
    Counts the number of collected samples for each activity and device.
    
    Args:
        data_collection(dict): collected data. Use `data_loading.load_data` to load the collected data.
        
    Returns:
        pandas.DataFrame: dataframe with the count of collected samples.
    
    '''
    
    counts = {
        'sp': {
            'SEATED': 0,
            'STANDING_UP': 0,
            'WALKING': 0,
            'TURNING': 0,
            'SITTING_DOWN': 0
        },
        'sw': {  
            'SEATED': 0,
            'STANDING_UP': 0,
            'WALKING': 0,
            'TURNING': 0,
            'SITTING_DOWN': 0
        },
    }

    for data_id, data in data_collection.items(): 
        source = data_id.split('_')[-1]
        if not isinstance(data, pd.DataFrame):
            counts[source]['SEATED'] += data.count('SEATED')
            counts[source]['STANDING_UP'] += data.count('STANDING_UP')
            counts[source]['WALKING'] += data.count('WALKING')
            counts[source]['TURNING'] += data.count('TURNING')
            counts[source]['SITTING_DOWN'] += data.count('SITTING_DOWN')
            continue
            
        count = data['label'].value_counts()
        counts[source]['SEATED'] += count['SEATED']
        counts[source]['STANDING_UP'] += count['STANDING_UP']
        counts[source]['WALKING'] += count['WALKING']
        counts[source]['TURNING'] += count['TURNING']
        counts[source]['SITTING_DOWN'] += count['SITTING_DOWN']
        
    df = pd.DataFrame(counts).transpose()
    df['TOTAL'] = df.sum(axis=1)
    return df