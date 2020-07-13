# GlasgowStudentSorter_v0.1.py
# PyQt5 Application
# Editable UI version of the MVC application.
# Inherits from the Ui_Wizard class defined in wizard.py.
# Provides functionality to the 4 interactive widgets (2 push-buttons,
# and 2 line-edits).

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRunnable, QThreadPool, QTimer, QObject, pyqtSignal, pyqtSlot
import sys, traceback
from wizard import Ui_Wizard
from filehandler import FileHandler
import StudentPlacementSorter_v0_2 as sps


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress 

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()    

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress        

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
            

class WizardUIClass( Ui_Wizard ):
    def __init__( self ):
        '''Initialize the super class
        '''
        super().__init__()
        self.inputFileHandler = FileHandler()
        self.outputFileHandler = FileHandler()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgressBar)
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        
    def setupUi( self, W ):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi( W )
        
        # Register mandatory fields
        self.wizardPage1.registerField("lineEdit_ApiKey*", self.lineEdit_ApiKey)
        self.wizardPage1.registerField("lineEdit_InputFilePath*", self.lineEdit_InputFilePath)
        self.wizardPage1.registerField("lineEdit_OutputFilePath*", self.lineEdit_OutputFilePath)
        self.wizardPage2.registerField("progressBar*", self.progressBar, property="value", changedSignal=self.progressBar.valueChanged)

        # close the lower part of the splitter to hide the 
        # debug window under normal operations
        self.splitter.setSizes([300, 0])
        
        # Set the initial value of the progress bar
        self.progress = 0
        self.progressBar.setValue(self.progress)


    def debugPrint( self, msg ):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        self.debugTextBrowser.append( msg )
    
    def refreshAll( self ):
        '''
        Updates the widgets whenever an interaction happens.
        Typically some interaction takes place, the UI responds,
        and informs the model of the change.  Then this method
        is called, pulling from the model information that is
        updated in the GUI.
        '''
        self.lineEdit_InputFilePath.setText( self.inputFileHandler.getFileName() )
        self.lineEdit_OutputFilePath.setText( self.outputFileHandler.getFileName() )
        self.lineEdit_ReadOnlyOutPath.setText( self.outputFileHandler.getFileName() )

    # slot
    def testKeyPressedSlot( self ):
        self.debugPrint('Test Key Button Pressed')
        api_key = self.lineEdit_ApiKey.text()
        try:
            sps.spsf.createLocator(api_key)
            
            m = QtWidgets.QMessageBox()
            m.setWindowTitle("Valid API key")
            m.setText("API Key accepted.")
            m.setStandardButtons(QtWidgets.QMessageBox.Ok)
            ret = m.exec_()
            self.debugPrint( "Valid API Key")
        except:
            m = QtWidgets.QMessageBox()
            m.setWindowTitle("Invalid API key")
            m.setText("Invalid API Key!")
            m.setInformativeText(" Please check that you have entered a valid \
                                 Google Cloud Geocoding API key. For more \
                                 details, check the User Manual.")
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit_ApiKey.setText( "" )
            self.debugPrint( "Invalid API Key")

    # slot
    def inputReturnPressedSlot( self ):
        ''' Called when the user enters a string in the line edit and
        presses the ENTER key.
        '''
        self.debugPrint( "RETURN key pressed in input LineEdit widget" )
        
        fileName =  self.lineEdit_InputFilePath.text()
        if self.inputFileHandler.isValid( fileName ):
            try:
                self.inputFileHandler.assertFormat(fileName)
            except Exception as e:
                m = QtWidgets.QMessageBox()
                m.setWindowTitle("Error Reading File!")
                m.setText("Invalid file!")
                m.setInformativeText(str(e))
                m.setIcon(QtWidgets.QMessageBox.Warning)
                m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                     | QtWidgets.QMessageBox.Cancel)
                m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
                ret = m.exec_()
                self.lineEdit_InputFilePath.setText( "" )
                self.refreshAll()
                self.debugPrint( "Invalid file specified: " + fileName  )            
            else:
                self.inputFileHandler.setFileName( self.lineEdit_InputFilePath.text() )
                self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setWindowTitle("Error Reading File!")
            m.setText("Invalid file name!\n" + fileName )
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit_InputFilePath.setText( "" )
            self.refreshAll()
            self.debugPrint( "Invalid file specified: " + fileName  )
        

    # slot
    def inputBrowseSlot( self ):
        ''' Called when the user presses the Browse button
        '''
        self.debugPrint( "Input Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Open Placment and Student Data",
                        "",
                        "Excel Files (*.xlsx);;All Files (*)",
                        options=options)
        if fileName:
            try:
                self.inputFileHandler.assertFormat(fileName)
            except Exception as e:
                m = QtWidgets.QMessageBox()
                m.setWindowTitle("Error Reading File!")
                m.setText("Invalid file!")
                m.setInformativeText(str(e))
                m.setIcon(QtWidgets.QMessageBox.Warning)
                m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                     | QtWidgets.QMessageBox.Cancel)
                m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
                ret = m.exec_()
                self.lineEdit_InputFilePath.setText( "" )
                self.refreshAll()
                self.debugPrint( "Invalid file specified: " + fileName  )            
            else:            
                self.debugPrint( "setting file name: " + fileName )
                self.inputFileHandler.setFileName( fileName )
                self.refreshAll()

    # slot
    def outputReturnPressedSlot( self ):
        ''' Called when the user enters a string in the line edit and
        presses the ENTER key.
        '''
        self.debugPrint( "RETURN key pressed in output LineEdit widget" )

        fileName =  self.lineEdit_InputFilePath.text()
        if self.outputFileHandler.isValid( fileName ):
            self.outputFileHandler.setFileName( self.lineEdit_OutputFilePath.text() )
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setWindowTitle("Error Reading File!")
            m.setText("Invalid file name!\n" + fileName )
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit_OutputFilePath.setText( "" )
            self.refreshAll()
            self.debugPrint( "Invalid file specified: " + fileName  )
        
    # slot
    def outputBrowseSlot( self ):
        ''' Called when the user presses the Browse button
        '''
        self.debugPrint( "Output Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
                        None,
                        "Save Destination",
                        "",
                        "Excel Files (*.xlsx);;All Files (*)",
                        options=options)
        self.debugPrint( "Chosen filename: " + fileName )
        if fileName:
            self.debugPrint( "setting file name: " + fileName )
            self.outputFileHandler.setFileName( fileName , isnewfile=True)
            self.refreshAll()
            
    # slot
    def startSlot( self ):
        ''' 
        Called when the use presses the Start button. 
        Begins the algorithm for sorting the students and updates the
        progress bar.
        '''
        input_filepath = str(self.wizardPage1.field("lineEdit_InputFilePath"))
        output_filepath = str(self.wizardPage1.field("lineEdit_OutputFilePath"))
        api_key = str(self.wizardPage1.field("lineEdit_ApiKey"))
        
        self.startButton.setText("Calculating...")
        self.startButton.setEnabled(False)
        
        print("Starting algorithm with " + str(input_filepath))
        self.startWorker(sps.sortPlacements, input_filepath, output_filepath, api_key)
        self.timer.start(300)


    def startWorker(self, func, *args, **kwargs):
        # Pass the function to execute
        worker = Worker(func, *args, **kwargs) # Any other args, kwargs are passed to the run function
        worker.signals.error.connect(self.algorithmErrorHandler)
        worker.signals.finished.connect(self.threadComplete)
        worker.signals.progress.connect(self.updateProgressBar)
        
        # Execute
        self.threadpool.start(worker) 

    def algorithmErrorHandler(self, error):
        exctype, value, traceback = error
        self.timer.stop()
        m = QtWidgets.QMessageBox()
        m.setWindowTitle("Error Sorting Students!")
        m.setText("An error occured!")
        m.setInformativeText("There was an error while using the data provided. " +
                             "Please check the data is formatted according to " +
                             "the User Manual, then try again.")
        m.setIcon(QtWidgets.QMessageBox.Warning)
        m.setStandardButtons(QtWidgets.QMessageBox.Ok
                             | QtWidgets.QMessageBox.Cancel)
        m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        ret = m.exec_()
        sys.exit()
        
    def threadComplete(self):
        print("THREAD COMPLETE!")        

    def updateProgressBar(self,progress_callback=None):
        if progress_callback: 
            self.progress = progress_callback
        else:
            self.progress += 1
        if self.progress >= 100:
            self.timer.stop()
        self.progressBar.setValue(self.progress)

def main():
    """
    This is the MAIN ENTRY POINT of our application.  The code at the end
    of the mainwindow.py script will not be executed, since this script is now
    our main program.   We have simply copied the code from mainwindow.py here
    since it was automatically generated by '''pyuic5'''.

    """
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #                     datefmt="%H:%M:%S")    
    
    app = QtWidgets.QApplication(sys.argv)
    Wizard = QtWidgets.QWizard()
    ui = WizardUIClass()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())

main()