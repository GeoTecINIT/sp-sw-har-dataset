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


import os
import pandas as pd


def _list_folder(path):
    
    items = os.listdir(path)
    items.sort()
    return items


def _list_subjects_folders(path):
    subjects = _list_folder(path)
    return list(filter(lambda name : os.path.isdir(os.path.join(path, name)) and name.startswith('s'), subjects))


def load_data(path='DATA'):
    '''
    Loads the accelerometer and gyroscope data for each execution.
    
    Args:
        path(str): root directory of the data. Default: 'DATA'.
        
    Returns:
        dict: pandas dict containing the accelerometer and gyroscope data for each execution.
    '''
    
    subjects = _list_subjects_folders(path)
    data = {}

    for subject in subjects:        
        subject_dir = os.path.join(path, subject)
        subject_files = _list_folder(subject_dir)

        for file in subject_files:
            file_path = os.path.join(subject_dir, file)
            file_desc = file.split('.')[0]
            if not os.path.isfile(file_path) or not file_path.endswith('.csv'):
                continue

            data[file_desc] = pd.read_csv(file_path)
    
    return data


def load_subjects_info(path=os.path.join('DATA', 'subjects_info.csv')):
    '''
    Loads the 'subjects_info.csv' file containing information about the subjects (age, gender, executions)
    
    Args:
        path (str): path of the file. Default: 'DATA/subjects_info.csv'
        
    Returns:
        pandas.DataFrame: dataframe with the contents of the file
    '''
    subjects_info = pd.read_csv(path)
    return subjects_info


def load_executions_info(path=os.path.join('DATA', 'executions_info.csv')):
    '''
    Loads the 'executions_info.csv' file containing information about the executions (id, phone orientation, turns direction)
    
    Args:
        path (str): path of the file. Default: 'DATA/executions_info.csv'
        
    Returns:
        pandas.DataFrame: dataframe with the contents of the file
    '''
    executions_info = pd.read_csv(path)
    return executions_info