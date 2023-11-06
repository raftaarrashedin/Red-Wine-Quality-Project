import pytest

class NotInRange(Exception) :
	def __init__(self, message="value not in range") :
		self.message = message
		super().__init__(self.message)


# 8080142595
def test_generic() :
	a = 5
	with pytest.raises(NotInRange) :
		if a not in range(10,20) :
			raise NotInRange
	# b = 2
	# assert a == b



def test_something() :
	a = 2
	b = 2
	assert True