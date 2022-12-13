import _ from "lodash";
import { ADD_PREDICTIONS, POP_PREDICTION } from "./actions";

const initialState = {
  predictionQueue: [],
  catalog: [],
  totalPages: 1,
  page: 1,
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_PREDICTIONS:
      return {
        ...state,
        predictionQueue: _.concat(
          action.predictions || [],
          state.predictionQueue
        ),
      };
    case POP_PREDICTION:
      return {
        ...state,
        predictionQueue: _.dropRight(state.predictionQueue),
      };
    default:
      return state;
  }
};

export default reducer;
