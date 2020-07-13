# filehandler.py
# This is the model part of the Model-View-Controller
# The class holds the name of a file.
# Both the name can be modified in the GUI
# and updated through methods of this model.
# 

from StudentPlacementSorterFunctions import readPlacementData, readStudentData

class FileHandler:
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None

    def isValid( self, fileName ):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False
        
    def assertFormat( self, fileName ):
        '''
        Returns True if the file can be read by the algorithm.
        Raises exception otherwise.
        '''
        try:
            readPlacementData(fileName)
            readStudentData(fileName)
            return True
        except:
            raise

    def setFileName( self, fileName , isnewfile=False):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        if self.isValid( fileName ) or isnewfile:
            self.fileName = fileName
        else:
            self.fileName = ""
            
    def getFileName( self ):
        '''
        Returns the name of the file name member.
        '''
        return self.fileName

    