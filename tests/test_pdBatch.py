import pytest

import datetime

import ExpMeta

##############################################################################

EXP_DB_PATH = "assets/exp_db/"

@pytest.fixture
def sample_meas_1():
	meas_obj = ExpMeta.Measurement(db_dir=EXP_DB_PATH, experiment="X1", snum=24, sort_date=datetime.date(year=2021,month=4,day=24))
	return meas_obj

@pytest.fixture
def batch_vary_snums():
	meas_batch = ExpMeta.pdBatch(db_dir=EXP_DB_PATH,
								 experiment="X1",
								 snums=range(20,28+1),
								 sort_date=datetime.date(
									 			year=2021,month=4,day=24))
	return meas_batch

@pytest.fixture
def batch_vary_snums_subset():
	meas_batch = ExpMeta.pdBatch(db_dir=EXP_DB_PATH,
								 experiment="X1",
								 snums=range(22,25+1),
								 sort_date=datetime.date(
									 			year=2021,month=4,day=24))
	return meas_batch

@pytest.fixture
def batch_vary_snums_2():
	meas_batch = ExpMeta.pdBatch(db_dir=EXP_DB_PATH,
								 experiment="X2",
								 snums=range(1,4+1),
								 sort_date=datetime.date(
									 			year=2021,month=5,day=3))
	return meas_batch


@pytest.fixture
def batch_vary_experiments(batch_vary_snums, batch_vary_snums_2):
	return batch_vary_snums + batch_vary_snums_2


##############################################################################
## Representation & formatting
##############################################################################


## String formatting
####################

def test_str_format_single_experiment(batch_vary_snums):
	assert "{}".format(batch_vary_snums) == "X1_0020-0028"

def test_name_single_experiment(batch_vary_snums):
	assert batch_vary_snums.name == "X1_0020-0028"


def test_str_format_multiple_experiments(batch_vary_experiments):
	assert "{}".format(batch_vary_experiments) == "X1_0020-X2_0004"


def test_name_multiple_experiments(batch_vary_experiments):
	assert batch_vary_experiments.name == "X1_0020-X2_0004"


##############################################################################
## Item access and attributes
##############################################################################


def test_len(batch_vary_snums):
	assert len(batch_vary_snums) == 9


## Direct access
################

def test_meas_access_via_string(batch_vary_snums, sample_meas_1):
	assert batch_vary_snums["X1_0024"] == sample_meas_1


def test_meas_access_via_meas_obj(batch_vary_snums, sample_meas_1):
	assert batch_vary_snums[sample_meas_1] == sample_meas_1


def test_meas_access_via_index(batch_vary_snums, sample_meas_1):
	assert batch_vary_snums[4] == sample_meas_1


def test_meas_access_via_slice(batch_vary_snums, batch_vary_snums_subset):
	assert batch_vary_snums[slice(2,5+1)] == batch_vary_snums_subset


##############################################################################
## Data manipulation
##############################################################################

## Compound construction
########################

def test_list_construction(batch_vary_experiments):
	## Construct the iterables for experiment, snums, and sort_date attributes
	experiment_list = ["X1"]*9 + ["X2"]*4
	snums_list = list(range(20,28+1))+list(range(1,4+1))
	sort_date_list = [datetime.date(year=2021,month=4,day=24)]*9 \
					+ [datetime.date(year=2021,month=5,day=3)]*4
	## Construct a pdBatch object out of all of these
	compound_batch = ExpMeta.pdBatch(db_dir=EXP_DB_PATH,
									 experiment=experiment_list,
									 snums=snums_list,
									 sort_date=sort_date_list)
	## Check that this is the same as the one from addition of the two
	## constituent batches
	assert compound_batch == batch_vary_experiments


## Reflexive operations
#######################

def test_reflexive_addition(batch_vary_snums, batch_vary_snums_2):
	assert (batch_vary_snums + batch_vary_snums_2) == \
		   (batch_vary_snums_2 + batch_vary_snums)
