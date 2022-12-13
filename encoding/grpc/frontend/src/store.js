import { createStore, applyMiddleware, compose, combineReducers } from "redux";
import thunk from "redux-thunk";
import itemReducer from "./containers/PredictPage/reducer";

const initialState = {};

const middlewares = [thunk];

const reducers = {
  item: itemReducer,
};

const rootReducer = combineReducers({
  ...reducers,
});

const store = createStore(
  rootReducer,
  initialState,
  compose(applyMiddleware(...middlewares))
);

export default store;
