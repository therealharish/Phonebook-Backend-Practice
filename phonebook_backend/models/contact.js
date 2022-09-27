const mongoose = require("mongoose")
const url = process.env.MONGODB_URI

mongoose
    .connect(url)
    .then(result => {
        console.log("Connected to Databse");
    })
    .catch(error => {
        console.log("error connecting to MongoDB:", error.message);
    })

const contactSchema = new mongoose.Schema({
    name: String,
    number: Number
})

contactSchema.set('toJSON', {
    transform: (document, returnedObject) => {
      returnedObject.id = returnedObject._id.toString()
      delete returnedObject._id
      delete returnedObject.__v
    }
  })

module.exports = mongoose.model('Contact', contactSchema)