# -*- coding: utf-8 -*-
"""
"""
import os, matplotlib.pyplot as plt, numpy as np


class PlotGraph:
    
    def getBarPlot(self,stockCat, finalList, col, numFeat, folderPath):
        
        my_xticks = [item['stock'] for item in finalList]
        x = np.array([i+1 for i in range(len(my_xticks))])    
    
        if len(my_xticks)>30:
            fSize = 5
        else:
            fSize = 7
    
        #Test Accuracy
        y_test = np.array([item['train_acc']*100 for item in finalList])
        plt.bar(x, y_test, align = 'center', color=col)
        plt.xticks(x, my_xticks, fontsize=fSize ,rotation='vertical')
        plt.title(stockCat + ' ('+ str(numFeat) + ' features) ')
        plt.xlabel('Stocks')
        plt.ylabel("Train Accuracy (%)")
        fig = plt.gcf()
        plt.show()
        plt.draw()
        #Save graph plot in train_Result folder
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
        fig.savefig(folderPath+'Train.png', format='png', bbox_inches='tight', dpi=1000)
        
        
        #Train Accuracy
        y_test = np.array([item['test_acc']*100 for item in finalList])
        plt.bar(x, y_test, align = 'center', color=col)
        plt.xticks(x, my_xticks, fontsize=fSize ,rotation='vertical')
        plt.title(stockCat + ' ('+ str(numFeat) + ' features) ')
        plt.xlabel('Stocks')
        plt.ylabel("Test Accuracy (%)")
        fig = plt.gcf()
        plt.show()
        plt.draw()
        #Save graph plot in test_Result folder
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)        
        fig.savefig(folderPath+'Test.png', format='png', bbox_inches='tight', dpi=1000)    


        