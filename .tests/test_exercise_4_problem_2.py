from points_decorator import points
import inspect
import os
import pandas as pd
import geopandas as gpd
import pyproj

class TestProblem2:

    @points(1, "Problem 2: Did you read in the travel times of each shopping centre?")
    def test_problem_2_centres(self, problem2):
        section_data, namespace = problem2
        grid = namespace['grid']

        expected_shopping_centres = [
            "Itis", "Myyrmanni", "Forum", "Iso_Omena", "Ruoholahti", "Dixi", "Jumbo"
            ]
        

        for shopping_centre in expected_shopping_centres:
            assert f"pt_r_t_{shopping_centre}" in grid.columns  

   
    @points(1, "Problem 2: Some of the values for the nearest shopping centre seem to be incorrect.")    
    def test_problem_2_closest_shopping_centre_value(self, problem2):
        section_data, namespace = problem2
        grid = namespace['grid']

        # Assert that the value of "closest_shopping_centre" for the row with index 5785641 is "Myyrmanni"
        row1 = grid.loc[5785641]
        assert row1['dominant_shopping_centre'] == "Myyrmanni"

        row2 = grid.loc[5876274]
        assert row2['dominant_shopping_centre'] == "Itis"

        row3 = grid.loc[5785641]
        assert row3['dominant_shopping_centre'] == "Myyrmanni"
    '''
    @points(1, "Problem 2: Did you save the plot as a PNG file?")
    def test_problem_2_plot_file_exists(self,problem2):
        section_data, namespace = problem2
        DATA_DIRECTORY = namespace['DATA_DIRECTORY']

        png_files = list(DATA_DIRECTORY.glob("*.png"))
        assert len(png_files) > 0
    
    @points(1, "Problem 2: Did you check that the PNG file is not empty?")
    def test_problem_2_plot_file_not_empty(self,problem2):
        section_data, namespace = problem2
        #DATA_DIRECTORY = namespace['DATA_DIRECTORY']

        png_files = list(DATA_DIRECTORY.glob("*.png"))
        for png_file in png_files:
            assert png_file.stat().st_size > 0
    '''