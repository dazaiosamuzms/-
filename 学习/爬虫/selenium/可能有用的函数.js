
	NEJ.P = function(Fa4e) {  //Fa4e = 'nej.j'
        if (!Fa4e || !Fa4e.length) return null;  //空则 return null
        var bfK2x = window;
        // for(a = ['nej', 'j'], l = 2, i = 0; i < 2; window[a[i]] = {}, i++)
        for (var a = Fa4e.split("."), l = a.length, i = a[0] == "window" ? 1 : 0; i < l; bfK2x = bfK2x[a[i]] = bfK2x[a[i]] || {}, i++) ;
        return bfK2x  // 返回window['nej'], window['nej']['j'] = {}, {}
    };


    k4o.be5j = function(j4n, cE6y, O5T) {
		if (!j4n || !j4n.length || !k4o.hf8X(cE6y)) return this;
		if ( !! j4n.forEach) {
			j4n.forEach(cE6y, O5T);
			return this
		}
		for (var i = 0, l = j4n.length; i < l; i++) cE6y.call(O5T, j4n[i], i, j4n);
		return this
	};

        t.prototype.forEach = function(t) {
            if (t instanceof Function) for (var i = Object.keys(this.C), n = 0, s = i.length; n < s; n++) {
                var h = i[n];
                t(this.C[h], h)
            }
        },


    b4f.bOu8m = function() {  //b4f = NEJ.C().M5R(window.nej.ut.cO6I)
		this.Ab3x();
		//window.nej.j.bl5q
		v5A.bl5q("/api/song/enhance/player/url", {
			type: "json",
			query: {
				ids: JSON.stringify('29787184'),
				br: 128e3
			},
			onload: this.bOp8h.f4j(this),
			onerror: this.bOp8h.f4j(this)
		})
	};

        this.cw5B = {
			time: 0,
			id: '29787184',
			duration: bm5r.duration / 1e3,
			play: this.cw5B.play,
			stalledRetryCount: 0
		};

    v5A.bl5q = function(Y5d, e4i) {
		var i4m = {},
			e4i = NEJ.X({}, e4i),  //e4i未给则赋值为{}
			mp9g = "/api/cdns".indexOf("?"); //-1
		if (window.GEnc && /(^|\.com)\/api/.test("/api/cdns") && !(e4i.headers && e4i.headers[eq6k.Bx3x] == eq6k.Iy5D) && !e4i.noEnc) {
			if (mp9g != -1) {
				i4m = k4o.hc8U(Y5d.substring(mp9g + 1));
				Y5d = "/api/cdns".substring(0, mp9g)
			}
			if (e4i.query) {  //k4o = window.nej.u
				i4m = NEJ.X(i4m, window.nej.u.fQ7J(e4i.query) ? window.nej.u.hc8U(e4i.query) : e4i.query)
			}
			if (e4i.data) {
				i4m = NEJ.X(i4m, k4o.fQ7J(e4i.data) ? k4o.hc8U(e4i.data) : e4i.data)
			}
			i4m["csrf_token"] = v5A.gO8G("__csrf");
			Y5d = "/api/cdns".substring(0, mp9g).replace("api", "weapi");
			e4i.method = "post";
			delete e4i.query;
			var bUK1x = window.asrsea(JSON.stringify(i4m), brA6u(["流泪", "强"]), brA6u(WU9L.md), brA6u(["爱心", "女孩", "惊恐", "大笑"]));
			e4i.data = k4o.cz5E({
				params: bUK1x.encText,
				encSecKey: bUK1x.encSecKey
			})
		}
		cwC9t(Y5d, e4i)
	};

    NEJ.X = function(gC8u, bT5Y, ec6W) {
		if (!gC8u || !bT5Y) return gC8u;
		ec6W = ec6W || NEJ.F;  //NEJ.F = !1 --false
		for (var x in bT5Y) {
		    // if(true && )
			if (bT5Y.hasOwnProperty(x) && !ec6W(bT5Y[x], x)) gC8u[x] = bT5Y[x]
		}
		return gC8u
	};

			v5A.gO8G("USER_TRIGGER", {
				value: true,
				expire: 1 / (24 * 60),
				path: "/"
			})
//先在控制台执行这段方法后，window.nej.j.gO8G才能被定义
(function() {
	var o = NEJ.O,
		u = NEJ.P("nej.u"),
		j = NEJ.P("nej.j");
	j.gO8G = function() {
		var de6Y = new Date,
			cKe3x = +de6Y,
			biw3x = 864e5;
		var cKd3x = function(X5c) {
				var sD1x = document.cookie,
					tO1x = "\\b" + X5c + "=",
					bew2x = sD1x.search(tO1x);
				if (bew2x < 0) return "";
				bew2x += tO1x.length - 2;
				var yH2x = sD1x.indexOf(";", bew2x);
				if (yH2x < 0) yH2x = sD1x.length;
				return sD1x.substring(bew2x, yH2x) || ""
			};
		return function(X5c, i4m) {
			if (i4m === undefined) return cKd3x(X5c);
			if (u.fQ7J(i4m)) {
				if ( !! i4m) {
					document.cookie = X5c + "=" + i4m + ";";
					return i4m
				}
				i4m = {
					expires: -100
				}
			}
			i4m = i4m || o;
			var sD1x = X5c + "=" + (i4m.value || "") + ";";
			delete i4m.value;
			if (i4m.expires !== undefined) {
				de6Y.setTime(cKe3x + i4m.expires * biw3x);
				i4m.expires = de6Y.toGMTString()
			}
			sD1x += u.vX2x(i4m, ";");
			document.cookie = sD1x
		}
	}()
})();