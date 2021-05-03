import pytest

import datetime
import os

import expmeta

##############################################################################

@pytest.fixture
def sample_meas_1():
	meas_obj = expmeta.Measurement(db_dir="assets/exp_db/", experiment="X1", snum=24, sort_date=datetime.date(year=2021,month=4,day=24))
	return meas_obj

@pytest.fixture
def sample_meas_2():
	meas_obj = expmeta.Measurement(db_dir="", experiment="X1", snum=32, sort_date=datetime.date(year=2021,month=4,day=24))
	return meas_obj

@pytest.fixture
def sample_meas_3():
	meas_obj = expmeta.Measurement(db_dir="", experiment="X2", snum=24, sort_date=datetime.date(year=2021,month=4,day=24))
	return meas_obj


##############################################################################
## Representation & formatting
##############################################################################


## Implicit type conversion
###########################

def test_str_conversion(sample_meas_1):
	assert str(sample_meas_1) == "X1_0024"


def test_int_conversion(sample_meas_1):
	assert int(sample_meas_1) == 24


def test_hash(sample_meas_1):
	assert hash(sample_meas_1) == hash(("X1", 24))


## String formatting
####################

def test_str_format_generic(sample_meas_1):
	assert "{}".format(sample_meas_1) == "X1_0024"


def test_str_format_string(sample_meas_1):
	assert "{:s}".format(sample_meas_1) == "X1_0024"


def test_str_format_decimal(sample_meas_1):
	assert "{:d}".format(sample_meas_1) == "24"


## Arithmetic comparison
########################

def test_lt(sample_meas_1, sample_meas_2, sample_meas_3):
	assert (sample_meas_1 < sample_meas_2) \
			and (sample_meas_2 < sample_meas_3) \
			and (sample_meas_1 < sample_meas_3) \
			and not(sample_meas_1 < sample_meas_1)


def test_le(sample_meas_1, sample_meas_2, sample_meas_3):
	assert (sample_meas_1 <= sample_meas_2) \
			and (sample_meas_2 <= sample_meas_3) \
			and (sample_meas_1 <= sample_meas_3) \
			and (sample_meas_1 <= sample_meas_1)


def test_eq(sample_meas_1, sample_meas_2, sample_meas_3):
	assert not(sample_meas_1 == sample_meas_2) \
			and not(sample_meas_2 == sample_meas_3) \
			and not(sample_meas_1 == sample_meas_3) \
			and (sample_meas_1 == sample_meas_1)


def test_ne(sample_meas_1, sample_meas_2, sample_meas_3):
	assert (sample_meas_1 != sample_meas_2) \
			and (sample_meas_2 != sample_meas_3) \
			and (sample_meas_1 != sample_meas_3) \
			and not(sample_meas_1 != sample_meas_1)


def test_gt(sample_meas_1, sample_meas_2, sample_meas_3):
	assert not(sample_meas_1 > sample_meas_2) \
			and not(sample_meas_2 > sample_meas_3) \
			and not(sample_meas_1 > sample_meas_3) \
			and not(sample_meas_1 > sample_meas_1)


def test_ge(sample_meas_1, sample_meas_2, sample_meas_3):
	assert not(sample_meas_1 >= sample_meas_2) \
			and not(sample_meas_2 >= sample_meas_3) \
			and not(sample_meas_1 >= sample_meas_3) \
			and (sample_meas_1 >= sample_meas_1)


## Compound attributes
######################

def test_attr_serial(sample_meas_1):
	assert sample_meas_1.serial == "0024"


def test_attr_name(sample_meas_1):
	assert sample_meas_1.name == "X1_0024"


def test_attr_directory(sample_meas_1):
	assert sample_meas_1.directory == "assets/exp_db/2021/04/Data_0424"


def test_attr_path(sample_meas_1):
	assert sample_meas_1.path == os.path.normpath("assets/exp_db/2021/04/Data_0424/X1_0024.hdf5")

