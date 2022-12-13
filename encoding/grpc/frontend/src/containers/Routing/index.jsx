import React from "react";
import { Route, Routes } from "react-router-dom";
import classNames from "classnames";
import style from "./index.module.scss";

import NotFound from "../../scenes/NotFound";
import PredictPage from "../PredictPage";

const Routing = () => {
  return (
    <div className="fill">
      <main className={classNames("fill", style.page)}>
        <Routes>
          <Route path="/" exact element={<PredictPage />} />
          <Route path="*" exact element={<NotFound />} />
        </Routes>
      </main>
    </div>
  );
};

export default Routing;
