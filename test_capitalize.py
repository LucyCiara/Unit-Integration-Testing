import pytest
from capitalize import *

def testCapitalCase():
    assert capitalCase('elvebakken') == 'Elvebakken'

def testCapitalCaseLowercase():
    assert capitalCase('elvebakken') != 'elvebakken'
