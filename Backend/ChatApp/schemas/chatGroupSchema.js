const mongoose = require("mongoose");

const ChatGroup = mongoose.model("ChatGroup", {
  userId1: String,
  name1: String,
  userId2: String,
  name2: String,
  // createdAt: { type: Date, expires: "2s", default: Date.now },
});

module.exports = ChatGroup;
