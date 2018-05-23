var src = 'abcd-efgh-ijkl-mnop-qrst';
//var mid = 'dbca-hfge-ljki-pnom-trsq';
var dst = 'tbcq-pfgm-ljki-hnoe-drsa';

var key = 'TBG8-Jjep-jM2L-KL23-Hr1A';
var input = key;

for (i=0; i<src.length; i++) {
	p = dst.indexOf(src[i]);
	tmp = input.split('');
	tmp[p] = key[i];
	input = tmp.join('');
}

console.log(input);