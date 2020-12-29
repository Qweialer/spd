import math

# need connect module "math"

# example: spd.spd_sq(a)
def spd_sq(a):	#S, P, D
	s = a * a
	p = a * 4
	d = a * math.sqrt(2)

	print("P = " + str(p) + "; S = " + str(s) + "; d = " + str(d))

# example: spd.spd_tr(a, b)
def spd_rt(a, b): # S, P, D
	s = a * b
	p = a + b
	p *= 2
	d = a * a
	d += b * b

	print("P = " + str(p) + "; S = " + str(s) + "; d = " + str(d))

# example: spd.sp_tr(a, b, c, h)
def sp_tr(a, b, c, h): # P and S
	p = a + b + c
	ah = a * h
	s = ah / 2

	print("P = " + str(p) + "; S = " + str(s))

# example: sp_crcl(p, r, pi, pi2, r2, s)
def sp_crcl(r):
	pi = math.pi * 2
	pi2 = pi * r 
	r2 = r * r

	p = 2 * pi2
	s = math.pi * pi2

	print("P = " + str(p) + "; S = " + str(s))

# example: spd.rp_crcl(p)
def rp_crcl(p):	# if know P 
	pr = 2 * math.pi
	r = p / pr

	print("R = " + str(r))

# example: spd.rs_crcl(r, s)
def rs_crcl(r, s):	   # if know S
	sqsp = s / math.pi
	r = sqsp.math.sqrt(sqsp)

	print("R = " + str(r))

# example: spd.rd_crcl(d, r)
def rd_crcl(d,):	   # if know D
	r = d / 2

	print("R = " + str(r))

# if you find a bug, or want to offer me help, write to alex.raz1apov@gmail.com
# Thanks for using this module!
# Made by Qweialer for @Qweialer
