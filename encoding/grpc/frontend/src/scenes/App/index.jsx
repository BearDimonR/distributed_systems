import { Provider } from "react-redux";

import store from "../../store";
import Routing from "../../containers/Routing";
import { BrowserRouter } from "react-router-dom";

const App = () => (
  <Provider store={store}>
    <BrowserRouter>
      <Routing />
    </BrowserRouter>
  </Provider>
);

export default App;
