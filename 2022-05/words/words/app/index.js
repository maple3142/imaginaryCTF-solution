const express = require("express");
const mongoose = require("mongoose");

const definitionSchema = new mongoose.Schema({
  word: String,
  definition: String,
});

const definitionModel = new mongoose.model("definitions", definitionSchema);

const app = express();
app.use(express.json());
app.use(express.static("public"));

// Handle errors parsing json in request body
app.use((err, req, res, next) => {
  if (err instanceof SyntaxError) {
    console.error(err);
    return res.status(400).json({ error: "Invalid request body" });
  }
  next();
});

// Connect to mongo
mongoose.connect("mongodb://words-db:27017/", {
  user: process.env.MONGO_INITDB_ROOT_USERNAME,
  pass: process.env.MONGO_INITDB_ROOT_PASSWORD,
  dbName: process.env.MONGO_INITDB_DATABASE,
});

mongoose.connection.once("open", () => {
  console.log("Connection to the Database is On! ");
});

// Return a random word we have a definition for
app.get("/api/random", async (req, res) => {
  try {
    const randomDefinitionArray = await definitionModel.aggregate().sample(1);

    if (randomDefinitionArray.length === 1) {
      const randomDefinition = randomDefinitionArray[0];
      return res.json({
        word: randomDefinition.word,
      });
    }
  } catch (err) {
    console.log(err.message);
  }

  return res.json({
    word: "default",
  });
});

// Get the definition of a word
app.post("/api/definition", async (req, res) => {
  if (!("word" in req.body)) {
    res.status(400);
    return res.json({ error: "Parameter 'word' is required" });
  }

  const { word } = req.body;

  // Did you think it would be this easy?
  if (word == "flag") {
    return res.json({
      word: "flag",
      definition:
        "a piece of cloth, usually rectangular and fixed to a pole at one edge, that has a pattern that shows it represents a country or a group, or has a particular meaning",
    });
  }

  // No NoSQL injection without $
  if (JSON.stringify(req.body).includes("$")) {
    return res.json({
      word: "dollar",
      definition:
        "the basic monetary unit of the US, Canada, Australia, and certain countries in the Pacific, Caribbean, SE Asia, Africa, and South America.",
    });
  }

  try {
    const result = await definitionModel.findOne({ word: word }).exec();
    if (result) {
      return res.json({
        word: result.word,
        definition: result.definition,
      });
    }
  } catch (err) {
    console.log(err.message);
  }

  res.status(404);
  return res.json({ error: "No definition found" });
});

app.listen(3000, () => {
  console.log("App listening on port 3000");
});
