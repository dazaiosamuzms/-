//破解encSecKey


function() {
	function a(a) {
		var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
			c = "";
		for (d = 0; a > d; d += 1) e = Math.random() * b.length, e = Math.floor(e), c += b.charAt(e);
		return c  //a(16) = 'qmkzY0zfadibDSQi'
	}
	function b(a, b) {
		var c = CryptoJS.enc.Utf8.parse(b),
			d = CryptoJS.enc.Utf8.parse("0102030405060708"),
			e = CryptoJS.enc.Utf8.parse(a),
			f = CryptoJS.AES.encrypt(e, c, {
				iv: d,
				mode: CryptoJS.mode.CBC
			});
		return f.toString()
	}
	function c(a, b, c) {
		var d, e;
		return setMaxDigits(131), d = new RSAKeyPair(b, "", c), e = encryptedString(d, a)
	}
	function d(d, e, f, g) {
		var h = {},
			i = a(16);//i = 'qmkzY0zfadibDSQi'
		// 返回h，分别为h.encText=KT7bk6McOWcx24dJ0gGaunDxzveF48mnUrMjq92qZcvCnduN/yJA5nnBnsi1FQaaIrXQs1PJlhtf2wd1rCkeSw52Hkqf1xvbAyKS1UadoXtKQG/sXNoSgEc2LON/NiLw

        //h.encSecKey = bf50d0bcf56833b06d8d1219496a452a1d860fd58a14c0aafba3e770104ca77dc6856cb310ed330
        // 9039e6865081be4ddc2df52663373b20b70ac25b4d0c6ca466daef6b50174e93536e2d580c49e70649ad19365848
        // 99e85722eb83ceddfb4f56c1172fca5e60592d0e6ee3e8e02be1fe6e53f285b0389162d8e6ddc553857cd
		return h.encText = b(d, g), h.encText = b(h.encText, i), h.encSecKey = c(i, e, f), h
	}
	function e(a, b, d, e) {
		var f = {};
		return f.encText = c(a + e, b, d), f
	}
	window.asrsea = d, window.ecnonasr = e
}();

(function() {
	var c4g = NEJ.P,
		eq6k = c4g("nej.g"),
		v5A = c4g("nej.j"), //返回window, 且window['nej'], window['nej']['j'] = {}, {}
		k4o = c4g("nej.u"),  //window.nej.u
		WU9L = c4g("nm.x.ek"),// window.nm.x.ek
		l4p = c4g("nm.x");
	if (v5A.bl5q.redefine) return; //v5A.bl5q.redefine为ture直接返回
	window.GEnc = true;
	var brA6u = function(cwG9x) {
			var m4q = [];
			k4o.be5j(cwG9x, function(cwE9v) {
				m4q.push(WU9L.emj[cwE9v])
			});
			return m4q.join("")  //m4q = ["01000", "1"], return "010001"
		};
	var cwC9t = v5A.bl5q;
	v5A.bl5q = function(Y5d, e4i) { //window.nej.j.bl5q
		var i4m = {},
			e4i = NEJ.X({}, e4i),
			mp9g = Y5d.indexOf("?");
		if (window.GEnc && /(^|\.com)\/api/.test(Y5d) && !(e4i.headers && e4i.headers[eq6k.Bx3x] == eq6k.Iy5D) && !e4i.noEnc) {
			if (mp9g != -1) {
				i4m = k4o.hc8U(Y5d.substring(mp9g + 1));
				Y5d = Y5d.substring(0, mp9g)
			}
			if (e4i.query) {
				i4m = NEJ.X(i4m, k4o.fQ7J(e4i.query) ? k4o.hc8U(e4i.query) : e4i.query)
			}
			if (e4i.data) {
				i4m = NEJ.X(i4m, k4o.fQ7J(e4i.data) ? k4o.hc8U(e4i.data) : e4i.data)
			}
			i4m["csrf_token"] = v5A.gO8G("__csrf"); //i4m["csrf_token"] = cc2c0bd6e78145ae849bc988f817b84c
			Y5d = Y5d.replace("api", "weapi");
			e4i.method = "post";
			delete e4i.query;
			//window.asrsea = d, 有4个参数， 1.'{"ids":"[29787184]","br":128000,"csrf_token":"cc2c0bd6e78145ae849bc988f817b84c"}', 2. "010001", 3."00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b72
            // 5152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cc
            // e10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7",  4."0CoJUm6Qyw8W8jud"
			var bUK1x = window.asrsea(JSON.stringify(i4m), brA6u(["流泪", "强"]), brA6u(WU9L.md), brA6u(["爱心", "女孩", "惊恐", "大笑"]));
			e4i.data = k4o.cz5E({
				params: bUK1x.encText,
				encSecKey: bUK1x.encSecKey
			})
		}
		cwC9t(Y5d, e4i)
	};
	v5A.bl5q.redefine = true
})();




//各个参数破解

function RSAKeyPair(a, b, c) {
	this.e = biFromHex(a), this.d = biFromHex(b), this.m = biFromHex(c), this.chunkSize = 2 * biHighIndex(this.m), this.radix = 16, this.barrett = new BarrettMu(this.m)
}
var maxDigits, ZERO_ARRAY, bigZero, bigOne, dpl10, lr10, hexatrigesimalToChar, hexToChar, highBitMasks, lowBitMasks, biRadixBase = 2;
function setMaxDigits(a) {
	maxDigits = a, ZERO_ARRAY = new Array(a);
	for (var b = 0; b < 2; b++) ZERO_ARRAY[b] = 0; // array[a] = [0, 0,...]
    //bigOne.digits = array[a] = [0, 0,...]   bigOne.digits = array[a] = [1, 0,...]
	bigZero = new BigInt, bigOne = new BigInt, bigOne.digits[0] = 1
}
// digits = ZERO_ARRAY, 即array[a] = [0, 0,...]
function BigInt(a) {
	this.digits = "boolean" == typeof a && 1 == a ? null : ZERO_ARRAY.slice(0)
}

function biFromHex(a) {
	var d, e, b = new BigInt, //array[a] = [0, 0,...]
		c = a.length;
	//                                                                               max（d-4, 0）         min(d, 4)
	for (d = c, e = 0; d > 0; d -= 4, ++e) b.digits[e] = hexToDigit(a.substr(Math.max(d - 4, 0), Math.min(d, 4)));
	return b
}

	function c(a, b, c) {
		var d, e;
		return setMaxDigits(131), d = new RSAKeyPair(b, "", c), e = encryptedString(d, a)
