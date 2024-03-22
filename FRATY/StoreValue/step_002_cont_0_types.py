import smartpy as sp

tstorage = sp.record(storedValue = sp.int).layout("storedValue")
tparameter = sp.variant(divide = sp.record(divisor = sp.int).layout("divisor"), double = sp.unit, replace = sp.record(value = sp.int).layout("value")).layout(("divide", ("double", "replace")))
tprivates = { }
tviews = { }
