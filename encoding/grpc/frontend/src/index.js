import React from "react";
import ReactDOM from "react-dom";
import "./index.scss";
import "./styles/reset.scss";
import "./styles/common.scss";
import App from "./scenes/App";
import "react-toastify/dist/ReactToastify.css";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
