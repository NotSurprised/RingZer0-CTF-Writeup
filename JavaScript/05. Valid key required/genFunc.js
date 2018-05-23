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
console.log(genFunc("ABCD"));