// console.log("hello")

const plus_button = document.getElementById('repeat')

const wrapper_div = document.getElementById('wrapper')

plus_button.onclick = (e) => {
  e.preventDefault()
  wrapper_div.innerHTML += `<div>
  <p>
      <label for='log-name'>1. Name of Exercise</label><br>
      <input id='log-name' type='text' name='name' />
  </p>
  <p>
      <label for='log-sets'>Sets</label><br>
      <input id='log-sets' type='text' name='sets' />
  </p>
  <p>
      <label for='log-reps'>Reps</label><br>
      <input id='log-reps' type='text' name='reps' />
  </p>
  <p>
      <label for='log-weight'>Weight</label><br>
      <input id='log-weight' type='text' name='weight' />
  </p>
  </div>`
}
