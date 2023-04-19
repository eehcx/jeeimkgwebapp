let date = new Date();
let month = date.toLocaleString('default', { month: 'long' });
let day = date.getDate();
document.querySelector('.date-title strong').innerHTML = `${month}, ${day}`;