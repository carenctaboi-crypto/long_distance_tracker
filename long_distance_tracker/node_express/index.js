import express from "express";
import bodyParser from "body-parser";
import { router } from "./routes.js";

const app = express();
app.use(bodyParser.json());

app.use("/", router);

const PORT = 8001;

app.listen(PORT, () => {
  console.log(` Node + Express Long Distance Tracker running on port ${PORT}`);
});
process.on("SIGINT", () => {
  console.log("\n Node + Express Long Distance Tracker shutting down");
  process.exit();
});