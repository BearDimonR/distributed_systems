import _, { range } from "lodash";

const { CardsClient } = require('../protobufs/cards_grpc_web_pb');
const { CardRequest } = require('../protobufs/cards_pb');

const client = new CardsClient(process.env.REACT_APP_PROXY_URL, null, null);

export const getPrediction = async (nPredictions) => {
  let cards = [];
  let i = 0;

  const request = new CardRequest();
  while (nPredictions > i) {
    i++;
    request.setCardId(_.random(1, 5));
	
    cards.push(await new Promise((resolve, reject) => client.getCard(request, {}, (err, response) => {
          if (response == null) {
            reject(err)
          } else {
            resolve(response.toObject())
            return
        }})));
  }
  return cards;
};
