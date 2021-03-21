# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:38:15 2021

@author: Rachel
"""


filedirectory = 'C:\\Users\\Rachel\\Documents\\GitHub\\familytree'
father1name = 'Father Name'
mother1name = 'Mother Name'
person1name = 'Rachel Molaro'

geolocatoremail = 'your.geolocator.email@gmail.com'

map_annote1 = ['Smith & Jones','Bambi','Simba','Duck','Scar',
               'Dumbo']

personsettings = {
    'Rachel': {
        'id' : 1,
        'num_gens_down': 1,
        'num_gens_up': 4,
        'degrees_sideways_to_include': [2, 2, 1, 1, 1, 0],
        'ex_list': [],
        'incl_list': [[226,1,1,False],[227,1,1,False],[228,1,1,True],[229,0,2,False], 
                      [230,0,2,False],[231,0,2,False],[232,1,1,True]],
        'size_by_degree' : None,
        'r' : 300,
        'canvas_width' : 40,
        'canvas_height' : 20,
        'top_border' : 1,
        'bottom_border' : 5,
        'side_border' : 0.5,
        'spacing_couple' : 0.1,
        'spacing_siblings' : 0.2,
        'min_spacing_generation' : 0.3,
        'min_spacing_family' : 0.4,
        'pic_aspect_ratio' : 3/2,
        'text_vert_fraction' : 1/2,
        'yspacing' : 0.07,
        'atextwrap' : [22,20,20,22,22,20,22,18,20,20,20,20,24,22,24,20],
        'aframewratio' : 1.5
    },
    'HarryPotter': {
        'id' : 0,
        'num_gens_down': 0,
        'num_gens_up': 2,
        'degrees_sideways_to_include': [2, 2, 1],
        'ex_list': [],
        'incl_list': [],
        'size_by_degree' : None,
        'r' : 300,
        'canvas_width' : 24,
        'canvas_height' : 18,
        'top_border' : 1,
        'bottom_border' : 3,
        'side_border' : 0.5,
        'spacing_couple' : 0.1,
        'spacing_siblings' : 0.2,
        'min_spacing_generation' : 0.5,
        'min_spacing_family' : 0.4,
        'pic_aspect_ratio' : 3/2,
        'text_vert_fraction' : 1/2,
        'yspacing' : 0.1,
        'atextwrap' : [],
        'aframewratio' : 1.2
    },
    'Khan': {
        'id' : 0,
        'num_gens_down': 5,
        'num_gens_up': 0,
        'degrees_sideways_to_include': [2, 2, 1, 1, 1, 0],
        'ex_list': [],
        'incl_list': [],
        'size_by_degree' : None,
        'r' : 300,
        'canvas_width' : 24,
        'canvas_height' : 18,
        'top_border' : 1,
        'bottom_border' : 3,
        'side_border' : 0.5,
        'spacing_couple' : 0.1,
        'spacing_siblings' : 0.2,
        'min_spacing_generation' : 0.5,
        'min_spacing_family' : 0.4,
        'pic_aspect_ratio' : 3/2,
        'text_vert_fraction' : 1/2,
        'yspacing' : 0.1,
        'atextwrap' : [],
        'aframewratio' : 1.2
    }
}
        
        