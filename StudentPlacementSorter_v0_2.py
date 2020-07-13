# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:35:33 2020

@author: unbor
"""

import StudentPlacementSorterFunctions as spsf
from time import time

# Global Variables #
ex_input_filename = 'Full_Placement_Data.xlsx'
ex_output_filename = 'Paired_Placements.xlsx'
    
def reportGeocodeTime(input_filename, api_key):
    start = time()
    placements = spsf.readPlacementData(input_filename)
    students = spsf.readStudentData(input_filename)
    spsf.geocodeHospitalPostcodeLocations(placements, api_key=api_key)
    spsf.geocodeStudentPostcodesLocations(students,api_key=api_key)
    end = time()
    print(end-start)    
    
def sortPlacements(input_filename, output_filename, api_key, progress_callback):
    
    start = time()
    placements = spsf.readPlacementData(input_filename)
    students = spsf.readStudentData(input_filename)   
    
    start_geocode = time()
    progress_callback.emit(2)
    
    hospital_postcode_locations = spsf.geocodeHospitalPostcodeLocations(placements, api_key=api_key)
    progress_callback.emit(10)
    
    student_postcode_locations = spsf.geocodeStudentPostcodesLocations(students, api_key=api_key)
    
    start_alg = time()
    progress_callback.emit(60)
    
    placement_pairings, remaining_students, remaining_placements =  \
        spsf.sortStudentsSameDayAnyHosp(students, 
                                        placements,
                                        student_postcode_locations,
                                        hospital_postcode_locations,
                                        show_score=True)
    
    paired_condition = (placement_pairings['Attendee'] != False)
    placement_pairings.loc[paired_condition, 'Score'] = \
        spsf.transformScore(placement_pairings.loc[paired_condition]['Score'])
    placement_pairings.sort_values(by=['Week','Score'], inplace=True)
    
    start_write = time()
    
    with spsf.pd.ExcelWriter(output_filename) as writer:
        placement_pairings.to_excel(writer, sheet_name='Placement Pairings', index=False)
        remaining_placements.to_excel(writer, sheet_name='Unallocated Placements', index=False)
        remaining_students.to_excel(writer, sheet_name='Unallocated Students', index=False)
    end = time()
    progress_callback.emit(100)
        
    spsf.logging.info("Read time: %.2f", (start_geocode-start))
    spsf.logging.info("Geocode time: %.2f", (start_alg-start_geocode))
    spsf.logging.info("Algorithm time: %.2f", (start_write-start_alg))
    spsf.logging.info("Write time: %.2f", (end-start_write))
    
if __name__ == "__main__":
    sortPlacements(ex_input_filename,ex_output_filename)
