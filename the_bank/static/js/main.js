const displayError = document.getElementById('displayError')
const displayMessage = document.getElementById('displayMessage')

const openAccount = document.getElementById('openAccount')
const viewAccount = document.getElementById('viewAccount')
const closeAccount = document.getElementById('closeAccount')

const openAccountForm = document.getElementById('openAccountForm')
const viewAccountForm = document.getElementById('viewAccountForm')
const closeAccountForm = document.getElementById('closeAccountForm')

const openAccountConfirm = document.getElementById('openAccountConfirm')
const viewAccountConfirm = document.getElementById('viewAccountConfirm')
const closeAccountConfirm = document.getElementById('closeAccountConfirm')

const displayAccount = document.getElementById('displayAccount')
const displayAccountHolder = document.getElementById('displayAccountHolder')
const displayAccountBalance = document.getElementById('displayAccountBalance')
const deposit = document.getElementById('deposit')
const withdraw = document.getElementById('withdraw')

const displayDeposit = document.getElementById('displayDeposit')
const displayDepositHolder = document.getElementById('displayDepositHolder')
const depositConfirm = document.getElementById('depositConfirm')

const displayWithdraw = document.getElementById('displayWithdraw')
const displayWithdrawHolder = document.getElementById('displayWithdrawHolder')
const withdrawConfirm = document.getElementById('withdrawConfirm')

const closeAllForms = () => {
  openAccountForm.style.display = 'none'
  viewAccountForm.style.display = 'none'
  closeAccountForm.style.display = 'none'
}

const clearRightSide = () => {
  closeAllForms()
  displayError.style.display = 'none'
  displayMessage.style.display = 'none'
  displayAccount.style.display = 'none'
  displayDeposit.style.display = 'none'
  displayWithdraw.style.display = 'none'
}

const showDisplayAccount = (holder, balance) => {
  displayAccount.style.display = 'block'
  displayAccountHolder.innerHTML = holder
  displayAccountBalance.innerHTML = balance
}

const showDisplayError = error => {
  displayError.style.display = 'block'
  displayError.innerHTML = error
}

const showDisplayMessage = message => {
  displayMessage.style.display = 'block'
  displayMessage.innerHTML = message
}

openAccount.addEventListener('click', () => {
  clearRightSide()
  openAccountForm.style.display = 'block'
})

viewAccount.addEventListener('click', () => {
  clearRightSide()
  viewAccountForm.style.display = 'block'
})

deposit.addEventListener('click', () => {
  const holder = displayAccountHolder.innerHTML
  clearRightSide()
  displayDeposit.style.display = 'block'
  displayDepositHolder.innerHTML = holder
})

withdraw.addEventListener('click', () => {
  const holder = displayAccountHolder.innerHTML
  clearRightSide()
  displayWithdraw.style.display = 'block'
  displayWithdrawHolder.innerHTML = holder
})

closeAccount.addEventListener('click', () => {
  clearRightSide()
  closeAccountForm.style.display = 'block'
})

openAccountConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('openAccountHolder')
  const password = document.getElementById('openPassword')
  axios.post('/api/account', {
    holder: accountHolder.value,
    password: password.value
  }).then(response => {
    accountHolder.value = ''
    password.value = ''
    closeAllForms()
    if (response.data.error) {
      showDisplayError(response.data.error)
    } else {
      showDisplayMessage(response.data.message)
    }
  }).catch(error => {
    console.log(error)
  })
})

viewAccountConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('viewAccountHolder')
  const password = document.getElementById('viewPassword')
  axios.put('/api/account', {
    holder: accountHolder.value,
    password: password.value
  }).then(response => {
    accountHolder.value = ''
    password.value = ''
    clearRightSide()
    if (response.data.error) {
      showDisplayError(response.data.error)
    } else {
      showDisplayAccount(response.data.holder, response.data.balance)
      axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`
    }
  }).catch(error => {
    console.log(error)
    accountHolder.value = ''
    password.value = ''
    clearRightSide()
    showDisplayMessage('Incorrect Password')
  })
})

depositConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('displayDepositHolder').innerHTML
  const amount = document.getElementById('depositAmount')
  axios.post(`/api/account/${accountHolder}/deposit`, {
    amount: +amount.value
  }).then(response => {
    amount.value = 0
    clearRightSide()
    if (response.data.error) {
      showDisplayError(response.data.error)
    } else {
      showDisplayMessage(response.data.message)
      showDisplayAccount(response.data.holder, response.data.balance)
    }
  }).catch(error => {
    console.log(error)
  })
})

withdrawConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('displayWithdrawHolder').innerHTML
  const amount = document.getElementById('withdrawAmount')
  axios.post(`/api/account/${accountHolder}/withdraw`, {
    amount: +amount.value
  }).then(response => {
    amount.value = 0
    clearRightSide()
    if (response.data.error) {
      showDisplayError(response.data.error)
    } else {
      showDisplayMessage(response.data.message)
      showDisplayAccount(response.data.holder, response.data.balance)
    }
  }).catch(error => {
    console.log(error)
  })
})

closeAccountConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('closeAccountHolder')
  const password = document.getElementById('closePassword')
  axios.delete('/api/account', {
    data: {
      holder: accountHolder.value,
      password: password.value
    }
  }).then(response => {
    accountHolder.value = ''
    password.value = ''
    clearRightSide()
    if (response.data.error) {
      showDisplayError(response.data.error)
    } else {
      showDisplayMessage(response.data.message)
    }
  }).catch(error => {
    console.log(error)
    accountHolder.value = ''
    password.value = ''
    clearRightSide()
    showDisplayMessage('Incorrect Password')
  })
})
