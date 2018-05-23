# **Valid key required**

```javascript=
function curry( orig_func ) {
    var ap = Array.prototype, args = arguments;

    function fn() {
        ap.push.apply( fn.args, arguments ); 
        return fn.args.length < orig_func.length ? fn : orig_func.apply( this, fn.args );
    }

    return function() {
        fn.args = ap.slice.call( args, 1 );
        return fn.apply( this, arguments );
    };
}

function callback(x,y,i,a) {
    return !y.call(x, a[a["length"]-1-i].toString().slice(19,21)) ? x : {};
}

var ref = {T : "BG8",J : "jep",j : "M2L",K : "L23",H : "r1A"};

function validatekey()
{
    e = false;
    var _strKey = "";
    try {
        _strKey = document.getElementById("key").value;
        var a = _strKey.split("-");
        if(a.length !== 5)
            e = true;

        var o=a.map(genFunc).reduceRight(callback, new (genFunc(a[4]))(Function));

        if(!equal(o,ref))
            e = true;

    }catch(e){
        e = true;
    }

    if(!e) {
        if(document.location.href.indexOf("?p=") == -1) {
            document.location = document.location.href + "?p=" + _strKey;
        }
    } else {
        $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
    }   
}

function equal(o,o1)
{
    var keys1 = Object.keys(o1);
    var keys = Object.keys(o);
    if(keys1.length != keys.length)
        return false;

    for(var i=0;i<keys.length;i++)
        if(keys[i] != keys1[i] || o[keys[i]] != o1[keys1[i]])
            return false;

    return true;

}

function hook(f1,f2,f3) {
    return function(x) { return f2(f1(x),f3(x));};
}

var h = curry(hook);
var fn = h(function(x) {return x >= 48;},new Function("a","b","return a && b;"));
function genFunc(_part) {
    if(!_part || !(_part.length) || _part.length !== 4)
        return function() {};

    return new Function(_part.substring(1,3), "this." + _part[3] + "=" + _part.slice(1,3) + "+" + (fn(function(y){return y<=57})(_part.charCodeAt(0)) ?  _part[0] : "'"+ _part[0] + "'"));
}
```

In major function `validatekey()`, we need to make sure `e` remain in default value: `false`, to it out put the `Flag`. 

After `input` split by `-`, its length should be **5**. 

Then put it into minor part :
```javascript
var o=a.map(genFunc).reduceRight(callback, new (genFunc(a[4]))(Function));
```

Final, compare return value with KEY :
```javascript
var ref = {T : "BG8",J : "jep",j : "M2L",K : "L23",H : "r1A"};
```

Let's trace deep inside, then I extract following script after I read it.

```javascript
function curry( orig_func ) {
    var ap = Array.prototype, args = arguments;

    function fn() {
        ap.push.apply( fn.args, arguments ); 
        return fn.args.length < orig_func.length ? fn : orig_func.apply( this, fn.args );
    }

    return function() {
        fn.args = ap.slice.call( args, 1 );
        return fn.apply( this, arguments );
    };
}
function hook(f1,f2,f3) {
    return function(x) { return f2(f1(x),f3(x));};
}
var h = curry(hook);
var fn = h(function(x) {return x >= 48;},new Function("a","b","return a && b;"));
function genFunc(_part) {
    if(!_part || !(_part.length) || _part.length !== 4)
        return function() {};

    return new Function(_part.substring(1,3), "this." + _part[3] + "=" + _part.slice(1,3) + "+" + (fn(function(y){return y<=57})(_part.charCodeAt(0)) ?  _part[0] : "'"+ _part[0] + "'"));
}
```
This is `function genFunc()` actually do:

* It takes a string of 4 characters as input
* It takes the first character of the input as ASCII code (_part.charCodeAt(0)) and checks if:
* ASCII code >= 48 in `function fn()`
* ASCII code <= 57 in `function(y)` inside `fn()`
* In ASCII table 48~57 is the range for digits

Wether the character is digit or not a new function will be build, and `digits` will become `integer` and `characters` will convert into `char` like following sample

```javascript
IN:  console.log(genFunc("ABCD"));
OUT: function anonymous(BC) {this.D=BC+'A'}
```
```javascript
IN:  console.log(genFunc("1BCD"));
OUT: function anonymous(BC) {this.D=BC+1}
```

I couldn't find out the function of `h` in `fn` & `curry()` `hook()`, it seems every thing went fine without `new Function("a","b","return a && b;")` in `fn`.

After that, it use `reduceRight()` and `callback()`

In conclution, `genFunc()` switch `d[i][0]` with `d[i][3]`, then `reduceRight()` and `callback()` switch `d[i][0]&d[i][3]` with `d[5-i][0]&d[5-i][3]`.

```javascript=
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
```

We simply give a sample and let the script to bring out real `input` that fit the KEY.

![](https://i.imgur.com/EFTHKC1.png)
