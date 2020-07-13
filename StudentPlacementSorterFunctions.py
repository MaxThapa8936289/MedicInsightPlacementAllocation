# -*- coding: utf-8 -*-
""" 
Student Placement Sorter Functions

Functions for Student Placement Sorter (Version 0.1)
    Decalration of all functions necessary for the Student PLacement Sorter
    program.

Created on Tue Mar 17 14:21:51 2020
@author: Max Thapa
"""

# Imports #
import pandas as pd;
import numpy as np;
from scipy.spatial.distance import cdist

from geopy.geocoders import GoogleV3
import logging
import concurrent.futures

from geopy.exc import GeocoderQueryError
from xlrd.biffh import XLRDError



# Data Engineering #
def readPlacementData(filename=None):
    """
    Attempts to read the placement data located in the working directory at 'filename', in preparation for 
    the main algorithm.
    File must be an excel spreadsheet with an .xlsx extension. Example file name: 'myfile.xlsx'.
    File must include a sheet names 'Placements' and include 7 columns representing the following quantities:
    ['Week', 'Day', 'Time', 'Clinician_ID', 'Type', 'HospName', 'Postcode']
    and the columns must appear in that order. 
    The file must not include any missing values.
    
    If the above requirements are met, returns the placement data as a pandas.DataFrame object.
    If the above requirements are NOT met, the function will try to raise an appropriate error message.
    """
    try:
        Placements_With_Weeks = pd.read_excel(filename, \
                                              sheet_name='Placements', \
                                              header=0, \
                                              names=['Week', 'Day', 'Time', 'Clinician_ID', 'Type', 'HospName', 'Postcode'])
    except ValueError as v_e:
        if 'Length mismatch' in str(v_e):
            raise ValueError(
                "Wrong number of columns in placement data. "
                +"Should have ['Week', 'Day', 'Time', 'Clinician_ID', 'Type', 'HospName', 'Postcode'] in that order."
            )      
        else:
            raise
    except XLRDError as xlrd_e:
        if 'No sheet named' in str(xlrd_e):
            raise XLRDError(
                "Could not read the sheet name for the placement data. "
                +"Sheet name must be called 'Placements'. Please check and try again."
            )
        else:
            raise
    
    if Placements_With_Weeks.isnull().any().any():
        raise ValueError(
            "The placement data provided has missing values. Please remove them and try again."
        )
    
    return Placements_With_Weeks

def readStudentData(filename=None):
    """
    Attempts to read the student data located in the working directory at 'filename', in preparation for 
    the main algorithm.
    File must be an excel spreadsheet with an .xlsx extension. Example file name: 'myfile.xlsx'.
    File must include a sheet names 'Student' and include 7 columns representing the following quantities:
    ['Attendee', 'Postcode', 'Week']
    and the columns must appear in that order. 
    The file must not include any missing values.
    
    If the above requirements are met, returns the student data as a pandas.DataFrame object.
    If the above requirements are NOT met, the function will try to raise an appropriate error message.
    """
    try:
        Students_With_Weeks = pd.read_excel(filename, \
                                            sheet_name='Students', \
                                            header=0, \
                                            names=['Week', 'Attendee', 'Postcode'])
    except ValueError as v_e:
        if 'Length mismatch' in str(v_e):
            raise ValueError(
                "Wrong number of columns in student data. "
                +"Should have ['Week', 'Attendee', 'Postcode'] in that order."
            )      
        else:
            raise
    except XLRDError as xlrd_e:
        if 'No sheet named' in str(xlrd_e):
            raise XLRDError(
                "Could not read the sheet name for the student data. "
                +"Sheet name must be called 'Students'. Please check and try again."
            )
        else:
            raise
    
    if Students_With_Weeks.isnull().any().any():
        raise ValueError(
            "The student data provided has missing values. Please remove them and try again."
        )
    
    return Students_With_Weeks

def createLocator(api_key = None):
    """

    Parameters
    ----------
    api_key : string, optional
        Google Cloud API key for geocoding. The default is None.
        If an invalid key is given the function will raise an error.

    Raises
    ------
    GeocoderQueryError
        geopy.exc.GeocoderQueryError if the request fails.

    Returns
    -------
    locator : TYPE
        geocoding object using the GoogleV3 cloud API.

    """
    locator = GoogleV3(api_key=api_key, user_agent="UoG_Medicine_Placement_Sorter")
    try:
        logging.info('Test request starting')
        locator.geocode('UK G1 Postcode') # test request
        logging.info('Test request complete')
        return locator
    except GeocoderQueryError:
        logging.info('Test request failed')
        raise GeocoderQueryError('Invalid API key.')

def addQuerys(unique_postcodes):
    """ Adds a column to the dataframe contianing Google Maps friendly queries.
    """
    unique_postcodes["Query"] = unique_postcodes["Postcode"].apply(lambda pc: "UK "+pc+" postcode")
    return unique_postcodes

def geocodeQuery(locator, query):
    """ Querys Google Maps with the query, returning a location tuple.
    """
    logging.info("Thread (geocode %s): starting", query)
    loc = locator.geocode(query)
    logging.info("Thread (geocode %s): finishing", query)
    return loc

def ThreadedGeocoder(students_or_placements, locator):
    """
    Geocodes the unique postcodes foun in the student/placement data.
    Uses concurrent.futures mulithreading to issue up to 4 simultaneous
    requests.
    
    Parameters
    ----------
    students_or_placements : pandas.DataFrame object
        The DataFrame containing either the student data or the placement
        data.
    locator : Geopy locator object.
        The Geopy Google Maps API object to make queries with, created with
        createLocator()

    Returns
    -------
    unique_postcodes : pandas.DataFrame object
        DataFrame containing the list of unique postcodes found in the data
        and their corresponding Latitude and Longditude values.

    """
    unique_postcodes = students_or_placements.groupby(['Postcode']).count().reset_index()["Postcode"].to_frame()
    unique_postcodes = addQuerys(unique_postcodes)
    queryList = unique_postcodes["Query"].values

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(geocodeQuery, [locator]*len(queryList), queryList)
    
    locations = []
    for result in results:
        locations.append(result)
    
    unique_postcodes['Location'] = locations
    unique_postcodes["Latitude"] = unique_postcodes["Location"].apply(lambda loc: loc.latitude)
    unique_postcodes["Longitude"] = unique_postcodes["Location"].apply(lambda loc: loc.longitude)
    unique_postcodes = unique_postcodes.drop(columns=["Query","Location"])
    return unique_postcodes

def geocodeHospitalPostcodeLocations(placements, api_key=None):
    """ Returns the unique hospital postcodes locations 
    found in the placement data.
    api_key must be a valid Google Cloud geocoding API key.
    """
    locator = createLocator(api_key=api_key)
    hospital_postcodes = ThreadedGeocoder(placements,locator)
    return hospital_postcodes
    
def geocodeStudentPostcodesLocations(students, api_key=None):
    """ Returns the unique student postcodes locations 
    found in the student data.
    api_key must be a valid Google Cloud geocoding API key.
    """
    locator = createLocator(api_key=api_key)
    student_postcodes = ThreadedGeocoder(students,locator)
    return student_postcodes

        
def optimiseStudentOrder(students,student_postcodes_locations):
    """
    Uses the lat-long values returned by geocodeStudentPostcodesLocations() to 
    sort the student data by distance from the centre of glasgow (highest first).
    This order is near optimal for the sorting main sorting algorithm.
    
    students: pandas.DataFrame object - student data returned by readStudentData().
    student_postcodes_locations: pandas.DataFrame object - returned by geocodeStudentPostcodesLocations().
    
    Returns: copy of 'students' in optimal order.
    """
    centre = np.array([[55.861852, -4.252371]]) # Glasgow Centre
    lat_long = student_postcodes_locations.drop(columns=['Postcode']).values
    student_postcode_distfromcentre = pd.DataFrame(cdist(lat_long, centre, 'euclidean'),columns=['Distance'], index=student_postcodes_locations['Postcode'].values)
    student_postcode_distfromcentre = student_postcode_distfromcentre.sort_values(by='Distance').reset_index().rename(columns={'index':'Postcode'})
    students_distfromcentre = students.merge(student_postcode_distfromcentre, how='left', left_on='Postcode', right_on='Postcode')
    out_to_in_students = students_distfromcentre.sort_values(by='Distance', ascending=False).drop(columns='Distance').reset_index(drop=True)
    return out_to_in_students

def getStudentHospitalDistanceMatrix(student_postcode_locations, hospital_postcode_locations):
    """
    Calulates the distances between all combinations of unique student postcode and unique hospital postcode.
    
    student_postcode_locations: pandas.DataFrame object - returned by geocodeStudentPostcodesLocations().
    hospital_postcode_locations: pandas.DataFrame object - returned by geocodeHospitalPostcodeLocations().
    
    Returns: pandas.DataFrame object containing the distance matrix and the postcodes as indicies/columns.
    """
    stud_loc = student_postcode_locations.copy().drop(columns="Postcode").values
    hosp_loc = hospital_postcode_locations.copy().drop(columns="Postcode").values
    DistMatrix_df = pd.DataFrame(cdist(stud_loc, hosp_loc, 'euclidean'),columns=hospital_postcode_locations["Postcode"].values, index=student_postcode_locations["Postcode"].values)
    DistMatrix_df = DistMatrix_df.sort_index(axis=0).sort_index(axis=1)
    return DistMatrix_df

def getHospitalHospitalDistanceMatrix(hospital_postcode_locations):
    """
    Calulates the distances between all combinations of unique hospital postcode.
    
    hospital_postcode_locations: pandas.DataFrame object - returned by geocodeHospitalPostcodeLocations().
    
    Returns: pandas.DataFrame object containing the distance matrix and the postcodes as indicies/columns.
    """
    hosp_loc = hospital_postcode_locations.copy().drop(columns="Postcode").values
    DistMatrix_df = pd.DataFrame(cdist(hosp_loc, hosp_loc, 'euclidean'),columns=hospital_postcode_locations["Postcode"].values, index=hospital_postcode_locations["Postcode"].values)
    DistMatrix_df = DistMatrix_df.sort_index(axis=0).sort_index(axis=1)
    return DistMatrix_df

# Main Algorithm #
    
class PlacementError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)

def pickRandomPlacement(placements, postcode=None, week=None, day=None, time=None, veto_type=None):
    """
    Picks a radom placement from the list. If any or all of 'postcode', 'week', day', and 'time' 
    are specified, the placement is chosen from the postcode, day and/or time. 
    If 'veto_type' is specified, function prefferentially chooses a placement that 
    is not of that type, if any exists.
    Returns: pandas.Series object containing a single placement session. 
    
    placements: pandas.DataFrame object containing placement information
    postcode: str object containing hospital postcode
    day: str object containing day
    time: str object containing 'AM' or 'PM'
    """
    temp_placements = placements.copy()
    
    availability_condition = (temp_placements['Attendee']==False)
    
    if postcode:
        hosp_condition = (temp_placements['Postcode'] == postcode)
    else: hosp_condition = temp_placements['Postcode'].apply(any)
    if week:
        week_condition = (temp_placements['Week'] == week)
    else: week_condition = temp_placements['Week'].apply(bool)
    if day:
        day_condition = (temp_placements['Day'] == day)
    else: day_condition = temp_placements['Day'].apply(any)
    if time:
        time_condition = (temp_placements['Time'] == time)
    else: time_condition = temp_placements['Time'].apply(any)
    if veto_type:
        veto_condition = (temp_placements['Type'] != veto_type)
    else: veto_condition = (temp_placements['Type'].apply(any))
    
    try:
        short_list = temp_placements.loc[availability_condition & hosp_condition & \
                                         week_condition & day_condition & time_condition & veto_condition].copy()
        placement = short_list.iloc[np.random.randint(len(short_list))]
    except ValueError: 
        short_list = temp_placements.loc[availability_condition & hosp_condition & \
                                         week_condition & day_condition & time_condition].copy()
        placement = short_list.iloc[np.random.randint(len(short_list))]
        
    return placement

def getAvailabilityMatrix(placement_pairings, week, day):
    """
    Calculates the the availability of all AM/PM combinations across all hospitals.
    Each element at row i and column j represents the capacity for full day 
    placements that have the AM session at hospital i and PM session at hospital j.

    Parameters
    ----------
    placement_pairings : pandas.DataFrame object 
        Frame containing placement inforamtion. 
    week : int
        The week within which to query availability  
    day : string
        The day within which to query availability.

    Returns
    -------
    hosp_hosp_availibility : pandas.DataFrame object
        DataFrame containing a matrix of all AM/PM combinations across all hospitals.
        Hospital postcodes are the index and column values.

    """
    week_pairings = placement_pairings.loc[placement_pairings['Week'] == week].copy()
    placement_slots = week_pairings.groupby(['Postcode','Day','Time','Attendee'])["Week"].count()\
        .unstack(fill_value=0).unstack(fill_value=0).unstack(fill_value=0).stack().stack().stack()
    AM = placement_slots.xs((day,'AM',False),level=('Day','Time','Attendee'))
    AM.index.rename('AM', inplace=True)
    PM = placement_slots.xs((day,'PM',False),level=('Day','Time','Attendee'))
    PM.index.rename('PM', inplace=True)
    hosp_hosp_availibility = pd.DataFrame(np.minimum(AM.values.reshape(len(AM),1), PM.values), index = AM.index, columns=PM.index)
    hosp_hosp_availibility = hosp_hosp_availibility.sort_index(axis=0).sort_index(axis=1)
    return hosp_hosp_availibility

def place(placement_pairings_, student, stud_hosp_distances, hosp_hosp_distances, show_score):
    """
    Places the student in the optimal AM and PM session available to them.#
    
    Parameters
    ----------
    placement_pairings_ : pandas.DataFrame object
        Frame containing placement inforamtion. 
    student : pandas.Series object
        Series containing student information
    stud_hosp_distances : pandas.DataFrame object
        Frame containing the distances between all combinations of (student, hospital)
        pairs.
    hosp_hosp_distances : pandas.DataFrame object
        Frame containing the distanced between all combinations of hospital.
    show_score : boolean
        If True, records the distance score for the pairing in the ['Score'] column.
        (Column must already exist in placement_pairings_)
    Raises
    ------
    PlacementError
        If there are no placements availabe to the student.

    Returns
    -------
    placement_pairings : pandas.DataFrame object
        Copy of placement_pairings_ with student inforamtion filled in on the 
        appropriate columns for a single AM and single PM session.

    """
    #placement_pairings = placement_pairings_.loc[placement_pairings_['Week']==student['Week']].copy()
    placement_pairings = placement_pairings_.copy()
    # get student-hosp distance as a Series
    student_hosp_dist = stud_hosp_distances.loc[student['Postcode']].squeeze()
    # make student-hosp-hosp matrix
    student_hosp_hosp_dist = hosp_hosp_distances.add(student_hosp_dist, axis=0).add(student_hosp_dist, axis=1)

    # declare value and index objects
    idx,idy = 0,0
    score = np.inf
    # # Loop Over Days and minimise score
    for day_iter in placement_pairings['Day'].unique():
        # get placement slots
        availability = getAvailabilityMatrix(placement_pairings, week=student['Week'], day=day_iter)
        # mask student-hosp-hosp matrix
        student_hosp_hosp_dist_mask = np.ma.masked_array(student_hosp_hosp_dist, (availability == 0).values)
        # get min idx,idy and val
        try: 
            temp_idx,temp_idy = np.transpose((student_hosp_hosp_dist_mask == student_hosp_hosp_dist_mask.min()).nonzero())[0]
            temp_score = student_hosp_hosp_dist.iloc[temp_idx,temp_idy]
        except IndexError: # no placements
            temp_score = np.inf 
        
        # minimise val
        if temp_score < score:
            idx,idy = temp_idx,temp_idy
            score = temp_score
            day = day_iter
    
    # Raise error ef no placement found
    if score == np.inf:
        raise PlacementError("no placement avaialable")
        
    # get params for placement
    am_hosp_code = student_hosp_hosp_dist.index[idx]
    pm_hosp_code = student_hosp_hosp_dist.columns[idy]
    
    # get placements
    am = pickRandomPlacement(placement_pairings, postcode=am_hosp_code, week=student['Week'], day=day, time='AM')
    pm = pickRandomPlacement(placement_pairings, postcode=pm_hosp_code, week=student['Week'], day=day, time='PM')
    
    # assign pairing:
    placement_pairings.loc[am.name, ['Attendee','Attendee_Postcode']]=student[['Attendee','Postcode']].values
    placement_pairings.loc[pm.name, ['Attendee','Attendee_Postcode']]=student[['Attendee','Postcode']].values
    
    if show_score:
        placement_pairings.loc[am.name, 'Score'] = score
        placement_pairings.loc[pm.name, 'Score'] = score
    
    return placement_pairings

def sortStudentsSameDayAnyHosp(students, placements, student_postcode_locations, hospital_postcode_locations, show_score=False):
    """
    Pairs students with their optimal available AM and PM session until either
    no placements or no students remain. Optionally records the score of each 
    pairing (lower is better).

    Parameters
    ----------
    students : pandas.DataFrame object
        Frame containing student information.
    placements : TYPE
        Frame containing placement information.
    student_postcode_locations : TYPE
        DESCRIPTION.
    hospital_postcode_locations : TYPE
        DESCRIPTION.
    show_score : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    placement_pairings : TYPE
        DESCRIPTION.
    remaining_students : TYPE
        DESCRIPTION.
    remaining_placements : TYPE
        DESCRIPTION.

    """
    # get distance matricies 
    stud_hosp_distances = getStudentHospitalDistanceMatrix(student_postcode_locations, hospital_postcode_locations)
    hosp_hosp_distances = getHospitalHospitalDistanceMatrix(hospital_postcode_locations)
    
    # order students
    ordered_students = optimiseStudentOrder(students,student_postcode_locations)
    
    # Create output DataFrames
    placement_pairings = placements.copy()
    placement_pairings['Attendee'] = False
    placement_pairings['Attendee_Postcode'] = False
    if show_score == True:
        placement_pairings['Score'] = None
    remaining_students = ordered_students.copy()
    remaining_placements = placements.copy()
    
    # Place students
    for idx, student in ordered_students.iterrows():
        try:
            placement_pairings = place(placement_pairings, student, stud_hosp_distances, hosp_hosp_distances, show_score)
            remaining_students.drop(student.name,inplace=True)
        except PlacementError:
            continue
    remaining_placements = placement_pairings.loc[placement_pairings['Attendee']==False].drop(columns=['Attendee','Attendee_Postcode'])
    return placement_pairings, remaining_students, remaining_placements

def transformScore(ScoreSeries):
    """
    Maps the score onto a scale of 33 to 100 representing a poor match (33) or good match (100).
    
    ScoreSeries: pandas.Series object containing score values in float type.
    Returns: pandas.Series object of transformed scores.
    """
    
    result = ScoreSeries.copy()
    reverse =  0 - ScoreSeries
    max_value = reverse.max()
    min_value = reverse.min()
    min_max_normalised = (reverse - min_value) / (max_value - min_value)
    projected = (1 + 2*min_max_normalised)/3
    percentised = (projected*100).apply(np.floor)
    result = percentised
    return result