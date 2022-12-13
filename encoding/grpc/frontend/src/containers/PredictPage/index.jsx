import React, { useEffect, useMemo, useRef, useState } from "react";
import style from "./index.module.scss";
import { loadPredictions, popPrediction } from "./actions";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import _ from "lodash";
import TinderCard from "react-tinder-card";
import { IconButton } from "@mui/material";
import { Close, Favorite, Person, WineBar } from "@mui/icons-material";
import { Link } from "react-router-dom";
import FlippyCard from "../../components/FlippyCard";

const INITIAL_PREDICTION_NUMBER = 3;

const lastPredIndex = INITIAL_PREDICTION_NUMBER - 1;

const PredictPage = () => {
  const dispatch = useDispatch();
  const items = useSelector((state) => state.item.predictionQueue);
  const [currIndex, setCurrIndex] = useState(lastPredIndex);

  const canSwipe = !_.isEmpty(items);

  useEffect(() => {
    dispatch(loadPredictions(INITIAL_PREDICTION_NUMBER));
  }, [dispatch]);

  const itemRefs = useMemo(
    () =>
      Array(items.length)
        .fill(0)
        .map(() => React.createRef()),
    [items.length]
  );

  const swiped = (direction, nameToDelete, index) => {
    if (index === 2) {
      dispatch(loadPredictions(INITIAL_PREDICTION_NUMBER));
    }
    let idx = index - 1;
    if (index <= 2) {
      idx = index + lastPredIndex;
    }
    setCurrIndex(idx);
  };

  const outOfFrame = (name, index) => {
    dispatch(popPrediction());
  };

  const swipe = async (dir) => {
    if (canSwipe) {
      console.log(itemRefs);
      await itemRefs[currIndex].current.swipe(dir);
    }
  };

  return (
    <div className={style.predictionPage}>
      <div className={style.header}>
        <Link to="/profile">
          <IconButton>
            <Person fontSize="large" />
          </IconButton>
        </Link>
        <Link to="/catalog">
          <IconButton>
            <WineBar fontSize="large" />
          </IconButton>
        </Link>
      </div>
      <div className={style.predictionContainer}>
        <div className={style.cardContainer}>
          {_.map(items, (item, index) => {
            return (
              <TinderCard
                className={style.swipe}
                key={item.name}
                ref={itemRefs[index]}
                swipeThreshold={50}
                preventSwipe={["up", "down"]}
                onSwipe={(dir) => swiped(dir, item.name, index)}
                onCardLeftScreen={() => outOfFrame(item.name, index)}
              >
                <FlippyCard item={item} />
              </TinderCard>
            );
          })}
        </div>
        <div className={style.buttons}>
          <IconButton onClick={() => swipe("left")}>
            <Close
              style={{
                backgroundColor: !canSwipe && "#c3c4d3",
                color: "#ec5e6f",
              }}
              fontSize="large"
            />
          </IconButton>
          <IconButton onClick={() => swipe("right")}>
            <Favorite
              style={{
                backgroundColor: !canSwipe && "#c3c4d3",
                color: "#76e2b3",
              }}
              fontSize="large"
            />
          </IconButton>
        </div>
      </div>
    </div>
  );
};

export default PredictPage;
