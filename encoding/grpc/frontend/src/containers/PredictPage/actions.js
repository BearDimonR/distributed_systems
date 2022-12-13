import { getPrediction } from "../../services/itemService";
import { handleError } from "../../utils/shared";

export const ADD_PREDICTIONS = "ITEM_ACTION:ADD_PREDICTIONS";
export const POP_PREDICTION = "ITEM_ACTION:POP_PREDICTION";

export const loadPredictions = (nPredictions) => async (dispatch) => {
  handleError(async () => {
    const items = await getPrediction(nPredictions);
    dispatch(addPredictions(items));
  });
};

const addPredictions = (predictions) => async (dispatch) =>
  dispatch({
    type: ADD_PREDICTIONS,
    predictions,
  });

export const popPrediction = () => async (dispatch) => {
  dispatch({
    type: POP_PREDICTION,
  });
};
