let $ = require('jquery')
let fs = require('fs')
let filename = 'contacts'

$('#add-to-database').on('click', () => {
   let date = $('#Date').val()
   let name = $('#Name').val()

   fs.appendFile('contacts', date + ',' + name + '\n')

   addEntry(date, name)
})

function addEntry(date, name, quantity, from, till, price) {
   if(date && name && quantity && from && till && price) {
      let updateString = '<tr><td class="date">'+ date + '</td><td class="name">'+ name +'</td><td class="qnt">' 
         + quantity +'</td><td class="from">' + from + '</td><td class="till">' + till +'</td><td class="price">'
         + price +'</td></tr>'
      $('#contact-table').append(updateString)
   }
}

function loadAndDisplayContacts() {  
   
   //Check if file exists
   if(fs.existsSync(filename)) {
      let data = fs.readFileSync(filename, 'utf8').split('\n')
      
      data.forEach((row, index) => {
         let [ date, name, quantity, from, till, price ] = row.split(',')
         addEntry(date, name, quantity, from, till, price)
      })
   
   } else {
      console.log("File Doesn\'t Exist. Creating new file.")
      fs.writeFile(filename, '', (err) => {
         if(err)
            console.log(err)
      })
   }
}

loadAndDisplayContacts()