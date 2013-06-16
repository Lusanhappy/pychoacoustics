# -*- coding: utf-8 -*-

#   Copyright (C) 2008-2012 Samuele Carcagno <sam.carcagno@gmail.com>
#   This file is part of pychoacoustics

#    pychoacoustics is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    pychoacoustics is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with pychoacoustics.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import nested_scopes, generators, division, absolute_import, with_statement, print_function, unicode_literals
from PyQt4 import QtGui, QtCore

class swapBlocksDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)

        self.prm = self.parent().prm
        self.currLocale = self.parent().prm['currentLocale']
        self.currLocale.setNumberOptions(self.currLocale.OmitGroupSeparator | self.currLocale.RejectGroupSeparator)
      
        grid = QtGui.QGridLayout()
        n = 0
            
        blockALabel = QtGui.QLabel(self.tr('Block A: '))
        grid.addWidget(blockALabel, n, 0)
        self.blockAWidget = QtGui.QLineEdit(str(self.prm['currentBlock']))
        self.blockAWidget.setValidator(QtGui.QIntValidator(self))
        grid.addWidget(self.blockAWidget, n, 1)

        blockBLabel = QtGui.QLabel(self.tr('Block B: '))
        grid.addWidget(blockBLabel, n, 2)
        self.blockBWidget = QtGui.QLineEdit('')
        self.blockBWidget.setValidator(QtGui.QIntValidator(self))
        grid.addWidget(self.blockBWidget, n, 3)
        
        n = n+1
        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|
                                     QtGui.QDialogButtonBox.Cancel)
        
        self.connect(buttonBox, QtCore.SIGNAL("accepted()"),
                     self, QtCore.SLOT("accept()"))
        self.connect(buttonBox, QtCore.SIGNAL("rejected()"),
                     self, QtCore.SLOT("reject()"))
        grid.addWidget(buttonBox, n, 3)
        self.setLayout(grid)
        self.setWindowTitle(self.tr("Swap Blocks"))

  
        
