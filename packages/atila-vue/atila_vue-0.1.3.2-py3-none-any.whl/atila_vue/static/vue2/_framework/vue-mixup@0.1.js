// vuex data loader ----------------------------------------
function _getTargetStore (schema, props) {
  let attr_name = schema.dataset.name
  let target_object = props.store
  const variables = schema.dataset.name.split ('.')
  if (variables.length == 2) {
    target_object = props.store [variables [0]]
    attr_name = variables [1]
  } else if (variables.length > 2) {
    throw new Error ('invalid map_data name')
  }
  return [target_object, attr_name]
}

function _getDataset (css, typeref) {
  const els = document.querySelectorAll (css)
  let rows = []
  els.forEach ((el, index) => {
  let row = {}
  for (let [key, val] of Object.entries (el.dataset)) {
    const t = typeof (typeref [key])
    if (val == 'null') {
      val = null
    } else if (t == 'boolean') {
      val = (val == 'true')
    } else if (t == 'number') {
      if (val.indexOf (".") != -1) {
        val = parseFloat (val)
      } else {
        val = parseInt (val)
      }
    }
    row [key] = val
  }
  rows.push (row)
  })
  return rows
}

vueInitMethods._getSchemaProps = function (schema) {
  let store = this.$store.state
  const type = schema.dataset.type
  const container = schema.dataset.container
  let dataSize = 0
  if (!!schema.dataset.maxSize) {
    dataSize = parseInt (schema.dataset.maxSize)
  }
  return {type, store, dataSize, container}
}

vueInitMethods._readSchemas = function () {
  const schemas = document.querySelectorAll ('#state-map > .veux-state')
  schemas.forEach (schema => {
  props = this._getSchemaProps (schema)
  let [target_object, attr_name] = _getTargetStore (schema, props)
  if (props.type == undefined) {
    let d = []
    for (let i = 0; i < props.dataSize; i++ ) {
      d.push (JSON.parse (schema.dataset.default))
    }
    target_object [attr_name] = d
  }
  else {
    target_object [attr_name] = ''
  }
  })
}

vueInitMethods._readDataset = function () {
  const schemas = document.querySelectorAll ('#state-map > .veux-state')
  for (let i=0; i<schemas.length; i++) {
    let schema = schemas [i]
    props = this._getSchemaProps (schema)

    let [target_object, attr_name] = _getTargetStore (schema, props)
    let typeref = target_object [attr_name]
    if (props.dataSize) {
      typeref = target_object [attr_name][0]
    }
    const container = document.querySelector (props.container)
    if (!!container) {
      if (props.type === 'html' && !!props.container) {
        target_object [attr_name] = container.innerHTML
      }
      else if (props.type === 'text' && !!props.container) {
        target_object [attr_name] = container.innerText
      }
      else {
        r = _getDataset (props.container, typeref)
        for (let i = 0; i < r.length; i++) {
          target_object [attr_name].splice (i, 1, r [i])
        }
      }
    }
  }
}

// export -----------------------------------
httpVueLoader.langProcessor ['babel'] = function (script) {
  return Babel.transform (script, {
    moduleId: this.name,
    presets: ['es2017', 'stage-3'],
    plugins: ['transform-es2015-modules-umd'],
  }).code
}
httpVueLoader.scriptExportsHandler = function (script) {
  return this.component.script.module.exports.default
}

axios.defaults.withCredentials = true
Vue.prototype.$http = axios
Vue.prototype.$bus = new Vue ()

function mapVuexItems () {
  return Vuex.mapState (['$debug', ...Object.keys (vuexItems)])
}

function websocketMethods () {
  return websocketMethods_
}

Object.assign (protoMethods, interactionMethods)
for (let [k, v] of Object.entries (protoMethods)) {
Vue.prototype [k] = v
}
Vue.prototype.$ut = vueUtilMethods
