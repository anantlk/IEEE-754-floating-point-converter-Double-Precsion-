import wx
import gui
from math import *
bias=1023
sign=0
exponent=""
mantissa=""


def int_to_binary(val):
	s=val;
	temp="";
	binary=""
	while(s>0):
		d=s%2;
		temp=temp+str(d);
		s=s//2;
	for i in temp[len(temp)-1::-1]:
		binary=binary+i
	if(binary==""):
		return "0";
	else:
		return binary;
	
def fract_to_binary(fract,ite):
	dec_part="";
	for i in range(ite):
		val=int(fract*2);
		fract=fract*2;
		dec_part=dec_part+str(val);
		if(val==1):
			fract=fract-1;
		if(fract.is_integer()):
			break;
	return dec_part
	
	
def convert(inp):
	c=0;
	if(inp[0]=='-'):
		sign=1;
		num=inp[1:];
	elif(inp[0]=='+'):
		sign=0;
		num=inp[1:];
	else:
		sign=0;
		num=inp
	if('.' in num): 
		num=float(num);
		if(int(num)==0):
			while(int(num)!=1):
				num=num*2;
				c=c+1;
		num=str(num);
		pos=num.index('.');
		integer=int(num[0:pos])
		#print(integer)
		binary=int_to_binary(integer);
		fract=float(num[pos:]);
		fract=fract_to_binary(fract,52-(len(binary)-1))
	else:
		integer=int(num)
		#print(integer)
		binary=int_to_binary(integer);
		fract=""
	exponent=int_to_binary(len(binary)-1+bias-c);
	t=52-(len(binary)-1)-len(fract);
	mantissa=binary[1:]+fract+"0"*t;
	exponent="0"*(11-len(exponent))+exponent;
	print(sign);
	print(exponent);
	print(mantissa);
	return str(sign),exponent,mantissa;


class calcFrame(gui.Mainframe):
	def __init__(self,parent):
		gui.Mainframe.__init__(self,parent);
	def SolveFunc(self,event):
		try:
			inp=self.text.GetValue();
			s,e,m=convert(inp);
			self.sign.SetValue(s);
			self.exponent.SetValue(e);
			self.mantissa.SetValue(m);
		except Exception: 
			print("Error");
	def ClearFunc(self,event):
		try:
			self.text.SetValue("");
			self.sign.SetValue("");
			self.exponent.SetValue("");
			self.mantissa.SetValue("");
		except Exception:
			print("Error");
app=wx.App(False);
frame=calcFrame(None)
frame.Show(True);
app.MainLoop()

