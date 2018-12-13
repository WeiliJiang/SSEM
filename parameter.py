# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:02:04 2018

@author: HW
"""
import numpy as np
#parameter

classifier_config_dict = {
        "param_grid_tree": {"criterion": ["gini", "entropy"],
                   "splitter": ["best","random"],
                   "max_depth": [3,8,12,15],
                   "min_samples_split": [3, 5,8,10],
                   "min_samples_leaf": [3, 5,8,10],
                   #"max_features": [3, 4, 5, 6, 7, 8, 9, 10],
                   },
        "param_grid_RF": {"max_depth": [3,8,12,15],  
                  "min_samples_split": [3, 5,8,10],  
                  "min_samples_leaf": [3, 5,8,10], 
                  "criterion": ["gini", "entropy"],  
                  "n_estimators": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
                  #"max_features": [3, 4, 5, 6, 7, 8, 9, 10],  
                  "warm_start": [True, False],  
                  "oob_score": [True, False],  
                  "verbose": [True, False]
                  },        
        'BernoulliNB': {
                'alpha': [1e-4, 1e-3, 1e-2, 1e-1, 1., 10., 100., 1000.],
                'fit_prior': [True, False]
                },
        
        'LogisticRegression': {
                'C': [1e-3, 1e-2, 1e-1, 1., 5., 10., 15., 20.],
                'dual': [True, False]
                },
        'ExtraTreesClassifier': {
                'n_estimators': [100],
                'criterion': ["gini", "entropy"],
                #'max_features': [3, 4, 5, 6, 7, 8, 9, 10],
                'min_samples_leaf': range(1, 17),
                'bootstrap': [True, False]
                },
        }