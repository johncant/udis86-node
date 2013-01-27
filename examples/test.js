// Spit out the mnemonic of the first instruction piped into stdin
var UDis86 = require("./build/Release/udis86_wrap.node");
var util = require("util");

var ud_obj = new UDis86.ud();

UDis86.ud_init(ud_obj);

UDis86.ud_disassemble(ud_obj);
console.log(util.inspect(UDis86.ud_lookup_mnemonic(ud_obj.mnemonic)));
