const { notEqual } = require('assert')
const mongoose = require('mongoose')

if(process.argv.length < 3) {
    console.log("Please provide valid arguments. Argument format - node mongo.js <password>")
    process.exit(0)
}

const password = process.argv[2]
// password = viix6PPKvtvfmwEx
const url = `mongodb+srv://harishaa827:${password}@cluster0.5ls4u.mongodb.net/phonebook_backend?retryWrites=true&w=majority`

const contactSchema = new mongoose.Schema({
    name: String,
    number: Number
})

const Contact = mongoose.model('Contact', contactSchema)

const postToServer = process.argv.length == 5 ? true: false

if(postToServer) {
    mongoose
    .connect(url)
    .then((result)=> {
        console.log('connected')
    })
    const contact = new Contact({
        name: process.argv[3],
        number: process.argv[4]
    })
    contact.save().then(result => {
        console.log(`added ${contact.name} number ${contact.number} to server`)
        return mongoose.connection.close()
    })
    .catch((err)=> console.log(err))
}
else {
    mongoose
    .connect(url)
    .then((result)=> {
        console.log('connected')
    })
    Contact.find({}).then(result => {
        console.log('phonebook:')
        result.forEach(contact => {
            console.log(contact.name+" "+contact.number)
        })
        return mongoose.connection.close()
    })
    .catch((err)=> console.log(err))
}



