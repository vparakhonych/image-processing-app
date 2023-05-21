from PyQt5 import QtCore, QtWidgets


class UiMainWindow(object):
    def setup_ui(self,  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuProcessing = QtWidgets.QMenu(self.menubar)
        self.menuProcessing.setObjectName("menuProcessing")
        self.menuHistogram_manipulation = QtWidgets.QMenu(self.menuProcessing)
        self.menuHistogram_manipulation.setObjectName("menuHistogram_manipulation")
        self.menuPoint_operations = QtWidgets.QMenu(self.menuProcessing)
        self.menuPoint_operations.setObjectName("menuPoint_operations")
        self.menuLocal_operations = QtWidgets.QMenu(self.menuProcessing)
        self.menuLocal_operations.setObjectName("menuLocal_operations")
        self.menuBlurring = QtWidgets.QMenu(self.menuLocal_operations)
        self.menuBlurring.setObjectName("menuBlurring")
        self.menuEdge_detection = QtWidgets.QMenu(self.menuLocal_operations)
        self.menuEdge_detection.setObjectName("menuEdge_detection")
        self.menuSegmentation = QtWidgets.QMenu(self.menuProcessing)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuConversion = QtWidgets.QMenu(self.menuProcessing)
        self.menuConversion.setObjectName("menuConversion")
        self.menuAnalyzing = QtWidgets.QMenu(self.menubar)
        self.menuAnalyzing.setObjectName("menuAnalyzing")
        self.menuAI = QtWidgets.QMenu(self.menubar)
        self.menuAI.setObjectName("menuAI")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.action_amera = QtWidgets.QAction(MainWindow)
        self.action_amera.setObjectName("action_amera")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDuplicate = QtWidgets.QAction(MainWindow)
        self.actionDuplicate.setObjectName("actionDuplicate")
        self.actionCascade = QtWidgets.QAction(MainWindow)
        self.actionCascade.setObjectName("actionCascade")
        self.actionRename = QtWidgets.QAction(MainWindow)
        self.actionRename.setObjectName("actionRename")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionZoom_Off = QtWidgets.QAction(MainWindow)
        self.actionZoom_Off.setObjectName("actionZoom_Off")
        self.actionSplitting_into_channels = QtWidgets.QAction(MainWindow)
        self.actionSplitting_into_channels.setObjectName("actionSplitting_into_channels")
        self.actionResize = QtWidgets.QAction(MainWindow)
        self.actionResize.setObjectName("actionResize")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHistogram = QtWidgets.QAction(MainWindow)
        self.actionHistogram.setObjectName("actionHistogram")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionStretching = QtWidgets.QAction(MainWindow)
        self.actionStretching.setObjectName("actionStretching")
        self.actionEqualization = QtWidgets.QAction(MainWindow)
        self.actionEqualization.setObjectName("actionEqualization")
        self.actionNegation = QtWidgets.QAction(MainWindow)
        self.actionNegation.setObjectName("actionNegation")
        self.actionThresholding = QtWidgets.QAction(MainWindow)
        self.actionThresholding.setObjectName("actionThresholding")
        self.actionPosterize = QtWidgets.QAction(MainWindow)
        self.actionPosterize.setObjectName("actionPosterize")
        self.actionPosterize_with_LUT = QtWidgets.QAction(MainWindow)
        self.actionPosterize_with_LUT.setObjectName("actionPosterize_with_LUT")
        self.actionBlur = QtWidgets.QAction(MainWindow)
        self.actionBlur.setObjectName("actionBlur")
        self.actionGaussian_Blur = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur.setObjectName("actionGaussian_Blur")
        self.actionMedian_Blur = QtWidgets.QAction(MainWindow)
        self.actionMedian_Blur.setObjectName("actionMedian_Blur")
        self.actionLaplacian = QtWidgets.QAction(MainWindow)
        self.actionLaplacian.setObjectName("actionLaplacian")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionCanny = QtWidgets.QAction(MainWindow)
        self.actionCanny.setObjectName("actionCanny")
        self.actionLinear_sharpening = QtWidgets.QAction(MainWindow)
        self.actionLinear_sharpening.setObjectName("actionLinear_sharpening")
        self.actionDirectional = QtWidgets.QAction(MainWindow)
        self.actionDirectional.setObjectName("actionDirectional")
        self.actionUniversal = QtWidgets.QAction(MainWindow)
        self.actionUniversal.setObjectName("actionUniversal")
        self.actionImage_calculator = QtWidgets.QAction(MainWindow)
        self.actionImage_calculator.setObjectName("actionImage_calculator")
        self.actionMorphology = QtWidgets.QAction(MainWindow)
        self.actionMorphology.setObjectName("actionMorphology")
        self.actionThresholdingSegmentation = QtWidgets.QAction(MainWindow)
        self.actionThresholdingSegmentation.setObjectName("actionThresholdingSegmentation")
        self.actionWatershed = QtWidgets.QAction(MainWindow)
        self.actionWatershed.setObjectName("actionWatershed")
        self.actionMoments = QtWidgets.QAction(MainWindow)
        self.actionMoments.setObjectName("actionMoments")
        self.actionArea = QtWidgets.QAction(MainWindow)
        self.actionArea.setObjectName("actionArea")
        self.actionAspect_ratios = QtWidgets.QAction(MainWindow)
        self.actionAspect_ratios.setObjectName("actionAspect_ratios")
        self.actionNeural_transfer_of_style = QtWidgets.QAction(MainWindow)
        self.actionNeural_transfer_of_style.setObjectName("actionNeural_transfer_of_style")
        self.actionRGB_Grayscale = QtWidgets.QAction(MainWindow)
        self.actionRGB_Grayscale.setObjectName("actionRGB_Grayscale")
        self.actionRGB_BGR = QtWidgets.QAction(MainWindow)
        self.actionRGB_BGR.setObjectName("actionRGB_BGR")
        self.actionRGB_HSV = QtWidgets.QAction(MainWindow)
        self.actionRGB_HSV.setObjectName("actionRGB_HSV")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.action_amera)
        self.menuFile.addAction(self.actionExit)
        self.menuWindows.addAction(self.actionCascade)
        self.menuWindows.addAction(self.actionDuplicate)
        self.menuWindows.addAction(self.actionRename)
        self.menuWindows.addAction(self.actionZoom_In)
        self.menuWindows.addAction(self.actionZoom_Out)
        self.menuWindows.addAction(self.actionZoom_Off)
        self.menuHistogram_manipulation.addAction(self.actionStretching)
        self.menuHistogram_manipulation.addAction(self.actionEqualization)
        self.menuPoint_operations.addAction(self.actionNegation)
        self.menuPoint_operations.addAction(self.actionThresholding)
        self.menuPoint_operations.addAction(self.actionPosterize)
        self.menuPoint_operations.addAction(self.actionPosterize_with_LUT)
        self.menuBlurring.addAction(self.actionBlur)
        self.menuBlurring.addAction(self.actionGaussian_Blur)
        self.menuBlurring.addAction(self.actionMedian_Blur)
        self.menuEdge_detection.addAction(self.actionLaplacian)
        self.menuEdge_detection.addAction(self.actionSobel)
        self.menuEdge_detection.addAction(self.actionCanny)
        self.menuEdge_detection.addAction(self.actionDirectional)
        self.menuLocal_operations.addAction(self.menuBlurring.menuAction())
        self.menuLocal_operations.addAction(self.menuEdge_detection.menuAction())
        self.menuLocal_operations.addAction(self.actionLinear_sharpening)
        self.menuLocal_operations.addAction(self.actionUniversal)
        self.menuLocal_operations.addAction(self.actionMorphology)
        self.menuSegmentation.addAction(self.actionThresholdingSegmentation)
        self.menuSegmentation.addAction(self.actionWatershed)
        self.menuConversion.addAction(self.actionRGB_Grayscale)
        self.menuConversion.addAction(self.actionRGB_BGR)
        self.menuConversion.addAction(self.actionRGB_HSV)
        self.menuProcessing.addAction(self.menuConversion.menuAction())
        self.menuProcessing.addAction(self.actionResize)
        self.menuProcessing.addAction(self.actionSplitting_into_channels)
        self.menuProcessing.addSeparator()
        self.menuProcessing.addAction(self.menuHistogram_manipulation.menuAction())
        self.menuProcessing.addAction(self.menuPoint_operations.menuAction())
        self.menuProcessing.addAction(self.menuLocal_operations.menuAction())
        self.menuProcessing.addAction(self.actionImage_calculator)
        self.menuProcessing.addAction(self.menuSegmentation.menuAction())
        self.menuAnalyzing.addAction(self.actionHistogram)
        self.menuAnalyzing.addAction(self.actionMoments)
        self.menuAnalyzing.addAction(self.actionArea)
        self.menuAnalyzing.addAction(self.actionAspect_ratios)
        self.menuAnalyzing.addAction(self.actionInfo)
        self.menuAI.addAction(self.actionNeural_transfer_of_style)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAuthor)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuProcessing.menuAction())
        self.menubar.addAction(self.menuAnalyzing.menuAction())
        self.menubar.addAction(self.menuAI.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing App"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuProcessing.setTitle(_translate("MainWindow", "Processing"))
        self.menuHistogram_manipulation.setTitle(_translate("MainWindow", "Histogram manipulation"))
        self.menuPoint_operations.setTitle(_translate("MainWindow", "Point operations"))
        self.menuLocal_operations.setTitle(_translate("MainWindow", "Local operations"))
        self.menuBlurring.setTitle(_translate("MainWindow", "Blurring"))
        self.menuEdge_detection.setTitle(_translate("MainWindow", "Edge detection"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuConversion.setTitle(_translate("MainWindow", "Conversion"))
        self.menuAnalyzing.setTitle(_translate("MainWindow", "Analyzing"))
        self.menuAI.setTitle(_translate("MainWindow", "AI"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.action_amera.setText(_translate("MainWindow", "Сamera"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDuplicate.setText(_translate("MainWindow", "Duplicate"))
        self.actionCascade.setText(_translate("MainWindow", "Cascade"))
        self.actionRename.setText(_translate("MainWindow", "Rename"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_Off.setText(_translate("MainWindow", "Zoom Off"))
        self.actionSplitting_into_channels.setText(_translate("MainWindow", "Splitting into channels"))
        self.actionResize.setText(_translate("MainWindow", "Resize"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHistogram.setText(_translate("MainWindow", "Histogram"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionStretching.setText(_translate("MainWindow", "Stretching"))
        self.actionEqualization.setText(_translate("MainWindow", "Equalization"))
        self.actionNegation.setText(_translate("MainWindow", "Negation"))
        self.actionThresholding.setText(_translate("MainWindow", "Thresholding"))
        self.actionPosterize.setText(_translate("MainWindow", "Posterize"))
        self.actionPosterize_with_LUT.setText(_translate("MainWindow", "Posterize with LUT"))
        self.actionBlur.setText(_translate("MainWindow", "Blur"))
        self.actionGaussian_Blur.setText(_translate("MainWindow", "Gaussian Blur"))
        self.actionMedian_Blur.setText(_translate("MainWindow", "Median Blur"))
        self.actionLaplacian.setText(_translate("MainWindow", "Laplacian"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionCanny.setText(_translate("MainWindow", "Canny"))
        self.actionLinear_sharpening.setText(_translate("MainWindow", "Linear sharpening"))
        self.actionDirectional.setText(_translate("MainWindow", "Directional"))
        self.actionUniversal.setText(_translate("MainWindow", "Universal"))
        self.actionImage_calculator.setText(_translate("MainWindow", "Image calculator"))
        self.actionMorphology.setText(_translate("MainWindow", "Morphology"))
        self.actionThresholdingSegmentation.setText(_translate("MainWindow", "Thresholding"))
        self.actionWatershed.setText(_translate("MainWindow", "Watershed"))
        self.actionMoments.setText(_translate("MainWindow", "Moments"))
        self.actionArea.setText(_translate("MainWindow", "Area"))
        self.actionAspect_ratios.setText(_translate("MainWindow", "Aspect ratios"))
        self.actionNeural_transfer_of_style.setText(_translate("MainWindow", "Neural transfer of style"))
        self.actionRGB_Grayscale.setText(_translate("MainWindow", "RGB -> Grayscale"))
        self.actionRGB_BGR.setText(_translate("MainWindow", "RGB -> BGR"))
        self.actionRGB_HSV.setText(_translate("MainWindow", "RGB -> HSV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
