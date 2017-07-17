var x1 >= 0;
var x2 >= 0;
var x3 >= 0;
var x4 >= 0;
var x5 >= 0;
var x6 >= 0;
var x7 >= 0;
var x8 >= 0;
var x9 >= 0;
var x10 >= 0;

maximize revenue:
	60*x1 + 40*x2 + 35*x3 + 30*x4 + 15*x5 + 
	20*x6 + 50*x7 + 30*x8 + 45*x9 + 15*x10;

subject to constraint1:
	1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5 + 
	1*x6 + 0*x7 + 0*x8 + 1*x9 + 0*x10 <= 7;

subject to constraint2:
	4*x1 + 2*x2 + 2*x3 + 2*x4 + 1*x5 + 
	3*x6 + 2*x7 + 4*x8 + 0*x9 + 1*x10 <= 8;

subject to constraint3:
	0*x1 + 1*x2 + 0*x3 + 1*x4 + 0*x5 + 
	0*x6 + 1*x7 + 1*x8 + 1*x9 + 1*x10 <= 3;

subject to constraint4:
	1*x1 + 0*x2 + 1*x3 + 0*x4 + 0*x5 + 
	0*x6 + 0*x7 + 0*x8 + 0*x9 + 1*x10 <= 1.8;

subject to constraint5:
	0*x1 + 0*x2 + 1*x3 + 0*x4 + 0*x5 + 
	0*x6 + 0*x7 + 0*x8 + 0*x9 + 0*x10 <= 0.3;



