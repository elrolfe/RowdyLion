from time import time
from math import sqrt, log

_seed = []

_n = 0
_k0 = 0
_k1 = 0
_k2 = 0
_k3 = 0
_s = []

def _mash(data):
	global _n

	data_str = str(data)

	for i in range(len(data_str)):
		_n += ord(data_str[i])
		h = 0.02519603282416938 * _n
		_n = int(h)
		h -= _n
		h *= _n
		_n = int(h)
		h -= _n
		_n += h * 0x100000000

	return int(_n) * 2.3283064365386963e-10;

def get_seed():
	global _seed
	return _seed

def normal(mean = 0, std = 1):
	r = 0

	while r > 1 or r == 0:
		u = 2 * random() - 1;
		v = 2 * random() - 1;
		r = u * u + v * v

	gauss = u * sqrt(-2 * log(r) / r)
	return mean + gauss * std

def normal_range(min, max):
	mean = (min + max) / 2.0
	sigma = (max - mean) / 3.0
	num = min - 1

	while num < min or num > max:
		num = int(normal(mean, sigma))

	return num

def random():
	global _k0, _k1, _k2, _k3, _s
	_k0 = (_k0 + 1) & 255
	_k1 = (_k1 + 1) & 255
	_k2 = (_k2 + 1) & 255
	_k3 = (_k3 + 1) & 255

	x = _s[_k0] - _s[_k1]
	if x < 0:
		x += 1

	x -= _s[_k2]
	if x < 0:
		x += 1

	x -= _s[_k3]
	if x < 0:
		x += 1

	_s[_k0] = x
	return x

def random_range(min, max):
	return int(random() * (max - min + 1)) + min

def set_seed(*arguments):
	global _s, _n, _k0, _k1, _k2, _k3, _seed
	_s = []
	_n = 0xefc8249d
	_k0 = 0
	_k1 = 58
	_k2 = 119
	_k3 = 178

	if len(arguments) == 0:
		args = [time()]
	else:
		args = arguments

	_seed = []

	for j in range(256):
		_s.append(_mash(" "))
		_s[j] -= _mash(" ") * 4.76837158203125e-7
		if _s[j] < 0:
			_s[j] += 1

	for i in range(len(args)):
		_seed.append(args[i])

		for j in range(256):
			_s[j] -= _mash(args[i])
			_s[j] -= _mash(args[i]) * 4.76837158203125e-7
			if _s[j] < 0:
				_s[j] += 1


# Setup Code

set_seed();