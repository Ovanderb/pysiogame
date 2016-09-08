# -*- coding: utf-8 -*-

accent_map = {'ά':'´α', 'έ':'´ε', 'ή':'´η', 'ί':'´ι','ϊ':'¨ι', 'ό':'´ο', 'ύ':'´υ', 'ϋ':'¨υ', 'Ϋ':'¨Υ', 'ώ':'´ω', 'Ά':'´Α', 'Έ':'´Ε', 'Ή':'´Η', 'Ί':'´Ι', 'Ϊ':'´Ι', 'Ό':'´Ο', 'Ύ':'´Υ', 'Ώ':'´Ω'}
accent_map2 = {'ϊ':'¨ι', 'Ϊ':'´Ι', 'ϋ':'¨υ', 'Ϋ':'¨Υ'}

kbrd_keys = [[0,0,25,22,"~","`","","","","",0],#0
[30,0,25,22,"!","1","","","","",0],
[60,0,25,22,'@',"2","","","","",1],
[90,0,25,22,"#","3","","","","",2],
[120,0,25,22,"$","4","","","","",3],
[150,0,25,22,"%","5","","","","",3],
[180,0,25,22,"^","6","","","","",4],
[210,0,25,22,"&","7","","","","",4],
[240,0,25,22,"*","8","","","","",5],
[270,0,25,22,"(","9","","","","",6],
[300,0,25,22,")","0","","","","",7],
[330,0,25,22,"_","-","","","","",7],
[360,0,25,22,"+","=","","","","",7],
[390,0,0,0,"","","","","","",7],
[390,0,55,22,"","","← Backspace","","","",7],#14

[0,27,43,22,"","","Tab","","","",0],#15
[48,27,25,22,":",";","","","","",0],
[78,27,25,22,"","ς","","Σ","","",1],
[108,27,25,22,"","ε","","Ε","","",2],
[138,27,25,22,"","ρ","","Ρ","","",3],
[168,27,25,22,"","τ","","Τ","","",3],
[198,27,25,22,"","υ","","Υ","","",4],
[228,27,25,22,"","θ","","Θ","","",4],
[258,27,25,22,"","ι","","Ι","","",5],
[288,27,25,22,"","ο","","Ο","","",6],
[318,27,25,22,"","π","","Π","","",7],
[348,27,25,22,"{","[","","","","",7],
[378,27,25,22,"}","]","","","","",7],
[408,27,37,22,"","","Enter","","","",7],#28

[0,54,50,22,"","","Caps Lock","","","",0],#29
[55,54,25,22,"","α","","Α","","",0],
[85,54,25,22,"","σ","","Σ","","",1],
[115,54,25,22,"","δ","","Δ","","",2],
[145,54,25,22,"","φ","","Φ","","",3],
[175,54,25,22,"","γ","","Γ","","",3],
[205,54,25,22,"","η","","Η","","",4],
[235,54,25,22,"","ξ","","Ξ","","",4],
[265,54,25,22,"","κ","","Κ","","",5],
[295,54,25,22,"","λ","","Λ","","",6],
[325,54,25,22,"¨","´","","","","",7],
[355,54,25,22,'"',"'","","","","",7],
[385,54,25,22,"|","\\","","","","",7],
[415,48,30,28,"","","","","","",7],#42

#alphabet_uc = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
#alphabet_lc = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']

[0,81,30,22,"","","Shift","","","",0],#43
[35,81,25,22,"»","«","","","","",0],
[65,81,25,22,"","ζ","","Ζ","","",0],
[95,81,25,22,"","χ","","Χ","","",1],
[125,81,25,22,"","ψ","","Ψ","","",2],
[155,81,25,22,"","ω","","Ω","","",3],
[185,81,25,22,"","β","","Β","","",3],
[215,81,25,22,"","ν","","Ν","","",4],
[245,81,25,22,"","μ","","Μ","","",4],
[275,81,25,22,"<",",","","","","",5],
[305,81,25,22,">",".","","","","",6],
[335,81,25,22,"?","/","","","","",7],
#[365,81,25,22,"|","/","","","","",7],
#[395,81,50,22,"","","Shift","","","",7],#55
[365,81,80,22,"","","Shift","","","",7],#55

[0,108,33,22,"","","Ctrl","","","",9],#56
[38,108,25,22,"","","","","","",9],
[68,108,25,22,"","","Alt","","","",9],
[98,108,214,22,"","","Space","","","",8],
[317,108,25,22,"","","Alt Gr","","","",9],
[347,108,25,22,"","","","","","",9],
[377,108,25,22,"","","","","","",9],
[407,108,38,22,"","","Ctrl","","","",9],#63

#Hand
[100,178,16,17,"","","","","","",0],#64 x+17
[122,151,17,19,"","","","","","",1],#x+4 w-8  x+2 y+2
[143,135,18,19,"","","","","","",2],#x y+2
[169,140,16,18,"","","","","","",3],#x-1 y+3

[261,140,16,18,"","","","","","",4],
[285,135,18,19,"","","","","","",5],
[307,151,17,19,"","","","","","",6],
[330,178,16,17,"","","","","","",7],#71

[203,186,18,20,"","","","","","",8],#Lt Thumb - Space - 72
[225,186,18,20,"","","","","","",8]]#Rt Thumb - Alt Gr - 73

"""
[0,81,60,22,"","","Shift","","","",0],#43
[65,81,25,22,"","","","Z","","",0],
[95,81,25,22,"","","","X","","",1],
[125,81,25,22,"","","","C","","",2],
[155,81,25,22,"","","","V","","",3],
[185,81,25,22,"","","","B","","",3],
[215,81,25,22,"","","","N","","",4],
[245,81,25,22,"","","","M","","",4],
[275,81,25,22,"<",",","","","","",5],
[305,81,25,22,">",".","","","","",6],
[335,81,25,22,"?","/","","","","",7],
[365,81,25,22,"|","\\","","","","",7],
[395,81,50,22,"","","Shift","","","",7],#55
"""