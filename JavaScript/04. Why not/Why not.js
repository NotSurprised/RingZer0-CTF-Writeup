var k = new Array(176,214,205,246,264,255,227,237,242,244,265,270,283);
u == "administrator"
p = []
for(i = 0; i< u.length; i++)
{
    p.push(k[i] - i*10 - u.charCodeAt(i))
}
String.fromCharCode.apply(null, p);