import "./App.css";
import Dashboard from "./components/Dashboard";
import { QueryClient, QueryClientProvider } from "react-query";
import { BrowserRouter } from "react-router-dom";
import store from "./store";
import { Provider } from "react-redux";

const queryClient = new QueryClient();

function App() {
  return (
    <BrowserRouter>
      <QueryClientProvider client={queryClient}>
        <Provider store={store}>
          <Dashboard />
        </Provider>
      </QueryClientProvider>
    </BrowserRouter>
  );
}

export default App;
