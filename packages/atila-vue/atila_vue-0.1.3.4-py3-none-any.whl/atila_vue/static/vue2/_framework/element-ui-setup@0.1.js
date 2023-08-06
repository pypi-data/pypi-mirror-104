interactionMethods.$uloading_ = null

interactionMethods.$uloading = function(text = null, opacity = 0.7) {
  const flag = !!text
  if (this.$uloading_ !== null) {
    this.$uloading_.close()
    this.$uloading_ = null
  }

  if (flag) {
    this.$uloading_ = this.$loading({
      lock: true,
      text: text,
      spinner: 'el-icon-loading',
      background: `rgba(0, 0, 0, ${opacity})`
    })
  }
}

interactionMethods.$unotify = function(title, message, type = 'info', duration = 3000, html = true, ok = "OK") {
  this.$notify({
    title: title,
    message: message,
    type: type,
    duration: duration,
    dangerouslyUseHTMLString: html,
    confirmButtonText: ok,
  })
}

interactionMethods.$usnackbar = function(message, type = 'info', duration = 3000, html = true) {
  this.$message({
    message: message,
    type: type,
    duration: durationduration,
    dangerouslyUseHTMLString: html
  })
}

interactionMethods.$ualert = function(title, message, callback = ((action) => {}), ok = "OK", html = true) {
  this.$alert(message, title, {
    confirmButtonText: ok,
    dangerouslyUseHTMLString: html,
    callback: (action) => callback(action)
  })
}

interactionMethods.$uconfirm = async function(title, message, type = 'warning', html = true, ok = "OK", cancel = 'Cancel') {
  try {
    answer = await this.$confirm(message, title, {
      confirmButtonText: ok,
      cancelButtonText: cancel,
      type: type,
      dangerouslyUseHTMLString: html
    })
    return true
  } catch (e) {
    return false
  }
}

interactionMethods.$uprompt = async function(title, message, inputPattern = null, inputErrorMessage = null, inputType = 'text', ok = "OK", cancel = 'Cancel') {
  try {
    ans = await this.$prompt(message, title, {
      confirmButtonText: ok,
      cancelButtonText: cancel,
      inputPattern: inputPattern,
      inputErrorMessage: inputErrorMessage,
      inputType: inputType
    })
    return ans.value
  } catch (e) {
    return null
  }
}

interactionMethods.$viewport = function () {
  const w = window.innerWidth
  if (w < 768) return 'xs'
  else if (w >= 1920) return 'xl'
  else if (w >= 1200) return 'lg'
  else if (w >= 992) return 'md'
  return 'sm'
}
