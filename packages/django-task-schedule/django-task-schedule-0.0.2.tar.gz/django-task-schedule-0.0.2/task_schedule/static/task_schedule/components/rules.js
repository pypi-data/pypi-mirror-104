export const Rules = {
  required: value => (!!value || value === 0) || 'Required.',
  maxLength: maxLength => {
    return value => value.length <= maxLength || `Max ${maxLength} characters.`
  },
  number: (min, max) => {
    return value => {
      if (value === '' || value === undefined || value === null) {
        return true
      }
      if (typeof value !== 'string') {
       value = value.toString()
      }
      const valueInt = parseInt(value)
      if (value !== valueInt.toString()) {
        return 'Must be a number.'
      }
      if (min !== undefined && min !== null) {
        if (valueInt < min) {
          return `Must be greater than or equal to ${min}.`
        }
      }
      if (max !== undefined && max !== null) {
        if (valueInt > max) {
          return `Must be less than or equal to ${max}.`
        }
      }
      return true
    }
  }
}
