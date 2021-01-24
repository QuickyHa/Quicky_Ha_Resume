const count = document.getElementById('count');

updateVisitCounter();

function updateVisitCounter() {
  fetch('https://m1c53403e0.execute-api.us-east-1.amazonaws.com/Prod/counter')
    .then(res => res.json()
      .then(data => {
        count.innerHTML = data
      })
    )
}