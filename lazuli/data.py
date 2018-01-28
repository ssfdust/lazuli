#!env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 RedLotus <ssfdust@gmail.com>
# Author: RedLotus <ssfdust@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import pandas as pd

class LazuliCore(object):
    def __init__(self, filename, **kwargs):
        self.filename = filename
        self.options = dict(kwargs)
        self.data = None
        self.result = None
        self.row = 0
        self.initilize()

    def initlize(self):
        if self.filename.endswith('.csv'):
            # handle csv files
            self.data = pd.read_csv(self.filename)
        elif self.filename.endswith('.xls') or self.filename.endswith('.xlsx'):
            self.data = pd.read_excel(self.filename)
        else:
            raise ValueError('Unsupported file type')

        self.result = self.data[0:25]

    def set_columns(self, col_arr):
        self.data = self.data.iloc[:,col_arr]
        sefl.result = self.data

    def set_rows(self, row_arr):
        start = row_arr[0]
        end = row_arr[1]
        self.data = self.data[start:end]
        self.result = self.data
            
    def get_head(self, n):
        self.result = self.data.head(n)
        return self.dict_result

    def get_dict_columns(self):
        cols = self.data.columns.values.tolist()
        self.result = {'col_{}'.format(i):d for i, d in enumerate(cols)}
        return self.dict_result

    def get_dict_contents(self):
        return self.data.to_dict('records')

    @property
    def dict_result(self):
        return self.result.to_dict('records')

