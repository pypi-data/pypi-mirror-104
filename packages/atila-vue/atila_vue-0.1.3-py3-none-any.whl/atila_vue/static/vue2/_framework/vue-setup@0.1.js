Number.prototype.format = function () {
  if(this==0) return "0"
  var reg = /(^[+-]?\d+)(\d{3})/
  var n = (this + '')
  while (reg.test(n)) n = n.replace (reg, '$1' + ',' + '$2')
    return n
}
String.prototype.format = function () {
  var num = parseFloat (this)
  if( isNaN(num) ) return "0"
  return num.format ()
}
String.prototype.titleCase = function () {
  return this.replace (/\w\S*/g, function (txt) {return txt.charAt(0).toUpperCase () + txt.substr (1).toLowerCase ();})
}
Date.prototype.format = function(f) {
  if (!this.valueOf()) return " "
  var d = this;
  return f.replace(/(%Y|%y|%m|%d|%H|%I|%M|%S|%p|%a|%A|%b|%B|%w|%c|%x|%X|%k|%n|%D)/gi, function($1) {
    switch ($1) {
      case "%Y":
        return d.getFullYear()
      case "%y":
        return (d.getFullYear() % 1000).zfill(2)
      case "%m":
        return (d.getMonth() + 1).zfill(2)
      case "%d":
        return d.getDate().zfill(2);
      case "%H":
        return d.getHours().zfill(2)
      case "%I":
        return ((h = d.getHours() % 12) ? h : 12).zfill(2)
      case "%M":
        return d.getMinutes().zfill(2)
      case "%S":
        return d.getSeconds().zfill(2)
      case "%p":
        return d.getHours() < 12 ? "AM" : "PM"
      case "%w":
        return d.getDay()
      case "%c":
        return d.toLocaleString()
      case "%x":
        return d.toLocaleDateString()
      case "%X":
        return d.toLocaleTimeString()
      case "%b":
        return ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][d.getMonth()]
      case "%B":
        return ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][d.getMonth()]
      case "%a":
        return ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][d.getDay()]
      case "%A":
        return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][d.getDay()]
      case "%k":
        return ['일', '월', '화', '수', '목', '금', '토'][d.getDay()]
      case "%n":
        return ( d.getMonth() + 1)
      case "%D":
        return d.getDate()
      default:
        return $1
    }
  })
}
String.prototype.repeat = function(len){var s = '', i = 0; while (i++ < len) { s += this; } return s;}
String.prototype.zfill = function(len){return "0".repeat(len - this.length) + this}
Number.prototype.zfill = function(len){return this.toString().zfill(len)}

function get_csrf () {
  const meta = document.querySelector ('head > meta[name=csrf]')
  if (meta == null) {
    return null
  }
  const [token, name] = meta.getAttribute ('content').split (';')
  return {token, name}
}

// session parsing -----------------------------
function unint8array (decoded) {
  let arr = []
  for (let i = 0; i < decoded.length; i++) {
    arr.push (decoded.charCodeAt(i))
  }
  return new Uint8Array (arr)
}

function bytes2string (bytes) {
  let decoded = atob (bytes)
  if (decoded.charCodeAt(0) == 88) {
    decoded = decoded.substring (5, decoded.length - 3)
    return new TextDecoder().decode (unint8array (decoded))
  }
  else if (decoded.charCodeAt(0) == 78) { // None
    return null
  }
  else if (decoded.charCodeAt(0) == 77) { // short int
    decoded = decoded.substring (1, 3)
    return new Int16Array (unint8array (decoded).buffer) [0]
  }
  else if (decoded.charCodeAt(0) == 75) { // char int
    decoded = decoded.substring (1, 2)
    return new Int8Array (unint8array (decoded).buffer) [0]
  }
  else if (decoded.charCodeAt(0) == 74) { // int
    decoded = decoded.substring (1, 5)
    return new Int32Array (unint8array (decoded).buffer) [0]
  }
  throw new Error ('Unknown pickle type')
}

function parse_session () {
  let session = null
  for (let each of document.cookie.split ("; ")) {
    if (each.indexOf ('ATLSES_STK=') == 0) {
      session = each
      break
    }
  }
  if (!session) {
    return null
  }
  const user = {}
  const sessionval = session.split ('?')
  if (sessionval.length == 1) {
    return null
  }
  for (let each of sessionval [1].split ('&')) {
    const [name, val] = each.split ('=')
    if (name == 'nick_name' || name == 'uid' || name == 'lev' || name == 'status') {
      user [name] = bytes2string (val)
    }
  }
  return user
}

function load_script (src, callback = () => {}) {
  let current = null
  if (typeof (src) === "string") {
    current = src
    src = []
  } else {
    current = src.shift ()
  }
  var script = document.createElement('script')
  script.setAttribute('src', current)
  script.setAttribute('async', true)
  if (src.length) {
    script.addEventListener('load', () => { this.$load_script (src, callback) })
  } else {
    script.addEventListener('load', callback)
  }
  document.head.appendChild(script)
}

protoMethods.$load_script = load_script

protoMethods.$nnotify = function (title, message, icon, timeout = 5000) {
  var options = {
    body: message,
    icon: icon
  }
  const n = new Notification(title, options)
  n.onclick = (event) => {
  n.close ()
  }
  n.onshow = (event) => {
  setTimeout(function(){ n.close () }, timeout)
  }
}

protoMethods.$get_ref_from_parent = function (ref) {
  return this.$parent.$parent.$parent.$refs [ref]
}

protoMethods.$set_cloak = function (flag) {
  this.$store.state.$cloak = flag
}

protoMethods.$log = function (msg, type = 'info') {
  if (this.$debug) {
    console.log (`[${type}] ${msg}`)
  }
}

protoMethods.$traceback = function (e) {
  let msg = ''
  if (e.response !== undefined) {
    const r = e.response
    let code = r.data.code || 70000
    let message = r.data.message || 'no message'
    this.$log (JSON.stringify(r.data), 'expt')
    msg = `${message} (status: ${r.status}, error: ${code})`
  }
  else {
    msg = `${e.name}: ${e.message}`
  }
  console.log (e)
  this.$log (e, 'expt')
  return msg
}

protoMethods.$mediafor = function (url) {
  return url
}

protoMethods.$sleep = function (ms) {
  return new Promise (resolve => setTimeout(resolve, ms))
}

protoMethods.$urlfor = function (name, args = [], _kargs = {}) {
  const target = this.$urlspecs [name]
  if (!target) {
    throw new Error (`route ${name} not found`)
  }

  let url = target.path

  let kargs = {}
  if (Object.prototype.toString.call(args).indexOf ("Array") != -1) {
    let i = 0
    for (let k of target.params) {
      kargs [k] = args [i]
      i += 1
    }
    for (let k of target.query) {
      kargs [k] = args [i]
      i += 1
    }
  } else {
   kargs = args
  }

  for (let k of target.params) {
    if (kargs [k] !== undefined ) {
      url = url.replace (":" + k, kargs [k])
    }
  }

  let newquery = ''
  for (let k of target.query) {
    if (kargs [k] === undefined ) {
      continue
    }
  const v = kargs [k]
  if (!!newquery) {
    newquery += '&'
  }
  newquery += k + "=" + encodeURIComponent (v)
  }

  if (!!newquery) {
    return url + "?" + newquery
  }
  return url
}

protoMethods.$build_url = function (baseurl, kargs = {}) {
  let url = baseurl
  let newquery = ''
  for (let [k, v] of Object.entries (kargs)) {
    if (v === null) {
      continue
    }
  if (!!newquery) {
    newquery += '&'
  }
  newquery += k + "=" + encodeURIComponent (v)
  }
  if (!!newquery) {
    return url + "?" + newquery
  }
  return url
}

const _deviceDetect = {
  android: function() {
    return navigator.userAgent.match(/Android/i)
  },
  ios: function() {
    return navigator.userAgent.match(/iPhone|iPad|iPod/i)
  },
  mobile: function() {
    return (deviceDetect.android() || deviceDetect.ios())
  },
  touchable: function () {
    return (navigator.maxTouchPoints || 'ontouchstart' in document.documentElement)
  },
  rotatable: function () {
    return window.orientation > -1
  },
  width: function () {
    return window.innerWidth
  },
  height: function () {
    return window.innerHeight
  }
}

protoMethods.$device = _deviceDetect

vueUtilMethods.date = function (dt = null) {
  if (dt === null) {
    return new Date ()
  }
  if (dt.indexOf ('-') === -1) {
    return new Date (parseFloat (dt) * 1000.)
  }
  const [a, b] = dt.split (' ')
  const [Y, m, d] = a.split ("-")
  const [H, M, S] = b.substring (0, 8).split (":")
  return new Date (Date.UTC (Y, parseInt (m) - 1, d, H, M, S))
}

// websocket -------------------------------------------
const websocketMethods_ = {
  $_wsconnectex () {
    this.$websocket.sock = new WebSocket (this.$websocket.url)
    this.$websocket.sock.onopen = this.$_handle_wsconnect
    this.$websocket.sock.onclose = this.$_handle_wsclose
    this.$websocket.sock.onerror = this.$_handle_wserror
    this.$websocket.sock.onmessage = this.$websocket.read_handler
  },
  $_handle_wsconnect() {
    this.$websocket.connected = true
    this.$log ('connected', 'websocket')
    this.$_handle_wswrite ()
  },
  $_handle_wswrite () {
  for (var i = 0; i < this.$websocket.buffer.length; i++) {
    msg = this.$websocket.buffer.shift ()
    this.$log (`send: ${ msg }`, 'websocket')
    this.$websocket.sock.send (msg)
  }
  },
  $_handle_wsclose (evt) {
    this.$websocket.sock = null
    this.$log ('closed', 'websocket')
  },
  $_handle_wserror (evt)	{
    this.$log (evt.data, 'error')
  },

  $wsconnect (url, read_handler = (evt) => this.$log (evt.data)) {
    // lazy connect on wpush, it is more reliable on disconnected
    if (url.indexOf ('/') == 0) {
      url = location.origin.replace(/^http/, 'ws') + url
    }
    this.$websocket.url = url
    this.$websocket.read_handler = read_handler
  },
  $wsclose (evt) {
    this.$websocket.connected = false
    this.$websocket.sock.close ()
  },
  $wspush (msg) {
    if (!msg) { return }
      this.$websocket.buffer.push (msg)
      if (this.$websocket.sock == null) {
        this.$_wsconnectex ()
        return
    }
    if (!this.$websocket.connected) {
      return
    }
    this.$_handle_wswrite ()
  },
}


class CachableStorage {
  constructor (loc) {
    if (loc == 'session') {
      this.__s = window.sessionStorage
    } else {
      this.__s = window.localStorage
    }
  }
  now () {
    return Math.floor(new Date().getTime() / 1000)
  }
  set (name, data, timeout = 0) {
    this.__s.setItem (name, JSON.stringify ([ timeout ? this.now () + timeout : 0, data ]))
  }
  get (name) {
    const _val = this.__s.getItem (name)
    if (_val == null) {
      return null
    }
    const _cached = JSON.parse (_val)
    if (_cached [0] && _cached [0] < this.now ()) {
      this.remove (name)
      return null
    }
    return _cached [1]
  }
  remove (name) {
    this.__s.removeItem (name)
  }
  clear () {
    this.__s.clear ()
  }
}

function prefetch (href) {
  const s = document.createElement('link')
  s.rel = 'prefetch'
  s.as = 'fetch'
  s.href = href
  document.body.appendChild (s)
}

vuexItems.$user = parse_session ()
vuexItems.$location = location
vuexItems.$location.uri = location.pathname + (location.search || '') + (location.hash || '')
vuexItems.$csrf = get_csrf ()
vuexItems.$websocket = {sock: null, url: null, buffer: [], read_handler: null, connected: false}
vuexItems.$ls = new CachableStorage ('local')
vuexItems.$ss = new CachableStorage ('session')
