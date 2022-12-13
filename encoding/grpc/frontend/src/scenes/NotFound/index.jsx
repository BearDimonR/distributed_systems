import React from "react";
import style from "./index.module.scss";
import { NavLink } from "react-router-dom";

const NotFound = () => (
  <div className={style.container}>
    <p className={style.title}>Page Not Found</p>
    <NavLink className={style.redirect} to="/">
      {" "}
      Go to predict page
    </NavLink>
  </div>
);

export default NotFound;
